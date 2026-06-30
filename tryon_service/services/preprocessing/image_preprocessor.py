from __future__ import annotations

from PIL import Image, ImageOps
from tryon_service.config.tryon import TryOnConfig


class ImagePreprocessor:
    """
    Shared preprocessing for all Virtual Try-On models.
    """

    PERSON_SIZE = (
        TryOnConfig.PERSON_WIDTH,
        TryOnConfig.PERSON_HEIGHT,
    )

    GARMENT_SIZE = (
        TryOnConfig.GARMENT_WIDTH,
        TryOnConfig.GARMENT_HEIGHT,
    )

    @classmethod
    def preprocess_person(
        cls,
        image: Image.Image,
    ) -> Image.Image:

        image = ImageOps.exif_transpose(image)

        image = image.convert("RGB")

        image = image.resize(
            cls.PERSON_SIZE,
            Image.Resampling.LANCZOS,
        )

        return image

    @classmethod
    def preprocess_garment(
        cls,
        image: Image.Image,
    ) -> Image.Image:

        image = ImageOps.exif_transpose(image)

        image = image.convert("RGB")

        image = image.resize(
            cls.GARMENT_SIZE,
            Image.Resampling.LANCZOS,
        )

        return image