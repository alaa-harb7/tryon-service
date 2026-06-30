from tryon_service.schemas.upload import UploadImageResponse


def test_upload_response() -> None:
    response = UploadImageResponse(
        image_id="123",
        filename="shirt.png",
        content_type="image/png",
        width=1000,
        height=1200,
        size_bytes=500000,
    )

    assert response.image_id == "123"