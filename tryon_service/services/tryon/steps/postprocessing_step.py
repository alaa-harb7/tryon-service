from __future__ import annotations

from tryon_service.services.tryon.result import (
    VirtualTryOnResult,
)


class PostprocessingStep:

    def execute(
        self,
        pipeline_result,
        mask_result,
    ) -> VirtualTryOnResult:

        return VirtualTryOnResult(
            image=pipeline_result[0],
            mask=mask_result["mask"],
            densepose=mask_result["densepose"],
            schp_lip=mask_result["schp_lip"],
            schp_atr=mask_result["schp_atr"],
        )