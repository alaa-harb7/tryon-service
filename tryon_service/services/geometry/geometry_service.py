from __future__ import annotations

from math import atan2
from math import degrees
from math import hypot

from tryon_service.models.human.landmark import Landmark


class GeometryService:
    """
    Common geometric calculations used across
    validation and image analysis.
    """

    @staticmethod
    def distance(
        a: Landmark,
        b: Landmark,
    ) -> float:

        return hypot(
            b.x - a.x,
            b.y - a.y,
        )

    @staticmethod
    def midpoint(
        a: Landmark,
        b: Landmark,
    ) -> tuple[float, float]:

        return (
            (a.x + b.x) / 2,
            (a.y + b.y) / 2,
        )

    @staticmethod
    def horizontal_difference(
        a: Landmark,
        b: Landmark,
    ) -> float:

        return abs(
            a.y - b.y
        )

    @staticmethod
    def vertical_difference(
        a: Landmark,
        b: Landmark,
    ) -> float:

        return abs(
            a.x - b.x
        )

    @staticmethod
    def angle(
        a: Landmark,
        b: Landmark,
    ) -> float:

        return degrees(
            atan2(
                b.y - a.y,
                b.x - a.x,
            )
        )