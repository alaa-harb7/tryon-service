from __future__ import annotations

from pydantic import BaseModel

from tryon_service.models.image import ImageData


class ResultContext(BaseModel):
    success: bool = False
    image: ImageData | None = None
    message: str | None = None
    quality_score: float | None = None