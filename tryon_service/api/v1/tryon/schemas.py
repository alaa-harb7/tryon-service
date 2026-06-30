from __future__ import annotations

from pydantic import BaseModel


class TryOnResponse(BaseModel):
    success: bool
    image_url: str