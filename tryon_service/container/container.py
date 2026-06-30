from __future__ import annotations

from functools import lru_cache

from tryon_service.services.storage.local_storage_service import (
    LocalStorageService,
)
from tryon_service.services.tryon.virtual_tryon_service import (
    VirtualTryOnService,
)


class Container:

    def __init__(self) -> None:
        self.virtual_tryon = VirtualTryOnService()

        self.storage = LocalStorageService()


@lru_cache
def get_container() -> Container:
    return Container()