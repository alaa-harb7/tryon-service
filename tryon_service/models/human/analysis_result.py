from __future__ import annotations

from dataclasses import dataclass

from tryon_service.models.human.body_analysis import BodyAnalysis
from tryon_service.models.human.pose import HumanPose


@dataclass(slots=True)
class HumanAnalysisResult:

    person_count: int

    pose: HumanPose | None

    body_analysis: BodyAnalysis | None

    blur_score: float

    brightness: float

    full_body: bool

    upper_body_visible: bool

    lower_body_visible: bool

    feet_visible: bool