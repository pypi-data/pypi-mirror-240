from typing import Any

from asgiref.sync import sync_to_async
from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.db.models import fields

from django_pgrls.constraints import RowLevelSecurityConstraint
from django_pgrls.queries import TenantBoundQueryset, TenantBypassQueryset
from django_pgrls.routing.info import RoutingInfo
from django_pgrls.state import TenantConstraint, active, get_current_tenant
from django_pgrls.utils import (
    get_tenant_fk_field,
    get_tenant_fk_field_name,
    get_tenant_model_path,
)


class TenantModel(models.Model):
    routing: RoutingInfo = None

    class Meta:
        abstract = True

    def __enter__(self) -> None:
        tenant = active.get()
        if tenant is not TenantConstraint.ALL:
            self._previous_active_token = active.set(self)

    __aenter__ = sync_to_async(__enter__)

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _previous_active_token = getattr(self, "_previous_active_token", None)
        if _previous_active_token is not None:
            active.reset(_previous_active_token)

    __aexit__ = sync_to_async(__exit__)


class TenantBoundModelBase(models.base.ModelBase):
    def __new__(cls, name: str, bases: tuple, attrs: dict, **kwargs: object) -> Any:
        new_class = super().__new__(cls, name, bases, attrs, **kwargs)
        meta = new_class._meta

        if meta.abstract or meta.proxy:
            return new_class

        relation_field: str | None = None

        for field in meta.local_fields:
            try:
                if (
                    field.one_to_one or field.many_to_one
                ) and field.remote_field.model._meta.label == get_tenant_model_path():
                    relation_field = field.name
                    if field.default is fields.NOT_PROVIDED:
                        field.default = get_current_tenant
                    break
            except AttributeError:
                continue

        if relation_field is None:
            try:
                relation_field = get_tenant_fk_field_name()
                field = meta.get_field(relation_field)
            except FieldDoesNotExist:
                pass
            else:
                relation_field = f"{meta.model_name}_{relation_field}"

            new_class.add_to_class(relation_field, get_tenant_fk_field())

        if hasattr(new_class, "unbound_objects"):
            meta.base_manager_name = "unbound_objects"

        if relation_field is not None and not any(
            isinstance(constraint, RowLevelSecurityConstraint) for constraint in meta.constraints
        ):
            constraint_name = "_".join(["rls", *meta.label_lower.split(".")])
            meta.constraints.append(
                RowLevelSecurityConstraint(relation_field, name=constraint_name)
            )
            meta.original_attrs["constraints"] = meta.constraints

        return new_class


class TenantBoundManager(models.Manager.from_queryset(TenantBoundQueryset)):  # type: ignore[misc]
    pass


class TenantBypassManager(models.Manager.from_queryset(TenantBypassQueryset)):  # type: ignore[misc]
    pass


class TenantBoundModel(models.Model, metaclass=TenantBoundModelBase):
    objects = TenantBoundManager()
    unbound_objects = TenantBypassManager()

    class Meta:
        abstract = True
