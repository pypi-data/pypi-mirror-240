from typing import Any

from asgiref.sync import sync_to_async
from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.db.models import fields

from django_pgrls.constraints import RowLevelSecurityConstraint
from django_pgrls.managers import TenantBoundManager, TenantBypassManager
from django_pgrls.state import TenantConstraint, active, get_current_tenant
from django_pgrls.utils import (
    get_tenant_fk_field,
    get_tenant_fk_field_name,
    get_tenant_model_path,
)


class TenantModel(models.Model):
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


class TenantBoundBase(models.base.ModelBase):
    def __new__(cls, name: str, bases: tuple, attrs: dict, **kwargs: object) -> Any:
        new_class = super().__new__(cls, name, bases, attrs, **kwargs)
        meta = new_class._meta

        if meta.abstract or meta.proxy:
            return new_class

        fk_field: str | None = None

        for field in meta.local_fields:
            if (
                field.one_to_one or field.many_to_one
            ) and field.remote_field.model._meta.label == get_tenant_model_path():
                fk_field = field.name
                if field.default is fields.NOT_PROVIDED:
                    field.default = get_current_tenant
                break

        if fk_field is None:
            try:
                fk_field = get_tenant_fk_field_name()
                field = meta.get_field(fk_field)
            except FieldDoesNotExist:
                pass
            else:
                fk_field = f"{meta.model_name}_{fk_field}"

            new_class.add_to_class(fk_field, get_tenant_fk_field())

        if fk_field is not None and not any(
            isinstance(constraint, RowLevelSecurityConstraint) for constraint in meta.constraints
        ):
            meta.constraints.append(
                RowLevelSecurityConstraint(
                    fk_field,
                    name="_".join(["rls", *meta.label_lower.split(".")]),
                )
            )
            meta.original_attrs["constraints"] = meta.constraints

        return new_class


class TenantBoundModel(models.Model, metaclass=TenantBoundBase):
    objects = TenantBoundManager()
    unbound_objects = TenantBypassManager()

    class Meta:
        abstract = True
