from pathlib import Path

from ultralytics import YOLO


ROOT = Path(__file__).resolve().parents[1]

weights = (
    ROOT
    / "models"
    / "person_detection"
    / "weights"
    / "yolo11n.pt"
)

model = YOLO(str(weights))

model.export(
    format="onnx",
    imgsz=640,
    opset=17,
    simplify=True,
)