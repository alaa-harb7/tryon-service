from __future__ import annotations

from io import BytesIO

import cloudinary
import cloudinary.uploader

from PIL import Image

from tryon_service.config.settings import settings


class CloudinaryStorageService:
    """
    Upload generated images to Cloudinary.
    """

    def __init__(self) -> None:

        cloudinary.config(
            cloud_name=settings._get_env("CLOUDINARY_CLOUD_NAME"),
            api_key=settings._get_env("CLOUDINARY_API_KEY"),
            api_secret=settings._get_env("CLOUDINARY_API_SECRET"),
            secure=True,
        )

        self._folder = settings.cloudinary["folder"]

    def save(
        self,
        image: Image.Image,
        filename: str,
    ) -> str:

        buffer = BytesIO()

        image.save(
            buffer,
            format="PNG",
        )

        buffer.seek(0)

        result = cloudinary.uploader.upload(
            buffer,
            folder=self._folder,
            public_id=filename,
            overwrite=True,
            resource_type="image",
        )

        return result["secure_url"]