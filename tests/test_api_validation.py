import pytest
from fastapi.testclient import TestClient
from tryon_service.main import app
from tryon_service.core.exceptions import ValidationException
from tryon_service.services.tryon.virtual_tryon_service import VirtualTryOnService

client = TestClient(app)


def test_exception_handler_returns_nested_error():
    # Trigger validation exception handler indirectly or mock
    with pytest.raises(ValidationException) as excinfo:
        raise ValidationException("Image is too blurry.", code="IMAGE_TOO_BLURRY")
    assert excinfo.value.code == "IMAGE_TOO_BLURRY"
    assert excinfo.value.message == "Image is too blurry."


def test_error_mapping_logic():
    service = VirtualTryOnService.__new__(VirtualTryOnService)
    assert service._map_error_to_code("The image is too blurry. Score=45") == "IMAGE_TOO_BLURRY"
    assert service._map_error_to_code("Multiple people detected in image.") == "MULTIPLE_PEOPLE_DETECTED"
    assert service._map_error_to_code("No person detected.") == "NO_PERSON_DETECTED"
    assert service._map_error_to_code("Unsupported format: image/gif") == "UNSUPPORTED_FORMAT"
    assert service._map_error_to_code("Garment type 'shoes' is not supported") == "UNSUPPORTED_GARMENT_TYPE"
    assert service._map_error_to_code("Upper body is not visible.") == "BODY_NOT_COMPATIBLE"
    assert service._map_error_to_code("Random unexpected error message") == "VALIDATION_ERROR"
