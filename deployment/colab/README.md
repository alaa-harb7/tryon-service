# Google Colab Microservice Deployment

This directory contains the deployment layer designed for executing the Virtual Try-On microservice inside a Google Colab GPU runtime.

---

## Prerequisites

Ensure your Google Colab instance is configured with a **GPU** (T4, V100, or A100). You can check and modify this by navigating to `Runtime` -> `Change runtime type` -> select `T4 GPU` (or higher).

---

## Quick Start (Google Colab Notebook)

Run the following cell to clone the repository and start setup:

```python
# 1. Clone the microservice repository
!git clone https://github.com/<your-username>/tryon-service.git
%cd tryon-service

# 2. Run the dynamic environment installation & weights downloader
!python deployment/colab/setup_colab.py
```

---

## Running the Service

After setup is complete, launch the server by specifying an optional `--ngrok` token to expose the API to the public internet:

```python
# Start the FastAPI server and warm up models in VRAM
!python deployment/colab/run_colab.py --warmup --ngrok <your_ngrok_auth_token>
```

---

## File Structure & Responsibilities

- **[requirements-colab.txt](file:///d:/Front/End/Projects/tryon-service/deployment/colab/requirements-colab.txt)**: Tailored dependencies avoiding conflicts with preinstalled PyTorch packages on Google Colab.
- **[download_models.py](file:///d:/Front/End/Projects/tryon-service/deployment/colab/download_models.py)**: Coordinates downloading and verifying local weights (`MediaPipe`, `YOLO`, `SCHP`, `DensePose`).
- **[setup_colab.py](file:///d:/Front/End/Projects/tryon-service/deployment/colab/setup_colab.py)**: Central orchestrator that handles verification, clones submodules (`external/catvton`), and installs requirements.
- **[run_colab.py](file:///d:/Front/End/Projects/tryon-service/deployment/colab/run_colab.py)**: Warms up pipelines to VRAM and starts the web server.
