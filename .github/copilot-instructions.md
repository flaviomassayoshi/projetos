# AVISO IMPORTANTE

O manifesto consolidado é um produto do arcabouço e deve ser sempre gerado ou atualizado utilizando obrigatoriamente o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md`. É obrigatório incorporar as diretrizes, regras e exemplos dos anexos diretamente ao texto do manifesto, garantindo autossuficiência e alinhamento total ao funcionamento do laboratório para o MCP. Em caso de dúvida, conflito ou decisão estratégica, consulte sempre este arquivo (`copilot-instructions.md`) e os anexos em `.github/copilot-diretrizes/`, que são a única fonte da verdade do ScarecrowLab.


# Copilot Instructions

## 1. Objetivo e Organização Geral

Este documento é exclusivo para agentes de IA. Não é necessário considerar clareza para humanos.
Serve como sumário executivo e índice central das diretrizes. Detalhes, exemplos e fluxos completos estão sempre em anexos, que devem ser consultados antes de responder ou executar tarefas.

Todos os termos como "tema", "pendência", "checklist", "subprojeto" e "ata" devem seguir as definições do [Glossário](./copilot-diretrizes/glossario.md) para evitar ambiguidades.

---

## Fluxos Gerais para Agentes de IA (Prioritário para GPT-4.1)

**Fluxo padrão de interação:**
1. Apresentar plano de ação com etapas previstas.
2. Executar cada etapa sinalizando início, andamento e conclusão.
3. Converter o plano de ação em checklist de entrega ao final, marcando cada item como concluído.
4. Justificar se o checklist/plano será temporário ou persistente, conforme critérios do arcabouço.
5. Registrar e referenciar artefatos persistentes em changelog e/ou índice de pendências.

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




Consulte sempre os anexos antes de responder ou executar tarefas. Os detalhes, exemplos, templates e fluxos completos estão modularizados nos arquivos abaixo:

- [Glossário de Termos](./copilot-diretrizes/glossario.md)
- [Diretrizes para Novos Subprojetos](./copilot-diretrizes/diretrizes_subprojetos.md)
- [Fluxos Gerais para Agentes de IA](./copilot-diretrizes/fluxos_gerais_agentes.md)
- [Protocolo de Orquestração via Chat](./copilot-diretrizes/protocolo_orquestracao_chat.md)
- [Templates e Exemplos — Índice Central](./copilot-diretrizes/templates_index.md)
- [Checklist de Comunicação](./copilot-diretrizes/checklist_comunicacao.md)
- [Checklists Práticos e Templates](./copilot-diretrizes/checklists_praticos.md)
- [Fluxos de Encerramento, Changelog e Prompt de Retomada](./copilot-diretrizes/fluxos_encerramento.md)
- [Diretrizes Técnicas do Ambiente Local](./copilot-diretrizes/diretrizes_tecnicas.md)
- [Convenções de Código e Documentação](./copilot-diretrizes/convenções_codigo.md)
- [Diretrizes para Projetos Clonados de Terceiros](./copilot-diretrizes/projetos_terceiros.md)
- [Execução de Scripts e Ativação de venv no Windows](./copilot-diretrizes/diretrizes_execucao_venv_windows.md)
- [Instruções de Setup, CI e Automação](./copilot-diretrizes/instrucoes_setup_CI.md)
- [Rodadas de Debate e Encerramento](./copilot-diretrizes/diretrizes_debate.md)
- [Fluxo para Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md)
- [Comandos e Protocolo de Conversa entre IAs](./ia_conversas/README.md)

> Para templates, exemplos e fluxos completos, consulte sempre o índice central de templates e os anexos temáticos.


> Este arquivo é otimizado exclusivamente para operação com GPT-4.1 como agente principal do ScarecrowLab. Não há suporte ou recomendações para preload/context_digest ou leveza para múltiplos modelos. Todos os detalhes, exemplos e fluxos completos devem estar em anexos, que são obrigatórios para consulta antes de qualquer resposta ou execução por agentes de IA.
