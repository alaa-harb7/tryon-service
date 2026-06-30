from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GarmentData(BaseModel):
    """
    Represents a garment used by the Try-On pipeline.
    """

    model_config = ConfigDict(
        frozen=False,
    )

    product_id: str

    category: str

    image_path: str

    brand: str | None = None

    color: str | None = None