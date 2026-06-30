import pytest

from tryon_service.core.exceptions import ValidationException


def test_validation_exception() -> None:
    with pytest.raises(ValidationException):
        raise ValidationException("Invalid image.")