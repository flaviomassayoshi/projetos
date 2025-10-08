# Diretrizes Técnicas do Ambiente Local

- GPU: NVIDIA RTX 4070, driver 576.52, CUDA 12.9 (usar builds PyTorch/xFormers para CUDA 12.1+)
- Python 3.10.11
- Ambiente virtual dedicado por subprojeto
- Instalar PyTorch CUDA 12.1: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
- xFormers: build compatível CUDA 12.x, Python 3.10
- Não misturar builds CPU-only e CUDA
- Só usar `--use-cpu all` se não houver GPU
- Se erro "Torch not compiled with CUDA enabled", revisar instalação
- Para troubleshooting: `nvidia-smi` para checar driver/GPU
