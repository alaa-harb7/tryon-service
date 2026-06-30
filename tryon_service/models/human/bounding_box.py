from __future__ import annotations

from pydantic import BaseModel


class BoundingBox(BaseModel):
    """
    Bounding box of the detected human body.
    """

    left: float
    top: float
    right: float
    bottom: float

    @property
    def width(self) -> float:
        return self.right - self.left

    @property
    def height(self) -> float:
        return self.bottom - self.top

    @property
    def area(self) -> float:
        return self.width * self.height