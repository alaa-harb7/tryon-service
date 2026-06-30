from pathlib import Path

from tryon_service.models.image import ImageData


def test_image_model() -> None:
    image = ImageData(
        path=Path("uploads/image.jpg"),
        filename="image.jpg",
        content_type="image/jpeg",
        width=1024,
        height=1024,
        size_bytes=100000,
    )

    assert image.filename == "image.jpg"
    assert image.width == 1024
    assert image.height == 1024
    