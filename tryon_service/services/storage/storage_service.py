from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from PIL import Image


class StorageService(ABC):
    """
    Abstract interface for storing generated images.
    """

    @abstractmethod
    def save(
        self,
        image: Image.Image,
    ) -> str:
        """
        Saves the image and returns its public URL.
        """
        raise NotImplementedError