import argparse
import os
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))


def warmup_models():
    print("=" * 60)
    print("Warming up models (CatVTON, AutoMasker, MediaPipe)")
    print("=" * 60)
    try:
        from tryon_service.providers.pipeline.provider import (
            CatVTONPipelineProvider,
        )
        from tryon_service.services.masking.automask_service import (
            AutoMaskService,
        )

        print("Warming up CatVTON Pipeline...")
        catvton = CatVTONPipelineProvider()
        catvton.load()

        print("Warming up AutoMask Service...")
        masker = AutoMaskService()

        print("✓ Models loaded successfully to device.")
    except Exception as e:
        print(f"⚠️ Warning: Could not pre-warm models: {e}")


def run_server(host: str, port: int, ngrok_token: str | None):
    # Apply nest_asyncio to prevent loop conflict in Google Colab Jupyters
    try:
        import nest_asyncio

        nest_asyncio.apply()
        print("✓ nest_asyncio applied successfully.")
    except ImportError:
        print("⚠️ Warning: nest_asyncio not installed.")

    # Optional public ngrok tunnel
    if ngrok_token:
        try:
            from pyngrok import ngrok

            ngrok.set_auth_token(ngrok_token)
            public_url = ngrok.connect(port)
            print("=" * 60)
            print(f"🌍 Ngrok Tunnel Active: {public_url}")
            print("=" * 60)
        except ImportError:
            print("❌ Failed to start ngrok tunnel: pyngrok is not installed.")

    import uvicorn

    print(f"Starting FastAPI Try-On Service on http://{host}:{port}...")
    uvicorn.run(
        "tryon_service.main:app",
        host=host,
        port=port,
        reload=False,
        access_log=True,
        log_level="info",
    )


def main():
    parser = argparse.ArgumentParser(description="Google Colab Server Runner")
    parser.add_argument("--host", default="0.0.0.0", help="Binding host")
    parser.add_argument("--port", type=int, default=8000, help="Binding port")
    parser.add_argument("--warmup", action="store_true", help="Warm up models before start")
    parser.add_argument("--ngrok", default=None, help="Optional ngrok auth token")
    args = parser.parse_args()

    # Pre-configure environment settings
    os.environ["APP_ENV"] = "development"
    os.environ["APP_DEBUG"] = "true"
    if "MONGODB_URI" not in os.environ:
        # Fallback to local mock db or default if not set
        required = [
            "MONGODB_URI",
            "DB_NAME",
        ]

        for key in required:

            if key not in os.environ:

                raise RuntimeError(
                    f"{key} is missing."
                )
    if "DB_NAME" not in os.environ:
        required = [
            "MONGODB_URI",
            "DB_NAME",
        ]

        for key in required:

            if key not in os.environ:

                raise RuntimeError(
                    f"{key} is missing."
                )

    if args.warmup:
        warmup_models()

    run_server(args.host, args.port, args.ngrok)


if __name__ == "__main__":
    main()
