from __future__ import annotations

from tryon_service.application.upload.use_case import UploadUseCase
from tryon_service.application.workflows.upload_workflow import UploadWorkflow
from tryon_service.pipelines.base.executor import PipelineExecutor
from tryon_service.pipelines.upload.upload_pipeline import UploadPipeline
from tryon_service.repositories.image_repository import ImageRepository


def get_upload_use_case() -> UploadUseCase:
    """
    Build UploadUseCase with all required dependencies.
    """

    executor = PipelineExecutor(
        pipelines=[
            UploadPipeline(),
        ]
    )

    workflow = UploadWorkflow(
        executor=executor,
    )

    repository = ImageRepository()

    return UploadUseCase(
        workflow=workflow,
        repository=repository,
    )