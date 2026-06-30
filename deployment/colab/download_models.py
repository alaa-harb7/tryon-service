import os
import urllib.request
from pathlib import Path

# Paths mapping relative to project root
MEDIAPIPE_DIR = Path("assets/models/mediapipe")
YOLO_DIR = Path("models/person_detection")
SCHP_DIR = Path("assets/models/catvton/SCHP")
DENSEPOSE_DIR = Path("assets/models/catvton/DensePose")


def download_file(url: str, output_path: Path):
    if output_path.exists():
        print(f"✓ {output_path.name} already exists. Skipping download.")
        return
    print(f"Downloading {output_path.name} from {url}...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(url, str(output_path))
        print(f"✓ Successfully downloaded {output_path.name}")
    except Exception as e:
        print(f"❌ Failed to download {output_path.name}: {e}")
        raise e


def download_all_models():
    print("=" * 60)
    print("Downloading Model Weights")
    print("=" * 60)

    # 1. MediaPipe Pose Landmarker
    mediapipe_url = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/1/pose_landmarker_heavy.task"
    download_file(mediapipe_url, MEDIAPIPE_DIR / "pose_landmarker.task")

    # 2. YOLOv11 ONNX Bounding Box Detector
    yolo_url = "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.onnx"
    download_file(yolo_url, YOLO_DIR / "yolo11n.onnx")

    # 3. SCHP Models (ATR & LIP)
    schp_atr_url = "https://huggingface.co/zhengchong/CatVTON/resolve/main/resource/parser/ltr.pth"
    schp_lip_url = "https://huggingface.co/zhengchong/CatVTON/resolve/main/resource/parser/lip.pth"
    download_file(schp_atr_url, SCHP_DIR / "exp-schp-201908301523-atr.pth")
    download_file(schp_lip_url, SCHP_DIR / "exp-schp-201908261155-lip.pth")

    # 4. DensePose Configs & Weights (Loaded directly via CatVTON architecture)
    dp_config_base = "https://raw.githubusercontent.com/facebookresearch/detectron2/main/projects/DensePose/configs/Base-DensePose-RCNN-FPN.yaml"
    dp_config_r50 = "https://raw.githubusercontent.com/facebookresearch/detectron2/main/projects/DensePose/configs/densepose_rcnn_R_50_FPN_s1x.yaml"
    download_file(dp_config_base, DENSEPOSE_DIR / "Base-DensePose-RCNN-FPN.yaml")
    download_file(dp_config_r50, DENSEPOSE_DIR / "densepose_rcnn_R_50_FPN_s1x.yaml")

    print("\n✓ All model downloads completed successfully!\n")


if __name__ == "__main__":
    download_all_models()
