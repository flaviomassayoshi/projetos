## [08/10/2025  - Execução de scripts e ativação de venv no Windows]

- Criada diretriz específica (`diretrizes_execucao_venv_windows.md`) para garantir que a execução de scripts que dependam de ambientes virtuais Python no Windows sempre ajuste a execution policy antes de ativar o venv.
- Atualizado o índice em `copilot-instructions.md` para referenciar a nova diretriz.
- A partir de agora, toda automação ou execução de comandos que dependam de venv ativa no Windows deve obrigatoriamente seguir este procedimento.
