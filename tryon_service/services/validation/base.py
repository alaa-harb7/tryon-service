from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext


class BaseValidator(ABC):
    """
    Base class for all validators.
    """

    @abstractmethod
    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:
        ...