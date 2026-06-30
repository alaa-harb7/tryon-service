from pathlib import Path

from PIL import Image

from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)
from tryon_service.services.tryon.virtual_tryon_service import (
    VirtualTryOnService,
)

service = VirtualTryOnService()

request = VirtualTryOnRequest(
    person=Image.open("scripts/images/person.jpg"),
    garment=Image.open("scripts/images/garment.jpg"),
    garment_type="upper",
)

result = service.generate(request)

output = Path("scripts/output")
output.mkdir(exist_ok=True)

result.image.save(output / "tryon.png")
result.mask.save(output / "mask.png")
result.densepose.save(output / "densepose.png")
result.schp_lip.save(output / "schp_lip.png")
result.schp_atr.save(output / "schp_atr.png")

print("Virtual Try-On Finished Successfully.")