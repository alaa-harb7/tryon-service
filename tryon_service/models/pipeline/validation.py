from __future__ import annotations

from pydantic import BaseModel, Field


class ValidationContext(BaseModel):
    passed: bool = False
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)