import pytest
from pathlib import Path

from tryon_service.models.image import ImageData
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.engine import ValidationEngine
from tryon_service.services.validation.validators.file_validator import (
    FileValidator,
)
from tryon_service.services.validation.validators.format_validator import (
    ImageFormatValidator,
)


@pytest.mark.asyncio
async def test_validation_engine_passes_valid_context():

    image = ImageData(
        path=Path(__file__),
        filename="test_validation_engine.py",
        content_type="image/jpeg",
        width=1200,
        height=1600,
        size_bytes=100,
    )

    context = PipelineContext()
    context.assets.user_image = image

    engine = ValidationEngine(
        validators=[
            FileValidator(),
            ImageFormatValidator(),
        ]
    )

    result = await engine.validate(context)

    assert result.is_success


@pytest.mark.asyncio
async def test_validation_engine_fails_missing_image():

    context = PipelineContext()
    # user_image intentionally left None

    engine = ValidationEngine(
        validators=[
            FileValidator(),
        ]
    )

    result = await engine.validate(context)

    assert not result.is_success
    assert "missing" in result.error.lower()