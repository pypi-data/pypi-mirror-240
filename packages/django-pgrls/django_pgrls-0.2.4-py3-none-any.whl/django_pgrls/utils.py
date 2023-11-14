from typing import TYPE_CHECKING

from django.apps import apps
from django.db import models
from django.utils.functional import lazy

from django_pgrls.settings import get_domain_model_path, get_tenant_model_path
from django_pgrls.state import get_current_tenant

if TYPE_CHECKING:
    from django_pgrls.models import TenantModel  # pragma: no cover
    from django_pgrls.routing.models import DomainModel  # pragma: no cover


def get_tenant_verbose_name() -> str | None:
    return get_tenant_model()._meta.verbose_name


get_tenant_verbose_name_lazy = lazy(get_tenant_verbose_name, str)


def get_tenant_fk_field_name() -> str:
    return get_tenant_model_path().split(".")[1].lower()


def get_tenant_fk_field(*, related_name: str | None = None) -> models.ForeignKey:
    return models.ForeignKey(
        get_tenant_model_path(),
        verbose_name=get_tenant_verbose_name_lazy(),
        default=get_current_tenant,
        on_delete=models.CASCADE,
        related_name=related_name or "+",
    )


def get_tenant_model(require_ready: bool = True) -> type["TenantModel"]:
    "Returns the tenant model."

    return apps.get_model(get_tenant_model_path(), require_ready=require_ready)


def get_domain_model(require_ready: bool = True) -> type["DomainModel"]:
    "Returns the domain model."

    return apps.get_model(get_domain_model_path(), require_ready=require_ready)
