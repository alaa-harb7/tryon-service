import pytest

from tryon_service.services.tryon.virtual_tryon_service import (
    VirtualTryOnService,
)


@pytest.mark.skip(
    reason=(
        "Integration test: VirtualTryOnService requires the FastAPI lifespan "
        "to have run first so that MediaPipe and CatVTON models are loaded "
        "into the container. Run this test against a live application instance."
    )
)
def test_service_creation():

    service = VirtualTryOnService()

    assert service is not None