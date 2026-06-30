from __future__ import annotations

from pydantic import BaseModel

from tryon_service.models.person.detection import (
    PersonDetection,
)


class PersonDetectionResult(BaseModel):
    """
    Result returned from the person detector.
    """

    detections: list[PersonDetection]

    @property
    def person_count(
        self,
    ) -> int:

        return len(self.detections)
    
    @property
    def main_person(self) -> PersonDetection | None:

        if not self.detections:
            return None

        return max(
            self.detections,
            key=lambda detection: detection.area,
        )