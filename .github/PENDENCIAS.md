# Pendências do Projeto

- [x] Criar repositório remoto no GitHub e conectar ao repositório local
- [x] Autenticar o GitHub CLI (gh) para criação automática do repositório
- [x] Realizar o commit inicial e push para o repositório remoto
- [ ] Configurar integração contínua (CI), se necessário
- [ ] Adicionar arquivos de configuração automáticos (.editorconfig, linters, etc.)
- [ ] Documentar o README.md do projeto

## Stable Diffusion WebUI
- [ ] Garantir instalação do PyTorch com suporte CUDA 12.1 para RTX 4070
- [ ] Ajustar/remover flags de CPU nos scripts de inicialização
- [ ] Validar funcionamento do xFormers com CUDA
- [ ] Testar geração de imagens utilizando GPU
- [ ] Documentar setup e troubleshooting específico para GPU

### Checklist para Configuração Avançada (LoL Skins)
- [ ] Instalar dependências: torch, torchvision, xformers
- [ ] Clonar repositório AUTOMATIC1111 da branch main
- [ ] Configurar `webui-user.bat` com argumentos: `--xformers --opt-sdp-attention --medvram`
- [ ] Criar pastas: `models/Lora/`, `embeddings/`
- [ ] Baixar LoRA e embeddings de personagens no Civitai
- [ ] Garantir compatibilidade com modelos como Anything V5, Counterfeit, DarkSushiMix
- [ ] Adicionar exemplo de prompt para gerar skin sombria da Lux e Neeko

> Objetivo: permitir que o usuário gere imagens de skins personalizadas de campeões do LoL com fidelidade visual, estilo splash art, e controle de composição.
