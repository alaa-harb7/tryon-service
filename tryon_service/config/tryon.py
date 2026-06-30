from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TryOnConfig:

    PERSON_WIDTH = 768
    PERSON_HEIGHT = 1024

    GARMENT_WIDTH = 768
    GARMENT_HEIGHT = 1024

    OUTPUT_WIDTH = 384
    OUTPUT_HEIGHT = 512

    NUM_INFERENCE_STEPS = 50

    GUIDANCE_SCALE = 2.5

    RANDOM_SEED = 555