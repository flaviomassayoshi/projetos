
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
- Registre sempre contexto, tarefas, critérios de sucesso e referência, prompt detalhado (espaço para maiores informaçoes, conteúdo de artefatos) quando aplicável.



## Exemplo de Conversa Orquestrada (Formato Ampliado)

---

**@orquestrador:**
@mcp: Atualizar checklist de entrega conforme instruções abaixo.

Contexto:
- Nova pendência identificada no subprojeto X.

Artefatos envolvidos:
- Checklist, changelog, README

Subprojeto relacionado:
- agente-integrador

Tarefas:
1. Criar checklist de entrega.
2. Registrar changelog.

Status atual da pendência:
- Checklist não iniciado

Justificativa da ação:
- Nova decisão registrada em ata, exige atualização do fluxo.

Critérios de sucesso:
- Checklist criado e vinculado ao subprojeto.
- Changelog registrado.

Links de referência:
- ata_debate_2025-10-08.md

**@mcp:**
Checklist criado e changelog registrado conforme solicitado. Segue o conteúdo dos artefatos gerados/atualizados:

---
**Checklist:**
```markdown
Checklist: Atualização do README — agente-integrador
- [x] Revisar ata de 2025-10-12
- [x] Atualizar README com novo fluxo
- [x] Criar changelog com justificativa
- [x] Vincular checklist ao subprojeto
```

**Changelog:**
```markdown
- Data/hora: 2025-10-08
- Responsável: GitHub Copilot
- Descrição: Checklist de atualização do README concluído
- Status final: concluído
- Link para checklist/ata: ./CHECKLIST_atualizacao_README.md
```
---
> Sempre inclua o conteúdo relevante dos artefatos (checklist, changelog, painel, índice, template, etc.) diretamente na resposta, evitando apenas links. Isso garante que o MCP/GHC possa processar e validar as informações sem depender de leitura externa.

---

> Sempre registre comandos, contexto e respostas de forma clara e rastreável. Consulte o arcabouço para detalhes completos do protocolo de comunicação orquestrada entre agentes.
