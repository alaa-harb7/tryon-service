from __future__ import annotations

from PIL import Image

from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)


class VirtualTryOnValidationError(Exception):
    pass


class VirtualTryOnValidator:

    VALID_TYPES = {
        "upper",
        "lower",
        "overall",
    }

    @classmethod
    def validate(
        cls,
        request: VirtualTryOnRequest,
    ) -> None:

        if not isinstance(request.person, Image.Image):
            raise VirtualTryOnValidationError(
                "person must be a PIL.Image.Image"
            )

        if not isinstance(request.garment, Image.Image):
            raise VirtualTryOnValidationError(
                "garment must be a PIL.Image.Image"
            )

        if request.garment_type not in cls.VALID_TYPES:
            raise VirtualTryOnValidationError(
                f"Unsupported garment type: {request.garment_type}"
            )

        if request.person.width == 0 or request.person.height == 0:
            raise VirtualTryOnValidationError(
                "Invalid person image."
            )

        if request.garment.width == 0 or request.garment.height == 0:
            raise VirtualTryOnValidationError(
                "Invalid garment image."
            )