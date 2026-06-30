from __future__ import annotations

from pathlib import Path

from fastapi import UploadFile

from tryon_service.models.image import ImageData


class UploadMapper:
    """
    Maps FastAPI UploadFile to ImageData.
    """

    @staticmethod
    def to_image_data(
        *,
        file: UploadFile,
        storage_path: Path,
        width: int,
        height: int,
        size_bytes: int,
    ) -> ImageData:

        return ImageData(
            path=storage_path,
            filename=file.filename or storage_path.name,
            content_type=file.content_type or "application/octet-stream",
            width=width,
            height=height,
            size_bytes=size_bytes,
        )