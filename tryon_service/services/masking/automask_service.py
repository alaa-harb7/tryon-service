from __future__ import annotations

from PIL import Image

from tryon_service.providers.masking.provider import AutoMaskerProvider


class AutoMaskService:
    """
    High-level service for Cloth Agnostic Mask generation.
    """

    def __init__(self) -> None:
        self._provider = AutoMaskerProvider()
        self._provider.load()

    def generate(
        self,
        image: Image.Image,
        mask_type: str = "upper",
    ) -> dict:

        return self._provider.masker(
            image=image,
            mask_type=mask_type,
        )