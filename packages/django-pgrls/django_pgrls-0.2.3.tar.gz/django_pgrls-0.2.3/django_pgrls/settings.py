from importlib import import_module
from typing import Any, Callable

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_tenant_model_path() -> str:
    TENANT_MODEL = getattr(settings, "TENANT_MODEL", None)

    if TENANT_MODEL is None:
        raise ImproperlyConfigured("TENANT_MODEL not found in settings")

    return TENANT_MODEL


def get_domain_model_path() -> str:
    DOMAIN_MODEL = getattr(settings, "DOMAIN_MODEL", None)

    if DOMAIN_MODEL is None:
        raise ImproperlyConfigured("DOMAIN_MODEL not found in settings")

    return DOMAIN_MODEL


def get_original_backend() -> str:
    return getattr(settings, "ORIGINAL_BACKEND", "django.db.backends.postgresql")


def get_original_backend_module() -> Any:
    return import_module(get_original_backend() + ".base")


def get_tenant_session_key() -> str:
    tenant_name = get_tenant_model_path().split(".")[1].lower()
    return getattr(settings, "TENANT_SESSION_KEY", f"{tenant_name}_id")


def get_tenant_header() -> str:
    tenant_name = get_tenant_model_path().split(".")[1].lower()
    return getattr(settings, "TENANT_HEADER", f"{tenant_name}-id")


def get_storage_pathname() -> Callable[[Any], str] | None:
    return getattr(settings, "TENANT_PATHNAME_FUNCTION", None)
