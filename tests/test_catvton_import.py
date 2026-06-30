import pytest

from tryon_service.bootstrap.catvton_environment import (
    CatVTONEnvironment,
)


@pytest.mark.skip(
    reason=(
        "Integration test: requires CatVTON external repo on sys.path. "
        "Run after calling CatVTONEnvironment.initialize() in the application lifespan."
    )
)
def test_import_automasker():

    CatVTONEnvironment.initialize()

    from external.catvton.model.cloth_masker import AutoMasker  # noqa: F401

    assert AutoMasker is not None