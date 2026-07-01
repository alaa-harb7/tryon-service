import torch

print("=" * 50)
print("Torch Version :", torch.__version__)
print("Torch CUDA    :", torch.version.cuda)
print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU Name      :", torch.cuda.get_device_name(0))
    print("GPU Count     :", torch.cuda.device_count())
else:
    print("Running on CPU")
print("=" * 50)