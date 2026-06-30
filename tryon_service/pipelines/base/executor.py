from __future__ import annotations

from collections.abc import Sequence

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.pipelines.base.pipeline import BasePipeline


class PipelineExecutor:
    """
    Executes pipeline stages sequentially.
    """

    def __init__(
        self,
        pipelines: Sequence[BasePipeline],
    ) -> None:
        self._pipelines = list(pipelines)

    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:

        current = context

        for pipeline in self._pipelines:

            result = await pipeline.execute(current)

            if not result.is_success:
                return Result.failure(result.error or "Pipeline execution failed.")

            current = result.value

            if current is None:
                return Result.failure("Pipeline returned no context.")

        return Result.success(current)