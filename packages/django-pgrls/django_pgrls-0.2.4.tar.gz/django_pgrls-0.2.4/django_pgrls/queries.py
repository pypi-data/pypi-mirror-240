from collections.abc import AsyncIterator, Iterator

from django.db import models

from django_pgrls.state import bypass, get_current_tenant


class UnboundUsage(Exception):
    pass


class TenantBoundQueryset(models.QuerySet):
    def _is_unbound(self) -> bool:
        return get_current_tenant() is None

    def _fetch_all(self) -> None:
        if self._is_unbound():
            raise UnboundUsage

        super()._fetch_all()

    def count(self) -> int:
        if self._is_unbound():
            raise UnboundUsage

        return super().count()

    def iterator(self, chunk_size: int = 2000) -> Iterator:
        if self._is_unbound():
            raise UnboundUsage

        return super().iterator(chunk_size)

    async def aiterator(self, chunk_size: int = 2000) -> AsyncIterator:
        if self._is_unbound():
            raise UnboundUsage

        async for item in super().aiterator(chunk_size):
            yield item

    def exists(self) -> bool:
        if self._is_unbound():
            raise UnboundUsage

        return super().exists()


class TenantBypassQueryset(models.QuerySet):
    def _fetch_all(self) -> None:
        with bypass():
            super()._fetch_all()

    def count(self) -> int:
        with bypass():
            return super().count()

    def iterator(self, chunk_size: int = 2000) -> Iterator:
        with bypass():
            yield from super().iterator(chunk_size)

    async def aiterator(self, chunk_size: int = 2000) -> AsyncIterator:
        with bypass():
            async for item in super().aiterator(chunk_size):
                yield item

    def exists(self) -> bool:
        with bypass():
            return super().exists()

    def create(self, **kwargs: object) -> models.Model:
        with bypass():
            return super().create(**kwargs)
