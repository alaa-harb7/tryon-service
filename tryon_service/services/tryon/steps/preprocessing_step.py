from __future__ import annotations

from PIL import Image

from tryon_service.services.downloader.image_downloader import (
    ImageDownloader,
)
from tryon_service.services.preprocessing.image_preprocessor import (
    ImagePreprocessor,
)
from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)


class PreprocessingStep:

    def __init__(
        self,
        downloader: ImageDownloader,
    ) -> None:
        self._downloader = downloader

    def execute(
        self,
        request: VirtualTryOnRequest,
    ) -> tuple[Image.Image, Image.Image]:

        person = ImagePreprocessor.preprocess_person(
            request.person,
        )

        if request.garment is not None:

            garment = request.garment

        elif request.garment_url:

            garment = self._downloader.download(
                request.garment_url,
            )

        else:

            raise ValueError(
                "Either garment or garment_url must be provided."
            )

        garment = ImagePreprocessor.preprocess_garment(
            garment,
        )

        return person, garment