from tryon_service.providers.masking.provider import (
    AutoMaskerProvider,
)

provider = AutoMaskerProvider()

print("Loading AutoMasker...")

provider.load()

print("Loaded:", provider.is_loaded)