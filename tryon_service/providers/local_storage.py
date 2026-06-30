from __future__ import annotations

from pathlib import Path

from tryon_service.core.result import Result
from tryon_service.interfaces.storage import StorageProvider
from tryon_service.models.image import ImageData


class LocalStorageProvider(StorageProvider):
    """
    Local filesystem storage provider.
    """

    async def save(
        self,
        image: ImageData,
    ) -> Result[ImageData]:

        destination = Path("uploads") / image.filename

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination.write_bytes(image.path.read_bytes())

        stored_image = image.model_copy(
            update={
                "path": destination,
            }
        )

        return Result.success(stored_image)

    async def delete(
        self,
        image: ImageData,
    ) -> Result[None]:

        if image.path.exists():
            image.path.unlink()

        return Result.success(None)

    async def exists(
        self,
        image: ImageData,
    ) -> bool:

        return image.path.exists()