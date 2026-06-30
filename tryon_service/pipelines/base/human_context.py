from __future__ import annotations

from pydantic import BaseModel

from tryon_service.models.human.body_analysis import BodyAnalysis
from tryon_service.models.human.pose import HumanPose
from tryon_service.models.person.result import (
    PersonDetectionResult,
)


class HumanContext(BaseModel):
    """
    Human analysis shared across the pipeline.
    """

    pose: HumanPose | None = None

    analysis: BodyAnalysis | None = None

    person_count: int = 0

    full_body: bool = False

    upper_body_visible: bool = False

    lower_body_visible: bool = False

    person_detection: PersonDetectionResult | None = None

    feet_visible: bool = False

    face_visible: bool = False

    occluded: bool = False