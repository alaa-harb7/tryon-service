from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.pipelines.base.executor import PipelineExecutor

from tryon_service.pipelines.upload.upload_pipeline import (
    UploadPipeline,
)

from tryon_service.pipelines.validation.validation_pipeline import (
    BasicValidationPipeline,
    PoseValidationPipeline,
)

from tryon_service.pipelines.human.human_analysis_pipeline import (
    HumanAnalysisPipeline,
)


class TryOnPipeline:
    """
    Main pipeline orchestrating all workflow stages.
    Execution order:
      1. UploadPipeline        — ensure image is present
      2. BasicValidationPipeline — file, format, resolution, blur, brightness
      3. HumanAnalysisPipeline   — MediaPipe pose + YOLO person detection
      4. PoseValidationPipeline  — pose, count, size, garment compatibility, etc.
    """

    def __init__(self) -> None:

        self._executor = PipelineExecutor(
            pipelines=[
                UploadPipeline(),
                BasicValidationPipeline(),
                HumanAnalysisPipeline(),
                PoseValidationPipeline(),
            ]
        )

    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:

        return await self._executor.execute(
            context
        )