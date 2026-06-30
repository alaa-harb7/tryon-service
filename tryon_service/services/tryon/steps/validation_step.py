from __future__ import annotations

from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)
from tryon_service.services.tryon.validation import (
    VirtualTryOnValidator,
)


class ValidationStep:

    def execute(
        self,
        request: VirtualTryOnRequest,
    ) -> VirtualTryOnRequest:

        VirtualTryOnValidator.validate(request)

        return request