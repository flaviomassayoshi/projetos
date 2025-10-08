
# Execução de scripts/venv no Windows (IA-only)

- Antes de ativar venv: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
- Ativar venv: `.\venv\Scripts\Activate.ps1`
- Só depois rodar comandos ou .bat dependentes do venv
- Sempre aplicar em subprojetos Python/Windows
