from __future__ import annotations

from pydantic import BaseModel

from tryon_service.models.garment import GarmentData
from tryon_service.models.image import ImageData


class AssetsContext(BaseModel):
    user_image: ImageData | None = None
    garment_image: ImageData | None = None
    garment: GarmentData | None = None
    generated_image: ImageData | None = None