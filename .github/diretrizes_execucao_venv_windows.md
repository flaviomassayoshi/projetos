# Diretriz: Execução de Scripts e Ativação de Ambientes Virtuais no Windows

Sempre que for necessário executar comandos que dependam de um ambiente virtual Python (venv) no Windows, é obrigatório garantir que a política de execução do PowerShell permita a execução do script de ativação do venv antes de rodar qualquer comando ou .bat dependente do ambiente.

## Procedimento Padrão

1. **Verifique e ajuste a Execution Policy:**
   - Antes de ativar o venv, execute:
     ```powershell
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
     ```
   - Isso garante que o script de ativação (`venv\Scripts\Activate.ps1`) será executado sem bloqueios.

2. **Ative o ambiente virtual:**
   - Execute o script de ativação do venv:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

3. **Execute o comando desejado ou o .bat do projeto:**
   - Após ativar o ambiente, execute o comando ou script principal normalmente.

## Observações
- Esta diretriz se aplica a todos os subprojetos que utilizam ambientes virtuais Python no Windows.
- Sempre consulte este documento antes de automatizar execuções que dependam de venv.
- Para mais detalhes, consulte as instruções gerais em `copilot-instructions.md`.
