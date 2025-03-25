# pip uninstall torch torchvision torchaudio -> since run on venv it not use cuda 
# install CUDA for NVIDIA GPU pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
import torch
print("CUDA Available:", torch.cuda.is_available())
print("GPU Count:", torch.cuda.device_count())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")