from __future__ import annotations

from typing import Annotated

from fastapi import File, UploadFile
from pydantic import BaseModel, ConfigDict


class UploadImageRequest(BaseModel):
    """
    Upload request model.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    image: Annotated[UploadFile, File(...)]

    category: str


class UploadImageResponse(BaseModel):
    """
    Upload response model.
    """

    image_id: str

    filename: str

    content_type: str

    width: int

    height: int

    size_bytes: int