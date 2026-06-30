from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.pipelines.base.pipeline import BasePipeline
from tryon_service.services.body.body_analysis_service import BodyAnalysisService
from tryon_service.services.human.mediapipe_service import MediaPipeService
from tryon_service.services.human.visibility_service import VisibilityService

from tryon_service.providers.person.provider import (
    PersonDetectionProvider,
)

from tryon_service.services.person.person_detection_service import (
    PersonDetectionService,
)

import cv2


class HumanAnalysisPipeline(BasePipeline):

    def __init__(self) -> None:
        self._service = MediaPipeService()

        self._person_provider = PersonDetectionProvider()
        self._person_provider.load()

        self._person_detector = PersonDetectionService(
            self._person_provider,
        )

    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:

        image = context.assets.user_image

        if image is None:
            return Result.failure(
                "User image is missing."
            )

        pose = self._service.detect(
            str(image.path)
        )
        context.human.pose = pose

        if pose.detected:
            context.human.analysis = (
                BodyAnalysisService.analyze(
                    pose
                )
            )
            context.human.full_body = VisibilityService.is_full_body(pose)
            context.human.upper_body_visible = VisibilityService.is_upper_body_visible(pose)
            context.human.lower_body_visible = VisibilityService.is_lower_body_visible(pose)
            context.human.feet_visible = VisibilityService.are_feet_visible(pose)
            context.human.face_visible = VisibilityService.is_face_visible(pose)
        else:
            context.human.full_body = False
            context.human.upper_body_visible = False
            context.human.lower_body_visible = False
            context.human.feet_visible = False
            context.human.face_visible = False

        opencv_image = cv2.imread(
            str(image.path),
        )

        detection_result = self._person_detector.detect(
            opencv_image,
        )

        context.human.person_detection = detection_result

        context.human.person_count = (
            detection_result.person_count
        )

        return Result.success(context)