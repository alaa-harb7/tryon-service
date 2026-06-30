from dataclasses import dataclass
from typing import Optional

from PIL import Image


@dataclass(slots=True)
class VirtualTryOnResult:
    image: Image.Image

    mask: Image.Image

    densepose: Image.Image

    schp_lip: Image.Image

    schp_atr: Image.Image