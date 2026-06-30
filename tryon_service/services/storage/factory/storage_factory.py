from __future__ import annotations

from tryon_service.config.settings import settings

from tryon_service.services.storage.local_storage_service import (
    LocalStorageService,
)
from tryon_service.services.storage.cloudinary.cloudinary_storage_service import (
    CloudinaryStorageService,
)


class StorageFactory:

    @staticmethod
    def create():

        provider = settings.storage["provider"]

        if provider == "local":
            return LocalStorageService()

        if provider == "cloudinary":
            return CloudinaryStorageService()

        raise ValueError(
            f"Unknown storage provider: {provider}"
        )