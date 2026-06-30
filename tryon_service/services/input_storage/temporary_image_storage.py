from __future__ import annotations

import uuid
from pathlib import Path

from PIL import Image

from tryon_service.models.image import ImageData


class TemporaryImageStorage:
    """
    Saves uploaded images temporarily so they
    can be consumed by the analysis pipeline.
    """

    def __init__(
        self,
        directory: str = "temp",
    ) -> None:

        self._directory = Path(directory)

        self._directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        image: Image.Image,
        prefix: str,
    ) -> ImageData:

        filename = (
            f"{prefix}_{uuid.uuid4().hex}.png"
        )

        path = self._directory / filename

        image.save(path)

        width, height = image.size

        return ImageData(
            path=path,
            filename=filename,
            content_type="image/png",
            width=width,
            height=height,
            size_bytes=path.stat().st_size,
        )