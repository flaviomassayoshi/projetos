

# Template de Conversa Orquestrada entre IAs (Protocolo ScarecrowLab)

> Instruções de uso: Este arquivo é o modelo operacional obrigatório para toda conversa orquestrada entre agentes de IA no ScarecrowLab. Sempre consulte e alinhe o registro de conversas ao protocolo oficial (`copilot-diretrizes/protocolo_orquestracao_chat.md`). Utilize este template ao criar novas conversas. Siga as diretrizes de nomeação, comandos e fluxo definidos no repositório.


## Participantes (preencher sempre no início da conversa)
- Orquestrador (humano): <nome ou identificação>
- MCP (Microsoft Copilot): <modelo ou identificação>
- GHC (GitHub Copilot), se aplicável: <modelo ou identificação>
- Outros agentes/modelos (se houver): <nome/modelo>

> Sempre declare explicitamente todos os participantes e seus papéis antes de iniciar a conversa. Isso elimina ambiguidades e facilita a rastreabilidade.



## Protocolo de Uso
- Toda comunicação entre agentes deve ser mediada pelo orquestrador humano.
- No início de cada prompt, identifique explicitamente o modelo de origem e o de destino, por exemplo:
	- De: @mcp
	- Para: @ghc
- Cada mensagem pode ser precedida pelo nome do agente/remetente (ex: `@mcp:`, `@ghc:`, `@orquestrador:`), mas a identificação explícita de origem e destino é obrigatória em fluxos com múltiplos agentes.
- Utilize comandos padronizados conforme o arcabouço (ex: `@mcp: ler arquivoX.md`, `@ghc: atualizar manifesto`).
- Mantenha o histórico completo, sem apagar mensagens anteriores.
- Registre sempre contexto, tarefas, critérios de sucesso e referência, prompt detalhado (espaço para maiores informações, conteúdo de artefatos) quando aplicável.
- **Todo registro de conversa deve estar alinhado ao protocolo oficial de orquestração (`copilot-diretrizes/protocolo_orquestracao_chat.md`). Em caso de atualização em qualquer um desses artefatos, revise ambos para garantir alinhamento e evitar divergências.**
- **Cabeçalhos autossuficientes:** Todo prompt deve seguir a [Diretriz de Cabeçalhos Autossuficientes](../copilot-diretrizes/diretrizes_cabecalhos_autossuficientes.md). Valide com [Checklist de Validação](../copilot-diretrizes/CHECKLIST_VALIDACAO_CABECALHOS.md) antes de submeter.




## Exemplo de Conversa Orquestrada (Formato Ampliado)

Participantes:
- Orquestrador (humano): Flavio
- MCP (Microsoft Copilot): modelo X
- GHC (GitHub Copilot): modelo Y

---

**De:** @orquestrador  
**Para:** @mcp

**Objetivo:** Atualizar checklist de entrega conforme instruções abaixo.

**Contexto:**  
Nova pendência identificada no subprojeto X. Nova decisão registrada em ata de 2025-10-08 exige atualização do fluxo.

**Artefato(s)/Subprojeto(s):**
- Checklist de entrega
- Changelog  
- README
- Subprojeto: agente-integrador

**Tarefas:**
1. Criar checklist de entrega
2. Registrar changelog
3. Vincular ao subprojeto no painel central

**Status atual da pendência:**  
Checklist não iniciado

**Critérios de Sucesso:**
- [ ] Checklist criado e vinculado ao subprojeto
- [ ] Changelog registrado
- [ ] Painel central atualizado

**Referência:** debates/ata_debate_2025-10-08.md

---

**Validação de Cabeçalho Autossuficiente:** ✅  
(Checklist: Identificação ✓ | Objetivo ✓ | Contexto ✓ | Artefatos ✓ | Critérios ✓ | Referência ✓)

---

De: @mcp
Para: @orquestrador
Checklist criado e changelog registrado conforme solicitado. Segue o conteúdo dos artefatos gerados/atualizados:

---

**@orquestrador:**

**De:** @orquestrador  
**Para:** @mcp

**Objetivo:** Atualizar checklist de entrega conforme instruções abaixo.

**Contexto:**  
Nova pendência identificada no subprojeto X. Nova decisão registrada em ata de 2025-10-08 exige atualização do fluxo.

**Artefato(s)/Subprojeto(s):**
- Checklist de entrega
- Changelog  
- README
- Subprojeto: agente-integrador

**Tarefas:**
1. Criar checklist de entrega
2. Registrar changelog
3. Vincular ao subprojeto no painel central

**Critérios de Sucesso:**
- [ ] Checklist criado e vinculado ao subprojeto
- [ ] Changelog registrado
- [ ] Painel central atualizado

**Referência:** debates/ata_debate_2025-10-08.md

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
> Recomendações do MCP para robustez do fluxo:
> - O MCP deve sinalizar automaticamente subprojetos citados que estejam ausentes ou desatualizados no painel central.
> - Validar se há changelogs ou atas vinculadas aos subprojetos impactados e sinalizar ausência ou desatualização como pendência crítica.
> - O changelog deve ser atualizado e coerente com o painel central, checklist e atas; divergências devem ser tratadas como prioridade.
> - O prompt de ativação proativa pode incluir variações como: `@mcp: revise pendências abertas nos subprojetos impactados`.
> - Campo opcional “Impacto Esperado” pode ser incluído para registrar o efeito da atualização sobre fluxos ou decisões estratégicas.

---

> Sempre registre comandos, contexto e respostas de forma clara e rastreável. Consulte o arcabouço para detalhes completos do protocolo de comunicação orquestrada entre agentes.
