from pathlib import Path
from PIL import Image

from tryon_service.providers.masking.provider import AutoMaskerProvider

provider = AutoMaskerProvider()
provider.load()

image = Image.open("scripts/images/person.jpg")

result = provider.masker(
    image=image,
    mask_type="upper",
)

output_dir = Path("scripts/output")
output_dir.mkdir(exist_ok=True)

result["mask"].save(output_dir / "mask.png")
result["densepose"].save(output_dir / "densepose.png")
result["schp_lip"].save(output_dir / "schp_lip.png")
result["schp_atr"].save(output_dir / "schp_atr.png")

print("Done.")