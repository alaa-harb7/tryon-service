from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.pipelines.base.pipeline import BasePipeline
from tryon_service.services.validation.engine import ValidationEngine

# Basic validators
from tryon_service.services.validation.validators.garment_type_validator import (
    GarmentTypeValidator,
)
from tryon_service.services.validation.validators.file_validator import (
    FileValidator,
)
from tryon_service.services.validation.validators.format_validator import (
    ImageFormatValidator,
)
from tryon_service.services.validation.validators.resolution_validator import (
    ResolutionValidator,
)
from tryon_service.services.validation.validators.blur_validator import (
    BlurValidator,
)
from tryon_service.services.validation.validators.brightness_validator import (
    BrightnessValidator,
)

# Pose/Body validators
from tryon_service.services.validation.validators.pose_validator import (
    PoseValidator,
)
from tryon_service.services.validation.validators.single_person_validator import (
    SinglePersonValidator,
)
from tryon_service.services.validation.validators.person_size_validator import (
    PersonSizeValidator,
)
from tryon_service.services.validation.validators.garment_compatibility_validator import (
    GarmentCompatibilityValidator,
)
from tryon_service.services.validation.validators.body_coverage_validator import (
    BodyCoverageValidator,
)
from tryon_service.services.validation.validators.facing_camera_validator import (
    FacingCameraValidator,
)
# from tryon_service.services.validation.validators.landmark_visibility_validator import (
#     LandmarkVisibilityValidator,
# )
from tryon_service.services.validation.validators.standing_pose_validator import (
    StandingPoseValidator,
)


class BasicValidationPipeline(BasePipeline):
    """
    Executes basic image metadata and quality validators.
    """

    def __init__(self) -> None:
        self._engine = ValidationEngine(
            validators=[
                GarmentTypeValidator(),
                FileValidator(),
                ImageFormatValidator(),
                ResolutionValidator(),
                BlurValidator(),
                BrightnessValidator(),
            ]
        )


    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:

        result = await self._engine.validate(context)

        if not result.is_success:
            return Result.failure(result.error)

        return Result.success(context)


class PoseValidationPipeline(BasePipeline):
    """
    Executes validation related to human body pose, landmarks, and count.
    """

    def __init__(self) -> None:
        self._engine = ValidationEngine(
            validators=[
                PoseValidator(),
                SinglePersonValidator(),
                PersonSizeValidator(),
                GarmentCompatibilityValidator(),
                BodyCoverageValidator(),
                FacingCameraValidator(),
                # LandmarkVisibilityValidator(),
                StandingPoseValidator(),
            ]
        )

    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:

        result = await self._engine.validate(context)

        if not result.is_success:
            return Result.failure(result.error)

        return Result.success(context)