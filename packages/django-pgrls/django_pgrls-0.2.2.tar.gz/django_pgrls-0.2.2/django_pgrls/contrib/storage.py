import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django_pgrls.state import get_current_tenant


class TenantFileSystemStorage(FileSystemStorage):
    """
    Tenant aware file system storage.
    Appends the tenant identifier to the base location and base URL.
    """

    def get_path_identifier(self) -> str:
        tenant = get_current_tenant()

        if tenant is None:
            return ""

        if hasattr(tenant, "storage_pathname"):
            return tenant.storage_pathname()

        if hasattr(settings, "PGRLS_PATHNAME_FUNCTION"):
            return settings.PGRLS_PATHNAME_FUNCTION(tenant)

        return str(tenant.pk)

    @property  # To avoid caching of tenant
    def base_location(self) -> str:
        """
        Appends base location with the tenant path identifier.
        """
        file_folder = self.get_path_identifier()
        location = os.path.join(super().base_location, file_folder)

        if not location.endswith("/"):
            location += "/"

        return location

    @property  # To avoid caching of tenant
    def location(self) -> str:
        return super().location

    @property  # To avoid caching of tenant
    def base_url(self) -> str:
        """
        Optionally appends base URL with the tenant path identifier.
        If the current tenant is already using a folder, no path identifier is
        appended.
        """
        tenant = get_current_tenant()
        url_folder = self.get_path_identifier()

        # This case corresponds to folder routing
        if url_folder and tenant and getattr(tenant, "folder", None):
            # Since we're already prepending all URLs with tenant, there is no
            # need to make the differentiation here
            url_folder = ""

        parent_base_url = super().base_url.strip("/")
        url = "/".join(["", parent_base_url, url_folder])

        if not url.endswith("/"):
            url += "/"

        return url
