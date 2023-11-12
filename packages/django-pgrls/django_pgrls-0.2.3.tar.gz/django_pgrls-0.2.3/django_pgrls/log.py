import logging
from typing import Any

from django_pgrls.routing.info import DomainInfo
from django_pgrls.state import get_current_tenant


class SchemaContextFilter(logging.Filter):
    """
    Add current tenant information to log records.
    """

    def filter(self, record: Any) -> bool:
        tenant = get_current_tenant()

        if tenant is not None:
            record.tenant_id = tenant.id
            match tenant.routing:
                case DomainInfo(url, folder):
                    record.domain_url = url
                    record.folder = folder
                case _:
                    pass

        return True
