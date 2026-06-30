from __future__ import annotations

from pydantic import BaseModel


class PersonDetection(BaseModel):
    """
    Represents one detected person.
    """

    x1: float

    y1: float

    x2: float

    y2: float

    confidence: float

    @property
    def width(self) -> float:
        return self.x2 - self.x1


    @property
    def height(self) -> float:
        return self.y2 - self.y1


    @property
    def area(self) -> float:
        return self.width * self.height


    @property
    def center_x(self) -> float:
        return (self.x1 + self.x2) / 2


    @property
    def center_y(self) -> float:
        return (self.y1 + self.y2) / 2