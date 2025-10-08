# Checklist: Execução de scripts e ativação de venv no Windows
- [PENDENTE] Avaliação prévia de custo/complexidade do prompt antes de execuções onerosas (inclusão de diretriz em copilot-instructions.md)
- [x] Criar diretriz específica para execution policy e ativação de venv
- [x] Atualizar índice em copilot-instructions.md
- [ ] Garantir que toda automação/execução de comandos que dependam de venv ativa siga a diretriz
# Pendências do Projeto

- [x] Criar repositório remoto no GitHub e conectar ao repositório local
- [x] Autenticar o GitHub CLI (gh) para criação automática do repositório
- [x] Realizar o commit inicial e push para o repositório remoto
- [ ] Configurar integração contínua (CI), se necessário
- [ ] Adicionar arquivos de configuração automáticos (.editorconfig, linters, etc.)
- [ ] Documentar o README.md do projeto



### Checklist para Configuração Avançada (LoL Skins)
- [ ] Instalar dependências: torch, torchvision, xformers
- [ ] Clonar repositório AUTOMATIC1111 da branch main
- [ ] Configurar `webui-user.bat` com argumentos: `--xformers --opt-sdp-attention --medvram`
- [ ] Criar pastas: `models/Lora/`, `embeddings/`
- [ ] Baixar LoRA e embeddings de personagens no Civitai
- [ ] Garantir compatibilidade com modelos como Anything V5, Counterfeit, DarkSushiMix
- [ ] Adicionar exemplo de prompt para gerar skin sombria da Lux e Neeko

> Objetivo: permitir que o usuário gere imagens de skins personalizadas de campeões do LoL com fidelidade visual, estilo splash art, e controle de composição.
