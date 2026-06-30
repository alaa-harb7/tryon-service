from __future__ import annotations

from tryon_service.application.upload.dto import (
    UploadImageCommand,
    UploadImageResult,
)
from tryon_service.application.workflows.upload_workflow import UploadWorkflow
from tryon_service.core.result import Result
from tryon_service.domain.entities.tryon_user_image import TryOnUserImage
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.repositories.image_repository import ImageRepository


class UploadUseCase:
    """
    Upload image business use case.
    """

    def __init__(
        self,
        workflow: UploadWorkflow,
        repository: ImageRepository,
    ) -> None:

        self._workflow = workflow
        self._repository = repository

    async def execute(
        self,
        command: UploadImageCommand,
    ) -> Result[UploadImageResult]:

        context = PipelineContext()

        context.request.user_id = command.user_id

        context.assets.user_image = command.image

        workflow_result = await self._workflow.execute(context)

        if not workflow_result.is_success:
            return Result.failure(
                workflow_result.error or "Workflow failed."
            )

        entity = TryOnUserImage(
            user_id=command.user_id,
            storage_path=str(command.image.path),
            filename=command.image.filename,
            content_type=command.image.content_type,
            width=command.image.width,
            height=command.image.height,
            size_bytes=command.image.size_bytes,
        )

        repository_result = await self._repository.create(entity)

        if not repository_result.is_success:
            return Result.failure(
                repository_result.error or "Database error."
            )

        return Result.success(
            UploadImageResult(
                image_id=entity.id,
                storage_path=entity.storage_path,
                filename=entity.filename,
                content_type=entity.content_type,
                width=entity.width,
                height=entity.height,
                size_bytes=entity.size_bytes,
            )
        )