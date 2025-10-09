
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





# Blocos Funcionais de Artefatos do Arcabouço

## .github/copilot-diretrizes/glossario.md
Resumo: Definições e siglas essenciais para agentes MCP/GHC.
Exemplo sintético:
- MCP: Microsoft Copilot
- Checklist: Lista de tarefas
- Changelog: Registro de alterações

## .github/copilot-diretrizes/checklist_comunicacao.md
Resumo: Critérios mínimos para comunicação entre agentes MCP e GHC.
Checklist:
- [ ] Mensagem clara
- [ ] Referência ao template
- [ ] Validação pelo orquestrador

## .github/copilot-diretrizes/fluxos_gerais_agentes.md
Resumo: Fluxo padrão de execução para agentes de IA.
Exemplo:
1. Apresentar plano de ação
2. Executar etapas
3. Converter em checklist

## .github/copilot-diretrizes/diretrizes_subprojetos.md
Resumo: Regras para criação e organização de subprojetos.
Exemplo:
- Nova proposta = nova pasta
- Usar TEMPLATE_SUBPROJETO.md

## .github/copilot-diretrizes/protocolo_orquestracao_chat.md
Resumo: Protocolo para prompts e orquestração MCP <-> GHC.
Exemplo:
@ghc: executar plano de ação
Contexto: resumo objetivo
Tarefas: lista numerada

## .github/copilot-diretrizes/fluxos_encerramento.md
Resumo: Fluxos de encerramento, changelog e prompt de retomada.
Exemplo de changelog:
- Data/hora: 2025-10-08
- Responsável: GitHub Copilot
- Descrição: Checklist X concluído

## .github/copilot-diretrizes/instrucoes_setup_CI.md
Resumo: Setup de ambiente, CI e automações para agentes de IA.
Exemplo:
- Consultar/atualizar .github/PENDENCIAS.md
- Executar comandos de setup

## .github/copilot-diretrizes/fluxo_revisao_diretrizes.md
Resumo: Processo padronizado de revisão e atualização das diretrizes.
Exemplo:
1. Abrir checklist de revisão
2. Registrar atualização via TEMPLATE_ATUALIZACAO_MANIFESTO.md

## .github/copilot-diretrizes/templates_index.md
Resumo: Índice central de templates e exemplos operacionais.
Exemplo:
- Template de Plano de Ação
- Template de Checklist de Entrega

## .github/copilot-diretrizes/checklists_praticos.md
Resumo: Exemplos práticos e templates de checklist.
Exemplo:
- [ ] Validar ambiente virtual
- [ ] Executar testes

## .github/copilot-diretrizes/diretrizes_tecnicas.md
Resumo: Diretrizes técnicas para ambiente local e escolha de modelos de IA.
Exemplo:
- Python 3.10.11
- Usar modelo 0x para rotina

## .github/copilot-diretrizes/convenções_codigo.md
Resumo: Convenções de código para agentes de IA.
Exemplo:
- snake_case para funções
- PascalCase para classes

## .github/copilot-diretrizes/projetos_terceiros.md
Resumo: Regras para projetos de terceiros e customizações.
Exemplo:
- Não inicializar Git em clonado
- Customizações em pasta separada

## .github/copilot-diretrizes/diretrizes_execucao_venv_windows.md
Resumo: Execução de scripts e venv no Windows.
Exemplo:
- Ativar venv: .\venv\Scripts\Activate.ps1

## .github/copilot-diretrizes/diretrizes_debate.md
Resumo: Estrutura e fluxo para rodadas de debate entre IAs.
Exemplo:
| Item | Proposta | Justificativa |
|------|----------|---------------|
| 1    | ...      | ...           |

## .github/ia_conversas/README.md
Resumo: Manual para conversas entre IAs, comandos e histórico.
Exemplo:
@copilot: ler conversa_modeloA_modeloB.md
@modeloB: escrever conversa_modeloA_modeloB.md

## .github/copilot-diretrizes/manual_redacao_mcp.md
Resumo: Manual minimificado para padronizar a redação do manifesto e artefatos, otimizando a atuação do MCP.
Exemplo:
- Usar títulos hierárquicos
- Blocos padronizados por artefato
- Glossário sintético
