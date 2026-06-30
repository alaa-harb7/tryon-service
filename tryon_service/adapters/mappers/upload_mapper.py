from __future__ import annotations

from pathlib import Path

from fastapi import UploadFile

from tryon_service.models.image import ImageData


class UploadMapper:
    """
    Maps FastAPI UploadFile into the internal ImageData model.
    """

    @staticmethod
    async def to_image_data(file: UploadFile) -> ImageData:
        contents = await file.read()

        return ImageData(
            path=Path(file.filename),
            filename=file.filename,
            content_type=file.content_type or "application/octet-stream",
            width=0,
            height=0,
            size_bytes=len(contents),
        )