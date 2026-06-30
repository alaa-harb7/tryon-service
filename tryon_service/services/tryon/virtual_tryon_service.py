from __future__ import annotations

from tryon_service.logging.logger import (
    get_logger,
)
from tryon_service.providers.pipeline.provider import (
    CatVTONPipelineProvider,
)
from tryon_service.services.masking.automask_service import (
    AutoMaskService,
)
from tryon_service.services.tryon.engine.virtual_tryon_engine import (
    VirtualTryOnEngine,
)
from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)
from tryon_service.services.tryon.result import (
    VirtualTryOnResult,
)
from tryon_service.pipelines.base.context import (
    PipelineContext,
)


from tryon_service.core.exceptions import (
    ValidationException,
)
from tryon_service.services.input_storage.temporary_image_storage import (
    TemporaryImageStorage,
)

from tryon_service.pipelines.human.human_analysis_pipeline import (
    HumanAnalysisPipeline,
)

from tryon_service.pipelines.validation.validation_pipeline import (
    BasicValidationPipeline,
    PoseValidationPipeline,
)


class VirtualTryOnService:
    """
    High-level orchestration service for Virtual Try-On.
    """

    def __init__(self) -> None:
        self._pipeline = CatVTONPipelineProvider()
        self._pipeline.load()

        self._mask = AutoMaskService()

        self._engine = VirtualTryOnEngine(
            pipeline=self._pipeline,
            mask_service=self._mask,
        )

        self._logger = get_logger(
            self.__class__.__name__,
        )
        self._temporary_storage = TemporaryImageStorage()

        self._human_pipeline = HumanAnalysisPipeline()

        self._basic_validation_pipeline = BasicValidationPipeline()
        self._pose_validation_pipeline = PoseValidationPipeline()

    async def generate(
        self,
        request: VirtualTryOnRequest,
    ) -> VirtualTryOnResult:
        
        self._logger.info(
            "Starting Virtual Try-On."
        )


        context = PipelineContext()

        context.request.garment_type = request.garment_type

        context.assets.user_image = (
            self._temporary_storage.save(
                request.person,
                "person",
            )
        )

        if request.garment is not None:

            context.assets.garment_image = (
                self._temporary_storage.save(
                    request.garment,
                    "garment",
                )
            )

        basic_validation_result = await self._basic_validation_pipeline.execute(
            context,
        )

        if not basic_validation_result.is_success:
            raise ValidationException(
                basic_validation_result.error,
                code=self._map_error_to_code(basic_validation_result.error)
            )

        human_result = await self._human_pipeline.execute(
            context,
        )

        if not human_result.is_success:
            raise ValidationException(
                human_result.error,
                code=self._map_error_to_code(human_result.error)
            )

        pose_validation_result = await self._pose_validation_pipeline.execute(
            context,
        )

        if not pose_validation_result.is_success:
            raise ValidationException(
                pose_validation_result.error,
                code=self._map_error_to_code(pose_validation_result.error)
            )


        result = self._engine.run(request)

        self._logger.info(
            "Virtual Try-On completed successfully."
        )

        return result

    def _map_error_to_code(self, error_msg: str | None) -> str:
        if not error_msg:
            return "VALIDATION_ERROR"
        msg = error_msg.lower()
        if "blurry" in msg:
            return "IMAGE_TOO_BLURRY"
        if "multiple people" in msg:
            return "MULTIPLE_PEOPLE_DETECTED"
        if "no person" in msg or "no body" in msg or "missing" in msg:
            return "NO_PERSON_DETECTED"
        if "format" in msg:
            return "UNSUPPORTED_FORMAT"
        if "resolution" in msg or "small" in msg or "width" in msg or "height" in msg:
            return "RESOLUTION_TOO_LOW"
        if "garment type" in msg:
            return "UNSUPPORTED_GARMENT_TYPE"
        if "upper body" in msg:
            return "BODY_NOT_COMPATIBLE"
        if "lower body" in msg:
            return "BODY_NOT_COMPATIBLE"
        if "full body" in msg:
            return "BODY_NOT_COMPATIBLE"
        if "feet" in msg:
            return "BODY_NOT_COMPATIBLE"
        if "facing" in msg:
            return "NOT_FACING_CAMERA"
        if "visibility" in msg or "landmark" in msg:
            return "LANDMARK_NOT_VISIBLE"
        if "level" in msg or "ankle" in msg:
            return "INVALID_POSE"
        if "garment" in msg:
            return "GARMENT_REQUIRED"
        return "VALIDATION_ERROR"