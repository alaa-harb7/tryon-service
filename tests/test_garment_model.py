from tryon_service.models.garment import GarmentData


def test_garment_model() -> None:
    garment = GarmentData(
        product_id="123",
        category="hoodie",
        image_path="products/hoodie.png",
    )

    assert garment.product_id == "123"
    assert garment.category == "hoodie"