from PIL import Image

from tryon_service.services.masking.automask_service import (
    AutoMaskService,
)


def test_service_creation():

    service = AutoMaskService()

    assert service is not None


def test_generate():

    image = Image.open("scripts/images/person.jpg")

    service = AutoMaskService()

    result = service.generate(image)

    assert "mask" in result
    assert "densepose" in result
    assert "schp_lip" in result
    assert "schp_atr" in result