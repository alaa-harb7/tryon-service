from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel

from tryon_service.models.image import ImageData


class UploadImageCommand(BaseModel):
    """
    Command sent to UploadUseCase.
    """

    user_id: str

    image: ImageData


class UploadImageResult(BaseModel):
    """
    Upload result returned by UploadUseCase.
    """

    image_id: str

    storage_path: str

    filename: str

    content_type: str

    width: int

    height: int

    size_bytes: int