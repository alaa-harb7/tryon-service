from __future__ import annotations

from io import BytesIO

from PIL import Image

from fastapi import HTTPException
from fastapi import UploadFile

from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)


class TryOnRequestBuilder:

    async def build(
        self,
        person: UploadFile,
        garment: UploadFile | None,
        garment_url: str | None,
        garment_type: str,
    ) -> VirtualTryOnRequest:

        try:

            person_image = Image.open(
                BytesIO(await person.read())
            ).convert("RGB")

        except Exception as exc:

            raise HTTPException(
                status_code=400,
                detail="Invalid person image.",
            ) from exc

        garment_image = None

        if garment is not None:

            try:

                garment_image = Image.open(
                    BytesIO(await garment.read())
                ).convert("RGB")

            except Exception as exc:

                raise HTTPException(
                    status_code=400,
                    detail="Invalid garment image.",
                ) from exc

        # Validation: one of them must be present
        if garment_image is None and not garment_url:
            raise HTTPException(
                status_code=400,
                detail="Garment image or garment_url must be provided.",
            )

        return VirtualTryOnRequest(
            person=person_image,
            garment=garment_image,
            garment_url=garment_url,
            garment_type=garment_type,
        )