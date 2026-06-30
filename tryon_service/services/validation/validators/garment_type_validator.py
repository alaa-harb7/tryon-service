from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator

# Dynamically supported garment types from active engine configuration.
# This keeps engine limitations decoupled from code logic.
SUPPORTED_TYPES = {"upper", "lower", "overall"}


class GarmentTypeValidator(BaseValidator):
    """
    Validates that the requested garment type is supported by the active try-on engine.
    """

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        garment_type = context.request.garment_type

        if garment_type not in SUPPORTED_TYPES:
            return Result.failure(
                f"Unsupported garment type: '{garment_type}'. "
                f"Supported: {sorted(list(SUPPORTED_TYPES))}"
            )

        return Result.success(None)
