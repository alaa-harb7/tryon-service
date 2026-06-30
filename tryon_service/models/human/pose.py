from __future__ import annotations

from pydantic import BaseModel, Field

from tryon_service.models.human.bounding_box import BoundingBox
from tryon_service.models.human.landmark import Landmark


class HumanPose(BaseModel):
    """
    Human pose extracted from the vision engine.
    """

    detected: bool = False

    landmarks: list[Landmark] = Field(default_factory=list)

    bounding_box: BoundingBox | None = None

    def landmark(
        self,
        index: int,
    ) -> Landmark:
        return self.landmarks[index]