from __future__ import annotations

from pydantic import BaseModel


class Landmark(BaseModel):
    """
    Single body landmark.
    """

    x: float
    y: float
    z: float
    visibility: float