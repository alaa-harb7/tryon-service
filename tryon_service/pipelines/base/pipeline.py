from __future__ import annotations

from abc import ABC, abstractmethod

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext


class BasePipeline(ABC):
    """
    Base class for all pipeline stages.
    """

    @abstractmethod
    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:
        """
        Execute pipeline stage.
        """
        raise NotImplementedError