from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


class PoseValidator(BaseValidator):
    """
    Validates that a human pose is available.
    """

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        pose = context.human.pose

        if pose is None:
            return Result.failure(
                "Human pose is missing."
            )

        if not pose.detected:
            return Result.failure(
                "No human pose detected."
            )

        return Result.success(None)