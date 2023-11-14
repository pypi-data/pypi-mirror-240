import re
from typing import Callable, TypeAlias

from asgiref.sync import iscoroutinefunction, sync_to_async
from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import clear_url_caches
from django.utils.decorators import sync_and_async_middleware

from django_pgrls.models import TenantModel
from django_pgrls.routing.info import DomainInfo, HeadersInfo, SessionInfo
from django_pgrls.routing.models import get_primary_domain_for_tenant
from django_pgrls.routing.urlresolvers import get_dynamic_tenant_prefixed_urlconf
from django_pgrls.settings import get_tenant_header, get_tenant_session_key
from django_pgrls.state import activate
from django_pgrls.utils import (
    get_domain_model,
    get_tenant_fk_field_name,
    get_tenant_model,
)


def remove_www(path: str) -> str:
    if path.startswith("www."):
        return path[4:]
    return path


def strip_tenant_from_path(path: str, prefix: str) -> str:
    if not prefix:
        return path
    return re.sub(r"^/{}/".format(prefix), "/", path)


ResponseHandler: TypeAlias = Callable[[HttpRequest], HttpResponse]


def route_domain(request: HttpRequest) -> HttpResponse | None:
    hostname = remove_www(request.get_host().split(":")[0])

    tenant: TenantModel

    ActualDomainModel = get_domain_model()
    prefix = request.path.split("/")[1]
    domain = None

    try:
        domain = ActualDomainModel._default_manager.select_related(get_tenant_fk_field_name()).get(
            domain=hostname, folder=prefix
        )
    except ActualDomainModel.DoesNotExist:
        try:
            domain = ActualDomainModel._default_manager.select_related(
                get_tenant_fk_field_name()
            ).get(domain=hostname, folder="")
        except ActualDomainModel.DoesNotExist:
            pass

    if domain is None:
        raise Http404("No tenant for hostname '%s'" % hostname)

    tenant = domain.get_tenant()
    tenant.routing = DomainInfo(domain=hostname, folder=None)

    if prefix and domain.folder == prefix:
        tenant.routing = DomainInfo(domain=hostname, folder=prefix)
        clear_url_caches()  # Required to remove previous tenant prefix from cache
        dynamic_path = settings.ROOT_URLCONF + "_dynamically_tenant_prefixed"
        request.urlconf = get_dynamic_tenant_prefixed_urlconf(settings.ROOT_URLCONF, dynamic_path)

    if domain.redirect_to_primary:
        primary_domain = get_primary_domain_for_tenant(tenant)
        if primary_domain:
            path = strip_tenant_from_path(request.path, prefix)
            return redirect(primary_domain.absolute_url(path), permanent=True)

    request.tenant = tenant
    activate(tenant)

    return None


def route_session(request: HttpRequest) -> HttpResponse | None:
    tenant_session_key = get_tenant_session_key()

    if hasattr(request, "session"):
        tenant_id = request.session.get(tenant_session_key)

        if tenant_id is not None:
            ActualTenantModel = get_tenant_model()
            tenant = ActualTenantModel.objects.get(pk=tenant_id)
            tenant.routing = SessionInfo()
            request.tenant = tenant
            activate(tenant)

    return None


def route_headers(request: HttpRequest) -> HttpResponse | None:
    tenant_header = get_tenant_header()

    tenant_id = request.headers.get(tenant_header)

    if tenant_id is not None:
        ActualTenantModel = get_tenant_model()
        tenant = ActualTenantModel.objects.get(pk=tenant_id)
        tenant.routing = HeadersInfo()
        request.tenant = tenant
        activate(tenant)

    return None


def middleware_factory(
    handler: Callable[[HttpRequest], HttpResponse | None]
) -> Callable[[ResponseHandler], ResponseHandler]:
    @sync_and_async_middleware
    def middleware(get_response: ResponseHandler) -> ResponseHandler:
        if iscoroutinefunction(get_response):
            async_base_middleware = sync_to_async(handler)

            async def sync_middleware(request: HttpRequest) -> HttpResponse | None:
                if response := await async_base_middleware(request):
                    return response

                return await get_response(request)

            return sync_middleware

        else:

            def async_middleware(request: HttpRequest) -> HttpResponse | None:
                if response := handler(request):
                    return response

                return get_response(request)

            return async_middleware

    return middleware


DomainRoutingMiddleware = middleware_factory(route_domain)
SessionRoutingMiddleware = middleware_factory(route_session)
HeadersRoutingMiddleware = middleware_factory(route_headers)
