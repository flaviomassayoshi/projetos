# Diretrizes Técnicas do Ambiente Local

- GPU principal: NVIDIA GeForce RTX 4070
- Driver NVIDIA: 576.52
- Versão CUDA reportada pelo driver: 12.9 (utilizar builds PyTorch/xFormers para CUDA 12.1 ou superior)
- Python: 3.10.11
- Ambiente virtual dedicado para cada subprojeto (exemplo: `venv` em `stable_diffusion_webui`)
- Recomendações para IA:
  - Instalar PyTorch com suporte CUDA 12.1: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
  - Para xFormers, preferir build compatível com CUDA 12.x e Python 3.10
  - Evitar misturar builds CPU-only e CUDA no mesmo ambiente virtual
  - Flags como `--use-cpu all` só devem ser usadas se não houver GPU disponível
  - Em caso de erro "Torch not compiled with CUDA enabled", revisar instalação do PyTorch e dependências
  - Para troubleshooting, usar `nvidia-smi` para checar driver e disponibilidade da GPU
