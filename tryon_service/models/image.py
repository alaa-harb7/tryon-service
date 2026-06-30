from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict


class ImageData(BaseModel):
    """
    Represents an image used throughout the TryOn pipeline.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=False,
    )

    path: Path
    filename: str
    content_type: str
    width: int
    height: int
    size_bytes: int