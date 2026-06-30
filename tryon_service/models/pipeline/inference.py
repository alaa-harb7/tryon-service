from __future__ import annotations

from pydantic import BaseModel


class InferenceContext(BaseModel):
    provider: str | None = None
    model: str | None = None
    attempts: int = 0