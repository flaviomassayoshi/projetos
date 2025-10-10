# AVISO IMPORTANTE

Para instruções detalhadas de atualização, checklist MVP e critérios, consulte exclusivamente o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` e o arcabouço em `.github/copilot-diretrizes/`. O manifesto consolidado não deve conter instruções operacionais ou fluxos de atualização: mantenha o foco em fluxos, exemplos, painéis e glossário.

# MANIFESTO CONSOLIDADO — SCARECROWLAB (MCP)

**Objetivo:** Garantir que toda atualização do manifesto produza um arquivo único, detalhado e autoexplicativo (formato `ManifestoMCP.md`), compatível com o agente MCP (Microsoft Copilot) e adequado para comunicação e operação no contexto do ScarecrowLab.

## Índice de Anexos e Templates do ScarecrowLab

- .github/copilot-diretrizes/glossario.md
- .github/copilot-diretrizes/fluxos_gerais_agentes.md
- .github/copilot-diretrizes/checklist_comunicacao.md
- .github/copilot-diretrizes/fluxos_encerramento.md
- .github/copilot-diretrizes/diretrizes_subprojetos.md
- .github/copilot-diretrizes/protocolo_orquestracao_chat.md *(referência obrigatória para fluxos de interação)*
- .github/copilot-diretrizes/templates_index.md
- .github/copilot-diretrizes/checklists_praticos.md
- .github/copilot-diretrizes/template_changelog.md
- .github/copilot-diretrizes/diretrizes_tecnicas.md
- .github/copilot-diretrizes/convenções_codigo.md
- .github/copilot-diretrizes/projetos_terceiros.md
- .github/copilot-diretrizes/diretrizes_execucao_venv_windows.md
- .github/copilot-diretrizes/instrucoes_setup_CI.md
- .github/copilot-diretrizes/diretrizes_debate.md
- .github/copilot-diretrizes/fluxo_revisao_diretrizes.md
- .github/TEMPLATE_ATUALIZACAO_MANIFESTO.md
- .github/TEMPLATE_CHECKLIST.md
- .github/TEMPLATE_CHECKLIST_ENTREGA.md
- .github/TEMPLATE_PLANO_ACAO.md
- .github/ia_conversas/TEMPLATE_CONVERSA_IA.md *(referência obrigatória para prompts de conversa)*
- .github/painel_subprojetos.md *(painel central de subprojetos)*
- python_apps/validacao_ia_multimodelo/README.md
- python_apps/validacao_ia_multimodelo/CHECKLIST.md
- python_apps/viabilizacao_debate_multimodelo/README.md
- python_apps/viabilizacao_debate_multimodelo/CHECKLIST.md
- python_apps/viabilizacao_debate_multimodelo/ATA_MIGRACAO_MANIFESTO.md

---

## 1. Objetivo do Manifesto
Este manifesto consolida as regras, fluxos e exemplos essenciais para operação do ScarecrowLab, servindo como referência única para o MCP (Microsoft Copilot) e humanos. Garante rastreabilidade, governança e automação dos processos do laboratório.

## 2. Visão Geral
O ScarecrowLab é um laboratório de integração, automação e governança de projetos de IA, com foco em modularização, rastreabilidade e atuação proativa de agentes. O manifesto define o arcabouço operacional e a identidade do laboratório.

## 3. Princípios Centrais
- Modularização de subprojetos
- Rastreabilidade de decisões e artefatos
- Automação de fluxos e validações
- Integração entre agentes de IA (MCP, GHC, etc.)
- Transparência e governança

# AVISO IMPORTANTE

Para instruções detalhadas de atualização, checklist MVP e critérios, consulte exclusivamente o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` e o arcabouço em `.github/copilot-diretrizes/`. O manifesto consolidado não deve conter instruções operacionais ou fluxos de atualização: mantenha o foco em fluxos, exemplos, painéis e glossário.

# TEMPLATE DE ATUALIZAÇÃO DO MANIFESTO — SCARECROWLAB (MCP)

**Objetivo:** Garantir que toda atualização do manifesto produza um arquivo único, detalhado e autoexplicativo (formato `ManifestoMCP.md`), compatível com o agente MCP (Microsoft Copilot) e adequado para comunicação e operação no contexto do ScarecrowLab.

## Índice de Anexos e Templates do ScarecrowLab

- .github/copilot-diretrizes/glossario.md
- .github/copilot-diretrizes/fluxos_gerais_agentes.md
- .github/copilot-diretrizes/checklist_comunicacao.md
- .github/copilot-diretrizes/fluxos_encerramento.md
- .github/copilot-diretrizes/diretrizes_subprojetos.md
- .github/copilot-diretrizes/protocolo_orquestracao_chat.md
- .github/copilot-diretrizes/templates_index.md
- .github/copilot-diretrizes/checklists_praticos.md
- .github/copilot-diretrizes/template_changelog.md
- .github/copilot-diretrizes/diretrizes_tecnicas.md
- .github/copilot-diretrizes/convenções_codigo.md
- .github/copilot-diretrizes/projetos_terceiros.md
- .github/copilot-diretrizes/diretrizes_execucao_venv_windows.md
- .github/copilot-diretrizes/instrucoes_setup_CI.md
- .github/copilot-diretrizes/diretrizes_debate.md
- .github/copilot-diretrizes/fluxo_revisao_diretrizes.md
- .github/TEMPLATE_ATUALIZACAO_MANIFESTO.md
- .github/TEMPLATE_CHECKLIST.md
- .github/TEMPLATE_CHECKLIST_ENTREGA.md
- .github/TEMPLATE_PLANO_ACAO.md
- .github/ia_conversas/TEMPLATE_CONVERSA_IA.md
- .github/painel_subprojetos.md
- python_apps/validacao_ia_multimodelo/README.md
- python_apps/validacao_ia_multimodelo/CHECKLIST.md
- python_apps/viabilizacao_debate_multimodelo/README.md
- python_apps/viabilizacao_debate_multimodelo/CHECKLIST.md
- python_apps/viabilizacao_debate_multimodelo/ATA_MIGRACAO_MANIFESTO.md
- ... (demais arquivos relevantes de subprojetos)
// Para checklist completo, solicite ao GHC via prompt.
```

---

### 16. Critérios para Atuação Proativa do MCP
- Quando há pendência registrada com tarefas não concluídas
- Quando há checklist incompleto ou changelog ausente
- Quando há ata com decisões sem plano de ação vinculado

---

### 17. Prompt de Ativação Proativa
```markdown
@orquestrador: @mcp: Atue proativamente sobre pendências registradas no manifesto. Priorize aquelas com checklist incompleto ou changelog ausente.
```

---

### 18. Artefato embutido no prompt (opcional)
Em situações onde o MCP ou orquestrador precise processar o conteúdo bruto de um artefato (ex: README, checklist, changelog) diretamente no corpo do prompt, o conteúdo pode ser incluído usando bloco markdown. Isso permite análise, validação ou extração de informações sem depender de arquivos externos.

**Exemplo funcional:**
```markdown
@ghc: Analise o seguinte README e gere um checklist de pendências:

```markdown
# README — Subprojeto X
Fluxo: ...
Pendências:
- [ ] Ajustar integração
- [ ] Revisar documentação
```
```

Oriente sempre a identificar claramente o início e fim do artefato embutido, usando blocos markdown aninhados se necessário.

---

> Sempre que atualizar o manifesto, garanta que ele seja autossuficiente, reflita a identidade e os fluxos vigentes do laboratório, e seja compatível com o MCP (Microsoft Copilot). Além disso, atualize o manifesto.

