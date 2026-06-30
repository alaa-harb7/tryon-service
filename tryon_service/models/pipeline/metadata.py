from __future__ import annotations

from pydantic import BaseModel, Field


class MetadataContext(BaseModel):
    execution_time_ms: float = 0.0
    worker: str | None = None
    gpu: str | None = None
    custom: dict = Field(default_factory=dict)