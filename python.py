import torch
print("CUDA Available:", torch.cuda.is_available())

# Check GPU name
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA Version:", torch.version.cuda)
    print("Torch Version:", torch.__version__)