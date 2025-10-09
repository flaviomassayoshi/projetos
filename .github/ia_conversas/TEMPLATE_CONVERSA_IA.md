
# Template de Conversa Orquestrada entre IAs (Protocolo ScarecrowLab)

> Instruções de uso: Este arquivo serve como ponto de troca de mensagens entre agentes de IA, sempre mediado por orquestrador humano, conforme protocolo do arcabouço. Utilize este template ao criar novas conversas. Siga as diretrizes de nomeação, comandos e fluxo definidos no repositório.

## Participantes
- Orquestrador (humano):
- MCP (Microsoft Copilot):
- GHC (GitHub Copilot), se aplicável:

## Protocolo de Uso
- Toda comunicação entre agentes deve ser mediada pelo orquestrador humano.
- Cada mensagem deve ser precedida pelo nome do agente/remetente (ex: `@mcp:`, `@ghc:`, `@orquestrador:`).
- Utilize comandos padronizados conforme o arcabouço (ex: `@mcp: ler arquivoX.md`, `@ghc: atualizar manifesto`).
- Mantenha o histórico completo, sem apagar mensagens anteriores.
- Registre sempre contexto, tarefas, critérios de sucesso e referência, quando aplicável.


## Exemplo de Conversa Orquestrada

---

**@orquestrador:**
@mcp: Atualizar checklist de entrega conforme instruções abaixo.

Contexto:
- Nova pendência identificada no subprojeto X.

Tarefas:
1. Criar checklist de entrega.
2. Registrar changelog.

Critérios de sucesso:
- Checklist criado e vinculado ao subprojeto.
- Changelog registrado.

Referência: ata_debate_2025-10-08.md

**@mcp:**
Checklist criado e changelog registrado conforme solicitado.

---

> Sempre registre comandos, contexto e respostas de forma clara e rastreável. Consulte o arcabouço para detalhes completos do protocolo de comunicação orquestrada entre agentes.
