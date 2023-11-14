import logging
from typing import Any

from django_pgrls.routing.info import DomainInfo
from django_pgrls.state import get_current_tenant
from django_pgrls.utils import get_tenant_fk_field_name


class SchemaContextFilter(logging.Filter):
    """
    Add current tenant information to log records.
    """

    def filter(self, record: Any) -> bool:
        tenant = get_current_tenant()

        if tenant is not None:
            tenant_field = f"{get_tenant_fk_field_name()}_id"
            setattr(record, tenant_field, tenant.id)
            match tenant.routing:
                case DomainInfo(url, folder):
                    record.domain_url = url
                    record.folder = folder
                case _:
                    pass

        return True
