from __future__ import annotations

from pydantic import BaseModel, Field


class AnalysisContext(BaseModel):
    pose: dict = Field(default_factory=dict)
    segmentation: dict = Field(default_factory=dict)
    human_parsing: dict = Field(default_factory=dict)
    landmarks: dict = Field(default_factory=dict)