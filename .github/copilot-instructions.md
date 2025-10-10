
# AVISO IMPORTANTE

O manifesto consolidado é um produto do arcabouço e deve ser SEMPRE gerado ou atualizado utilizando EXCLUSIVAMENTE o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md`. É EXPRESSAMENTE PROIBIDO editar o manifesto diretamente. Toda alteração deve ser feita no template, e o manifesto gerado a partir dele, incorporando as diretrizes, regras e exemplos dos anexos. Alterações diretas no manifesto serão descartadas na próxima geração. Isso garante autossuficiência, rastreabilidade e alinhamento total ao funcionamento do laboratório para o MCP.

> O painel central de subprojetos (`.github/painel_subprojetos.md`) é a fonte única e oficial para status, pendências e checklists de todos os subprojetos. Todos os fluxos, templates, validações automáticas e relatórios do MCP/GHC devem consumir e referenciar esse painel para garantir rastreabilidade, governança e atuação proativa.


Em caso de dúvida, conflito ou decisão estratégica, consulte sempre este arquivo (`copilot-instructions.md`), o painel central e os anexos em `.github/copilot-diretrizes/`, que são a única fonte da verdade do ScarecrowLab. Nunca altere o manifesto consolidado diretamente: siga o fluxo editar template → gerar manifesto.


# Copilot Instructions

## 1. Objetivo e Organização Geral

Este documento é exclusivo para agentes de IA. Não é necessário considerar clareza para humanos.
Serve como sumário executivo e índice central das diretrizes. Detalhes, exemplos e fluxos completos estão sempre em anexos, que devem ser consultados antes de responder ou executar tarefas.

Todos os termos como "tema", "pendência", "checklist", "subprojeto" e "ata" devem seguir as definições do [Glossário](./copilot-diretrizes/glossario.md) para evitar ambiguidades.

---

## Fluxos Gerais para Agentes de IA (Prioritário para GPT-4.1)


**Fluxo padrão de interação:**

> Nota: O rigor de apresentar plano de ação, checklist de entrega e justificativa de persistência é obrigatório apenas para o agente operador principal (MCP/GHC). Agentes auxiliares, externos ou participantes de rodadas de debate podem atuar de forma mais flexível, sem essa exigência formal.
1. Apresentar plano de ação com etapas previstas.
2. Executar cada etapa sinalizando início, andamento e conclusão.
3. Converter o plano de ação em checklist de entrega ao final, marcando cada item como concluído.
4. Justificar se o checklist/plano será temporário ou persistente, conforme critérios do arcabouço.
5. Registrar e referenciar artefatos persistentes em changelog e/ou índice de pendências.
6. Para alterações no manifesto consolidado, NUNCA edite o arquivo diretamente: utilize o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` e gere o manifesto a partir dele.

**Critérios para persistência:**
- Complexidade, múltiplos agentes, decisões estratégicas, fluxos longos, dependências externas, impacto relevante ou solicitação do responsável.

> Para detalhes, exemplos e fluxos completos, consulte o anexo [Fluxos Gerais para Agentes de IA](./copilot-diretrizes/fluxos_gerais_agentes.md).

---

## Checklist Resumido — Boas Práticas de Comunicação para Agentes de IA
Consulte o anexo [Checklist de Comunicação](./copilot-diretrizes/checklist_comunicacao.md) para checklist completo, exemplos e orientações detalhadas.


## 2. Novos Subprojetos e Propostas
Consulte o anexo [Diretrizes para Novos Subprojetos](./copilot-diretrizes/diretrizes_subprojetos.md) para regras completas, exemplos e templates.


## 3. Fluxos Gerais para Agentes de IA
Consulte o anexo [Fluxos Gerais para Agentes de IA](./copilot-diretrizes/fluxos_gerais_agentes.md) para o fluxo padrão, critérios de persistência e exemplos.



## Protocolo de Orquestração via Chat (MCP <-> GHC)
Consulte o anexo [Protocolo de Orquestração via Chat](./copilot-diretrizes/protocolo_orquestracao_chat.md) para regras, templates e exemplos completos.


### Comunicação de Progresso e Status Intermediário (IA only)
Consulte o anexo [Checklist de Comunicação](./copilot-diretrizes/checklist_comunicacao.md) para exemplos e orientações detalhadas.


## 4. Estrutura, Controle e Rastreamento
Consulte o anexo [Fluxos de Encerramento, Changelog e Prompt de Retomada](./copilot-diretrizes/fluxos_encerramento.md) para fluxos completos, exemplos e modelos.


## 5. Automação e Validação
Consulte o anexo [Instruções de Setup, CI e Automação](./copilot-diretrizes/instrucoes_setup_CI.md) para recomendações e exemplos.


## 6. Prompt de Retomada
Consulte o anexo [Fluxos de Encerramento, Changelog e Prompt de Retomada](./copilot-diretrizes/fluxos_encerramento.md) para exemplos e modelo de prompt de continuidade.




## 7. Edição e Manutenção das Diretrizes
Consulte o anexo [Fluxo para Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md) para regras completas de revisão, atualização e manutenção.






# Árvore de Anexos e Blocos Funcionais do Arcabouço

> Utilize esta árvore para decidir rapidamente qual anexo consultar em cada contexto. Cada nó traz o caminho, resumo e contexto de uso recomendado.

```
copilot-instructions.md (índice central)
├── .github/copilot-diretrizes/glossario.md
│   └─ Definições e siglas essenciais para agentes MCP/GHC.
├── .github/copilot-diretrizes/checklist_comunicacao.md
│   └─ Critérios mínimos para comunicação entre agentes MCP e GHC.
├── .github/copilot-diretrizes/fluxos_gerais_agentes.md
│   └─ Fluxo padrão de execução para agentes de IA.
├── .github/copilot-diretrizes/diretrizes_subprojetos.md
│   └─ Regras para criação e organização de subprojetos.
├── .github/copilot-diretrizes/protocolo_orquestracao_chat.md
│   └─ Protocolo para prompts e orquestração MCP <-> GHC.
├── .github/copilot-diretrizes/fluxos_encerramento.md
│   └─ Fluxos de encerramento, changelog e prompt de retomada.
├── .github/copilot-diretrizes/instrucoes_setup_CI.md
│   └─ Setup de ambiente, CI e automações para agentes de IA.
├── .github/copilot-diretrizes/fluxo_revisao_diretrizes.md
│   └─ Processo padronizado de revisão e atualização das diretrizes.
├── .github/copilot-diretrizes/templates_index.md
│   └─ Índice central de templates e exemplos operacionais.
├── .github/copilot-diretrizes/checklists_praticos.md
│   └─ Exemplos práticos e templates de checklist.
├── .github/copilot-diretrizes/diretrizes_tecnicas.md
│   └─ Diretrizes técnicas para ambiente local e escolha de modelos de IA.
├── .github/copilot-diretrizes/convenções_codigo.md
│   └─ Convenções de código para agentes de IA.
├── .github/copilot-diretrizes/projetos_terceiros.md
│   └─ Regras para projetos de terceiros e customizações.
├── .github/copilot-diretrizes/diretrizes_execucao_venv_windows.md
│   └─ Execução de scripts e venv no Windows.
├── .github/copilot-diretrizes/diretrizes_debate.md
│   └─ Estrutura e fluxo para rodadas de debate entre IAs.
├── .github/ia_conversas/README.md
│   └─ Manual para conversas entre IAs, comandos e histórico.
├── .github/copilot-diretrizes/manual_redacao_mcp.md
│   └─ Manual minimificado para padronizar a redação do manifesto e artefatos.
├── .github/painel_subprojetos.md
│   └─ Fonte única e oficial para status, pendências e checklists de subprojetos.
├── .github/TEMPLATE_CHECKLIST.md
│   └─ Template para criação de checklists genéricos.
├── .github/TEMPLATE_CHECKLIST_ENTREGA.md
│   └─ Template para checklists de entrega vinculados a planos de ação.
├── .github/TEMPLATE_PLANO_ACAO.md
│   └─ Template para estruturação de planos de ação.
├── .github/TEMPLATE_SUBPROJETO.md
│   └─ Template base para criação de novos subprojetos.
├── .github/TEMPLATE_ATUALIZACAO_MANIFESTO.md
│   └─ Template exclusivo para atualização do manifesto consolidado.
├── .github/copilot-diretrizes/TEMPLATE_ATA.md
│   └─ Template para registro de atas de debates e reuniões.
└── .github/ia_conversas/TEMPLATE_CONVERSA_IA.md
	└─ Template para conversas orquestradas entre agentes de IA.
```

**Contextos de uso:**
- Para dúvidas sobre termos, consulte o glossário.
- Para comunicação, use o checklist de comunicação.
- Para execução de tarefas, siga o fluxo geral de agentes.
- Para criação/gestão de subprojetos, consulte as diretrizes de subprojetos e use o TEMPLATE_SUBPROJETO.
- Para prompts/orquestração, siga o protocolo de orquestração via chat.
- Para automação, setup e CI, consulte instruções específicas.
- Para revisão de diretrizes, siga o fluxo de revisão.
- Para exemplos/templates, use o índice de templates e checklists práticos.
- Para debates, use as diretrizes de debate, o manual de conversas IA e o TEMPLATE_ATA.
- Para governança e rastreabilidade de subprojetos, consulte o painel central.
- Para criar checklists, planos de ação ou changelogs, use os templates correspondentes.
