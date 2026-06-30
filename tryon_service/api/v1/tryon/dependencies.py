from __future__ import annotations

from tryon_service.container.container import (
    get_container,
)

from tryon_service.services.storage.local_storage_service import (
    LocalStorageService,
)

from tryon_service.services.tryon.virtual_tryon_service import (
    VirtualTryOnService,
)
from tryon_service.api.v1.tryon.builders.request_builder import (
    TryOnRequestBuilder,
)


def get_virtual_tryon_service() -> VirtualTryOnService:
    return get_container().virtual_tryon


def get_local_storage_service() -> LocalStorageService:
    return get_container().storage

def get_request_builder() -> TryOnRequestBuilder:
    return TryOnRequestBuilder()