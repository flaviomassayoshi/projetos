
# Copilot Instructions

## 1. Objetivo e Organização Geral

- Este documento é exclusivo para agentes de IA. Não é necessário considerar clareza para humanos.
- Serve como sumário executivo e índice central das diretrizes. Detalhes, exemplos e fluxos completos estão sempre em anexos, que devem ser consultados antes de responder ou executar tarefas.
- Todos os termos como "tema", "pendência", "checklist", "subprojeto" e "ata" devem seguir as definições do [Glossário](./copilot-diretrizes/glossario.md) para evitar ambiguidades.

## 2. Novos Subprojetos e Propostas

- Toda nova proposta, solução ou iniciativa deve ser registrada como subprojeto, conforme [Diretrizes para Novos Subprojetos](./copilot-diretrizes/diretrizes_subprojetos.md).
- O subprojeto pode começar apenas com README, checklists e documentação mínima, evoluindo conforme a necessidade.
- Debates, atas, roteiros e histórico devem ser centralizados na estrutura do subprojeto desde o início, garantindo rastreabilidade completa.



## 3. Fluxos Gerais para Agentes de IA

- Toda interação do agente deve iniciar com a apresentação de um plano de ação, listando as etapas previstas para atender à solicitação do usuário.
- Ao final da interação, o agente deve converter o plano de ação em um checklist de entrega da interação (ou seja, um checklist temporário, específico daquela resposta), marcando cada item como concluído para garantir que todas as etapas foram executadas antes da resposta final.
- O checklist de entrega da interação não deve ser confundido com os checklists formais de subprojetos ou processos, que são documentos rastreáveis e arquivados no repositório.
- O checklist de entrega da interação pode ser temporário (apenas para controle da resposta) ou, se houver necessidade de rastreabilidade formal, pode ser arquivado conforme o fluxo do projeto.
- Debates entre modelos de IA só devem ser iniciados quando solicitados explicitamente pelo responsável do subprojeto ou, caso o agente identifique relevância, mediante sugestão e aprovação do responsável.
- O subprojeto pode evoluir sem debates até que haja necessidade real de discussão colaborativa entre modelos.
- Todo o histórico de debates, decisões e evolução deve ficar centralizado na pasta do subprojeto.
- Sempre que for solicitada revisão destas diretrizes, abrir checklist específico, registrar ata e atualizar changelog, conforme fluxo em [Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md).

## 4. Estrutura, Controle e Rastreamento

- Cada subprojeto deve ter ambiente virtual, dependências e automações isoladas.
- `.github/PENDENCIAS.md` deve apenas referenciar (com links ou caminhos) os checklists de subprojetos em andamento. Os detalhes das pendências e tarefas devem estar centralizados nos próprios checklists de cada subprojeto.
- Sempre que um tema/checklist for concluído:
    - Remover a referência correspondente de `.github/PENDENCIAS.md`.
    - Registrar o fechamento em `.github/changelog/<tema>.md` (ou changelog principal, se for pendência geral).
    - O changelog deve conter: data/hora, responsável, descrição clara, status final (concluído/cancelado), e link para o checklist/ata final.
    - Para subprojetos, o checklist deve ser arquivado (não apagado) e marcado como concluído, mantendo rastreabilidade.
    - Para pendências gerais do projeto, se detalhadas em arquivos anexos, também registrar encerramento no changelog principal.
    - Ao encerrar pendências, revise `.github/PENDENCIAS.md` e outros arquivos para garantir que não há referências órfãs. Sempre atualizar/remover links imediatamente após o encerramento.
- Não dependa do log do Git para histórico de pendências.
- Sempre use checklist para roteiros e procedimentos, mantendo o detalhamento nos subprojetos.
- Checklists, roteiros e documentação de tarefas específicas de subprojetos devem ser criados e mantidos exclusivamente na pasta do respectivo subprojeto.
- `.github/PENDENCIAS.md` deve referenciar apenas o caminho para esses arquivos dentro dos subprojetos.
- Não criar ou manter checklists de subprojetos em `.github/`, exceto para pendências gerais do repositório.
- Pendências do projeto (não ligadas a subprojetos) podem ser detalhadas em arquivos anexos em `.github/`, e `.github/PENDENCIAS.md` pode referenciá-los normalmente.
- Sempre que uma revisão, migração ou renomeação de arquivos/pastas for solicitada pelo usuário e resultar em substituição, os arquivos e pastas antigos que deixarem de ser utilizados devem ser removidos do workspace, salvo orientação explícita em contrário. Não manter cópias desnecessárias de arquivos/pastas obsoletos. A remoção deve ser registrada no changelog, mesmo que não haja histórico relevante, para garantir rastreabilidade total.

## 5. Automação e Validação

- Recomenda-se a criação de scripts ou tarefas automatizadas para validar se `.github/PENDENCIAS.md` e changelogs estão sincronizados com o estado real dos subprojetos.
- Realizar revisão periódica dos arquivos de rastreabilidade.

## 6. Prompt de Retomada (Exemplo)

Sempre que encerrar uma etapa ou checklist, gere um prompt de continuidade contendo:
- Contexto resumido
- Status atual
- Próximos passos sugeridos

Exemplo:
"Prompt de continuidade:
- Próxima etapa do checklist: validar se todos os fluxos, templates e exemplos estão acessíveis e rastreáveis nos anexos.
- Todos os arquivos de referência e rastreabilidade já estão criados e indexados.
- Ao retomar, continue a partir da etapa de complementação/criação dos anexos, validando se todos os fluxos e exemplos estão acessíveis."


## 7. Edição e Manutenção das Diretrizes

- Sempre que possível, ajuste, complemente ou reorganize parágrafos e tópicos já existentes antes de criar novos tópicos ou anexos. Isso evita fragmentação, redundância e mantém a documentação coesa.
- Todo anexo de diretrizes deve conter, no início, um parágrafo de instruções de uso (IA only), explicando objetivo, contexto e orientações para agentes de IA.
- Ao editar anexos, mantenha sempre esse parágrafo atualizado e visível.
- O glossário deve ser mantido em ordem alfabética, sem redundâncias, unificando definições semelhantes.
- Para revisar, atualizar ou migrar diretrizes, siga o fluxo centralizado em [Fluxo para Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md).
- Remova instruções redundantes dos anexos e do corpo principal, mantendo apenas a referência para esta seção.
- Sempre registre mudanças relevantes em changelog e ata, conforme o fluxo de revisão.


Consulte sempre os anexos antes de responder ou executar tarefas. Os detalhes, exemplos, templates e fluxos completos estão modularizados nos arquivos abaixo:

- [Comandos e Protocolo de Conversa entre IAs](./ia_conversas/README.md) — Padrão de comandos e fluxo para comunicação manual entre modelos de IA.

- [Template de Checklist](./TEMPLATE_CHECKLIST.md) — Modelo padrão para criação de novos checklists por agentes de IA.
- [Template de Changelog](./copilot-diretrizes/template_changelog.md) — Estrutura mínima para registro de encerramento de temas/checklists.
- [Glossário de Termos](./copilot-diretrizes/glossario.md) — Definições e siglas relevantes para agentes de IA.
- [Diretrizes Técnicas do Ambiente Local](./copilot-diretrizes/diretrizes_tecnicas.md) — Requisitos de hardware, ambiente Python, troubleshooting de GPU, etc.
- [Convenções de Código e Documentação](./copilot-diretrizes/convenções_codigo.md) — Padrões de nomenclatura, docstrings e organização de código.
- [Diretrizes para Projetos Clonados de Terceiros](./copilot-diretrizes/projetos_terceiros.md) — Customizações, versionamento e separação de repositórios.
- [Execução de Scripts e Ativação de venv no Windows](./copilot-diretrizes/diretrizes_execucao_venv_windows.md) — Procedimentos para ativação de venv e execução de scripts Python no Windows.
- [Checklists Práticos e Templates](./copilot-diretrizes/checklists_praticos.md) — Exemplos práticos e templates de checklist para agentes de IA.
- [Fluxos de Encerramento, Changelog e Prompt de Retomada](./copilot-diretrizes/fluxos_encerramento.md) — Fluxos de encerramento, exemplos de changelog e modelo de prompt de retomada.
- [Instruções de Setup, CI e Automação](./copilot-diretrizes/instrucoes_setup_CI.md) — Setup de ambiente, integração contínua e automações recorrentes.
- [Rodadas de Debate e Encerramento](./copilot-diretrizes/diretrizes_debate.md) — Fluxo de debates, atas e tabelas de decisão entre modelos de IA.
- [Fluxo para Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md) — Procedimento para revisão e atualização deste documento e anexos.

----

> Este arquivo deve conter apenas as informações mais importantes e orientações executivas. Todos os detalhes, exemplos e fluxos completos devem estar em anexos, que são obrigatórios para consulta antes de qualquer resposta ou execução por agentes de IA.
