from __future__ import annotations

from PIL import Image

from tryon_service.services.masking.automask_service import (
    AutoMaskService,
)


class MaskGenerationStep:

    def __init__(
        self,
        mask_service: AutoMaskService,
    ) -> None:

        self._mask = mask_service

    def execute(
        self,
        person: Image.Image,
        garment_type: str,
    ):

        return self._mask.generate(
            image=person,
            mask_type=garment_type,
        )