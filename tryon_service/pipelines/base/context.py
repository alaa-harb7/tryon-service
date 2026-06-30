from __future__ import annotations

from dataclasses import dataclass, field


from tryon_service.models.pipeline.analysis import AnalysisContext
from tryon_service.models.pipeline.assets import AssetsContext
from tryon_service.models.pipeline.inference import InferenceContext
from tryon_service.models.pipeline.metadata import MetadataContext
from tryon_service.models.pipeline.request import RequestContext
from tryon_service.models.pipeline.result import ResultContext
from tryon_service.models.pipeline.validation import ValidationContext
from tryon_service.pipelines.base.human_context import HumanContext


@dataclass(slots=True)
class PipelineContext:
    """
    Shared context passed through the entire Try-On workflow.
    """

    request: RequestContext = field(default_factory=RequestContext)

    assets: AssetsContext = field(default_factory=AssetsContext)

    analysis: AnalysisContext = field(default_factory=AnalysisContext)

    validation: ValidationContext = field(default_factory=ValidationContext)

    inference: InferenceContext = field(default_factory=InferenceContext)

    result: ResultContext = field(default_factory=ResultContext)

    metadata: MetadataContext = field(default_factory=MetadataContext)

    human: HumanContext = field(default_factory=HumanContext )