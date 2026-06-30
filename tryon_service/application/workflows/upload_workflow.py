from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.pipelines.base.executor import PipelineExecutor


class UploadWorkflow:
    """
    Executes the upload workflow.
    """

    def __init__(
        self,
        executor: PipelineExecutor,
    ) -> None:
        self._executor = executor

    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:
        return await self._executor.execute(context)