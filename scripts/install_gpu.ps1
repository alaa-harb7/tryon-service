python -m pip install --upgrade pip setuptools wheel

pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu121

pip install ^
fastapi>=0.116.1 ^
uvicorn[standard]>=0.35.0 ^
pydantic>=2.11.7 ^
pydantic-settings>=2.10.1 ^
python-dotenv>=1.1.1 ^
PyYAML>=6.0.2 ^
loguru>=0.7.3 ^
httpx>=0.28.1 ^
motor>=3.7.1 ^
pymongo>=4.13.2 ^
mediapipe>=0.10.21 ^
accelerate==0.31.0 ^
transformers==4.46.3 ^
numpy==1.26.4 ^
opencv-python-headless==4.10.0.84 ^
Pillow==10.3.0 ^
scipy==1.13.1 ^
scikit-image==0.24.0 ^
tqdm==4.66.4 ^
fvcore==0.1.5.post20221221 ^
cloudpickle==3.0.0 ^
omegaconf==2.3.0 ^
pycocotools==2.0.8 ^
av==12.3.0 ^
peft>=0.17.0 ^
huggingface_hub>=0.34.0,<2.0

pip install -e . --no-deps