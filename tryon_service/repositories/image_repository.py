from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.core.container import container
from tryon_service.domain.entities.tryon_user_image import TryOnUserImage


class ImageRepository:
    """
    Repository responsible for persisting user images.
    """

    def __init__(self) -> None:
        self._collection = container.collections.tryon_user_images

    async def create(
        self,
        entity: TryOnUserImage,
    ) -> Result[TryOnUserImage]:

        document = entity.model_dump(mode="json")

        await self._collection.insert_one(document)

        return Result.success(entity)