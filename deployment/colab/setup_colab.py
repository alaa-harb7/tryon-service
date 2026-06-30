import os
import subprocess
import sys
from pathlib import Path

# Fix sys.path to resolve project root imports
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))


def run_command(command: list[str], cwd: Path = PROJECT_ROOT):
    print(f"Executing: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error during command execution:\n{result.stderr}")
        sys.exit(result.returncode)
    print(result.stdout)


def verify_hardware():
    print("=" * 60)
    print("Verifying Hardware Context")
    print("=" * 60)
    try:
        import torch

        cuda_available = torch.cuda.is_available()
        print(f"PyTorch Version: {torch.__version__}")
        print(f"CUDA Available: {cuda_available}")
        if cuda_available:
            print(f"GPU Device Name: {torch.cuda.get_device_name(0)}")
            print(f"CUDA Device Count: {torch.cuda.device_count()}")
        else:
            print("⚠️ WARNING: Running on CPU. Performance will be degraded.")
    except ImportError:
        print("❌ PyTorch is not installed in the environment!")
        sys.exit(1)


def install_dependencies():
    print("=" * 60)
    print("Installing Dependencies")
    print("=" * 60)
    req_file = PROJECT_ROOT / "deployment" / "colab" / "requirements-colab.txt"
    run_command([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
    # Also install the current project in editable mode
    run_command(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-e",
            ".",
            "--no-deps",
        ]
    )


def setup_external_repositories():
    print("=" * 60)
    print("Setting Up External Repositories (CatVTON)")
    print("=" * 60)
    external_dir = PROJECT_ROOT / "external"
    external_dir.mkdir(exist_ok=True)

    catvton_path = external_dir / "catvton"
    if not catvton_path.exists():
        print("Cloning CatVTON repository...")
        run_command(
            [
                "git",
                "clone",
                "https://github.com/Zheng-Chong/CatVTON.git",
                
                str(catvton_path),
            ]
        )
    else:
        print("✓ CatVTON repository already cloned.")

print("Checking CatVTON repository...")

def create_required_directories():
    print("=" * 60)
    print("Creating Required Directories")
    print("=" * 60)
    dirs = ["outputs", "logs", "temp", "storage/uploads/original"]
    for d in dirs:
        dir_path = PROJECT_ROOT / d
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Directory ready: {d}")


def run_model_health_check():
    print("=" * 60)
    print("Running Model Health Checks")
    print("=" * 60)
    # Check if files exist
    checks = {
        "MediaPipe Pose": "assets/models/mediapipe/pose_landmarker.task",
        "YOLO ONNX": "models/person_detection/yolo11n.onnx",
        "SCHP ATR": "assets/models/catvton/SCHP/exp-schp-201908301523-atr.pth",
        "SCHP LIP": "assets/models/catvton/SCHP/exp-schp-201908261155-lip.pth",
        "DensePose Config Base": "assets/models/catvton/DensePose/Base-DensePose-RCNN-FPN.yaml",
        "DensePose Config R50": "assets/models/catvton/DensePose/densepose_rcnn_R_50_FPN_s1x.yaml",
    }
    missing = False
    for name, relative_path in checks.items():
        full_path = PROJECT_ROOT / relative_path
        if full_path.exists():
            print(f"✓ {name}: Present")
        else:
            print(f"❌ {name}: MISSING ({relative_path})")
            missing = True
    if missing:
        print("❌ Health check failed. Some model files are missing.")
        sys.exit(1)
    else:
        print("✓ All model files are present and verified.")


def main():
    verify_hardware()
    install_dependencies()
    setup_external_repositories()

    # Trigger model download script
    from deployment.colab.download_models import download_all_models

    download_all_models()

    create_required_directories()
    run_model_health_check()

    print("=" * 60)
    print("Colab Environment Ready Summary")
    print("=" * 60)
    try:
        import torch

        gpu_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None (CPU)"
    except Exception:
        gpu_name = "Unknown"

    summary = f"""
=====================================
Environment Ready
GPU: {gpu_name}
CUDA: {"Available" if gpu_name != "None (CPU)" else "Not Available"}
Models:
  ✓ CatVTON (HF Hub ready)
  ✓ YOLO (Present)
  ✓ SCHP (Present)
  ✓ DensePose (Present)
  ✓ MediaPipe (Present)
FastAPI Ready
=====================================
"""
    print(summary)


if __name__ == "__main__":
    main()
