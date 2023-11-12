from typing import Any

from django.core.exceptions import ImproperlyConfigured
from django.db.utils import DatabaseError
from django.utils.asyncio import async_unsafe

from django_pgrls.postgresql.schema import DatabaseSchemaEditor
from django_pgrls.settings import get_original_backend_module
from django_pgrls.state import TenantConstraint, active

try:
    try:
        import psycopg as _psycopg
    except ImportError:
        import psycopg2 as _psycopg  # type: ignore[no-redef]
except ImportError:
    raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")


original_backend = get_original_backend_module()


class DatabaseWrapper(original_backend.DatabaseWrapper):  # type: ignore[name-defined]
    SchemaEditorClass = DatabaseSchemaEditor

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.tenant_pk: str | None = None
        self._setting_tenant_pk = False
        super().__init__(*args, **kwargs)

    @async_unsafe
    def close(self) -> None:
        self.tenant_pk = None
        self._setting_tenant_pk = False
        super().close()

    @async_unsafe
    def rollback(self) -> None:
        self.tenant_pk = None
        self._setting_tenant_pk = False
        super().rollback()

    def _handle_tenant(self, cursor: Any = None) -> None:
        tenant = active.get()

        tenant_pk: str = tenant.value if isinstance(tenant, TenantConstraint) else str(tenant.pk)

        skip = self._setting_tenant_pk or self.tenant_pk == tenant_pk

        if not skip:
            self._setting_tenant_pk = True
            cursor_for_tenant = self.connection.cursor() if cursor is None else cursor

            try:
                cursor_for_tenant.execute(f"SET app.tenant_id = '{tenant_pk}';")
            except (DatabaseError, _psycopg.InternalError):
                self.tenant_pk = None
            else:
                self.tenant_pk = tenant_pk
            finally:
                self._setting_tenant_pk = False

            if cursor is None:
                cursor_for_tenant.close()

    def _cursor(self, name: Any = None) -> Any:
        cursor = super()._cursor(name=name)

        cursor_for_tenant = cursor if name is None else None  # Named cursors cannot be reused
        self._handle_tenant(cursor_for_tenant)

        return cursor
