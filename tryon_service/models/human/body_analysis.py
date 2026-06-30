from __future__ import annotations

from pydantic import BaseModel


class BodyAnalysis(BaseModel):
    """
    High-level analysis of the detected body.
    """

    shoulder_angle: float

    hip_angle: float

    body_center_x: float

    body_center_y: float

    body_area: float