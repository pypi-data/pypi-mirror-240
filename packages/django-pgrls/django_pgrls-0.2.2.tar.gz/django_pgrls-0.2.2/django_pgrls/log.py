import logging
from typing import Any

from django_pgrls.state import get_current_tenant


class SchemaContextFilter(logging.Filter):
    """
    Add current tenant information to log records.
    """

    def filter(self, record: Any) -> bool:
        tenant = get_current_tenant()

        if tenant is not None:
            record.tenant_id = tenant.id
            record.domain_url = getattr(tenant, "domain_url")
            record.folder = getattr(tenant, "folder")

        return True
