from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


class ValidationEngine:

    def __init__(
        self,
        validators: list[BaseValidator],
    ) -> None:
        self._validators = validators

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        for validator in self._validators:

            result = await validator.validate(context)

            if not result.is_success:
                return result

        return Result.success(None)