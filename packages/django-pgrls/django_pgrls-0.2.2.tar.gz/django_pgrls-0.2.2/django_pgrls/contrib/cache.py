from django_pgrls.state import get_current_tenant


def make_key(key: str, key_prefix: str, version: str) -> str:
    """
    Tenant aware function to generate a cache key.
    """
    tenant = get_current_tenant()

    if tenant is None:
        return "%s:%s:%s" % (key_prefix, version, key)

    return "%s:%s:%s:%s" % (key_prefix, version, key, tenant.pk)


def reverse_key(key: str) -> str:
    """
    Tenant aware function to reverse a cache key.
    """
    return key.split(":", 3)[2]
