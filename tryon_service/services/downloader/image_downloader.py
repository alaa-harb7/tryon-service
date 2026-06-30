from __future__ import annotations

from io import BytesIO

import requests

from PIL import Image


class ImageDownloader:
    """
    Downloads an image and returns a PIL Image.
    """

    def download(
        self,
        url: str,
    ) -> Image.Image:

        response = requests.get(
            url,
            timeout=30,
        )

        response.raise_for_status()

        return Image.open(
            BytesIO(response.content)
        ).convert("RGB")