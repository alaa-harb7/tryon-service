from tryon_service.providers.pipeline.provider import (
    CatVTONPipelineProvider,
)

print("=" * 60)
print("Loading CatVTON Pipeline...")
print("=" * 60)

provider = CatVTONPipelineProvider()

provider.load()

print("=" * 60)
print("Pipeline Loaded Successfully")
print("=" * 60)
print(provider.is_loaded)