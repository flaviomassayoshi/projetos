# Documento de Apoio — Copilot CLI vs Copilot Agent

## Relatório Minificado

### Copilot CLI
- Interface: Terminal (bash, zsh, PowerShell)
- Função: Sugere comandos shell via linguagem natural
- Instalação: `npm install -g @githubnext/copilot-cli`
- Autonomia: Baixa (não executa comandos)
- Integração: Indireta com GitHub (via comandos Git e `gh`)
- Uso típico: Automatizar tarefas simples, aprender terminal
- Consumo: Leve, sob demanda

### gh-copilot (CLI Extension)
- Interface: Terminal via GitHub CLI
- Instalação: `gh extension install github/gh-copilot`
- Comandos: `gh copilot suggest "ação desejada"`
- Integração: Com GitHub CLI (`gh`), útil para PRs, issues, workflows
- Pode simular um pseudo agente com scripts e aliases

### Copilot Agent
- Interface: GitHub Web, VS Code, GitHub Mobile
- Função: Executa tarefas completas via IA (edita código, abre PRs)
- Autonomia: Alta (planeja, propõe, testa)
- Segurança: PRs exigem revisão humana, ambiente isolado
- Integração: Direta com GitHub Actions e repositórios
- Linguagem natural: Sim, entende comandos como “corrigir erro de login”

### Comparativo

| Recurso         | CLI / gh-copilot        | Copilot Agent             |
|-----------------|-------------------------|---------------------------|
| Interface       | Terminal                | GUI (GitHub, VS Code)     |
| Autonomia       | Baixa                   | Alta                      |
| Execução        | Manual                  | Automatizada (com revisão)|
| Contexto        | Parcial                 | Completo do repositório   |
| Segurança       | Manual                  | Isolado e rastreável      |

### Conclusão
Copilot CLI pode funcionar como pseudo agente com criatividade, mas o Copilot Agent é a solução oficial e integrada para tarefas autônomas com IA no GitHub.
