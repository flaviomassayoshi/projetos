# TEMPLATE DE PROMPT PADRÃO — SCARECROWLAB

**Objetivo:** Estruturar prompts de forma padronizada, garantindo rastreabilidade, clareza e alinhamento com o arcabouço do ScarecrowLab.

---

## Identificação do Prompt

🔑 **Identificador único do prompt:**  
`[gerar_guid]`

> A instrução `[gerar_guid]` deve ser processada pelo agente MCP/GHC para gerar automaticamente um identificador único (GUID/UUID) no momento da execução. Este identificador garante rastreabilidade completa do prompt em logs, changelogs, painéis e manifestos.

---

## Dados do Prompt

**De:** @[agente_origem]  
**Para:** @[agente_destino]  
**Data/hora:** [AAAA-MM-DD HH:MM]

---

## Contexto

Descreva brevemente o contexto da solicitação, incluindo:
- Situação atual
- Motivação da ação
- Dependências ou pré-requisitos

---

## Objetivo

Descreva de forma clara e objetiva o que se espera alcançar com este prompt.

---

## Tarefas

Liste as tarefas específicas a serem executadas:

1. [ ] Tarefa 1
2. [ ] Tarefa 2
3. [ ] Tarefa 3

---

## Artefatos Envolvidos

Liste os artefatos que serão criados, atualizados ou consultados:

- [ ] Checklist
- [ ] Changelog
- [ ] README
- [ ] Ata
- [ ] Outros: _______

---

## Subprojeto Relacionado (se aplicável)

Nome do subprojeto conforme painel central: _______

> Sempre referencie subprojetos usando o painel central (`.github/painel_subprojetos.md`) como fonte única de verdade.

---

## Critérios de Sucesso

Liste critérios claros e mensuráveis para considerar o prompt concluído:

- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

---

## Justificativa de Persistência

Explique se este prompt e seus artefatos devem ser:
- **Temporário:** Para ações pontuais sem impacto estrutural
- **Persistente:** Para decisões estratégicas, fluxos complexos, múltiplos agentes ou rastreabilidade obrigatória

**Justificativa:** _______

---

## Links de Referência

Liste links para artefatos, atas, debates ou documentação relevante:

- [ ] Link 1
- [ ] Link 2
- [ ] Link 3

---

## Observações Adicionais (opcional)

Inclua quaisquer observações, restrições, alertas ou informações complementares relevantes para a execução do prompt.

---

> **Instruções de uso:**  
> - Este template deve ser utilizado para todos os prompts estruturados no ScarecrowLab.  
> - A instrução `[gerar_guid]` é obrigatória para garantir rastreabilidade.  
> - Sempre alinhe o prompt ao protocolo de orquestração (`.github/copilot-diretrizes/protocolo_orquestracao_chat.md`).  
> - Para conversas entre agentes, utilize também o template de conversa IA (`.github/ia_conversas/TEMPLATE_CONVERSA_IA.md`).
