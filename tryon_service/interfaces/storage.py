from __future__ import annotations

from abc import ABC, abstractmethod

from tryon_service.core.result import Result
from tryon_service.models.image import ImageData


class StorageProvider(ABC):
    """
    Contract for image storage providers.
    """

    @abstractmethod
    async def save(
        self,
        image: ImageData,
    ) -> Result[ImageData]:
        """
        Save an image.

        Returns the stored image metadata.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(
        self,
        image: ImageData,
    ) -> Result[None]:
        """
        Delete an image.
        """
        raise NotImplementedError

    @abstractmethod
    async def exists(
        self,
        image: ImageData,
    ) -> bool:
        """
        Check if an image exists.
        """
        raise NotImplementedError