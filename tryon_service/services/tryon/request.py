from dataclasses import dataclass
from PIL import Image


from typing import Optional

@dataclass(slots=True)
class VirtualTryOnRequest:
    person: Image.Image
    garment_type: str
    garment: Optional[Image.Image] = None
    garment_url: Optional[str] = None