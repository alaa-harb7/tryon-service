from __future__ import annotations

from tryon_service.providers.pipeline.provider import (
    CatVTONPipelineProvider,
)
from tryon_service.services.masking.automask_service import (
    AutoMaskService,
)
from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)
from tryon_service.services.tryon.result import (
    VirtualTryOnResult,
)

from tryon_service.services.tryon.steps.preprocessing_step import (
    PreprocessingStep,
)
from tryon_service.services.tryon.steps.mask_generation_step import (
    MaskGenerationStep,
)
from tryon_service.services.tryon.steps.inference_step import (
    InferenceStep,
)
from tryon_service.services.tryon.steps.postprocessing_step import (
    PostprocessingStep,
)
from tryon_service.services.downloader.image_downloader import (
    ImageDownloader,
)
from tryon_service.pipelines.base.context import (
    PipelineContext,
)


class VirtualTryOnEngine:
    """
    Executes the complete Virtual Try-On pipeline.
    """

    def __init__(
        self,
        pipeline: CatVTONPipelineProvider,
        mask_service: AutoMaskService,
    ) -> None:

        self._downloader = ImageDownloader()

        self._preprocessing = PreprocessingStep(
            downloader=self._downloader,
        )

        self._masking = MaskGenerationStep(mask_service)

        self._inference = InferenceStep(pipeline)

        self._postprocessing = PostprocessingStep()

        self._context = PipelineContext()

    def run(
        self,
        request: VirtualTryOnRequest,
    ) -> VirtualTryOnResult:

        person, garment = self._preprocessing.execute(request)
        
        self._context.request.garment_type = request.garment_type

        mask_result = self._masking.execute(
            person,
            request.garment_type,
        )

        pipeline_result = self._inference.execute(
            person,
            garment,
            mask_result["mask"],
        )

        return self._postprocessing.execute(
            pipeline_result,
            mask_result,
        )