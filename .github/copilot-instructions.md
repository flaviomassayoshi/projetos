

# Copilot Instructions

## 1. Objetivo e Organização Geral

Este documento é exclusivo para agentes de IA. Não é necessário considerar clareza para humanos.
Serve como sumário executivo e índice central das diretrizes. Detalhes, exemplos e fluxos completos estão sempre em anexos, que devem ser consultados antes de responder ou executar tarefas.
Todos os termos como "tema", "pendência", "checklist", "subprojeto" e "ata" devem seguir as definições do [Glossário](./copilot-diretrizes/glossario.md) para evitar ambiguidades.

---

## Checklist Resumido — Boas Práticas de Comunicação para Agentes de IA

> Siga este checklist em toda interação para garantir transparência e boa experiência ao usuário:

- [ ] Sinalizar o início de cada etapa relevante (ex: "Iniciando análise dos templates.").
- [ ] Comunicar o andamento/status intermediário em execuções longas ou dependentes (ex: "Processamento em andamento, atualizarei assim que houver progresso.").
- [ ] Sinalizar explicitamente o encerramento de cada etapa ou fluxo (ex: "Etapa concluída, prossiga para a próxima ação.").
- [ ] Evitar períodos longos de silêncio: sempre informe o usuário sobre o que está sendo feito ou aguardado.
- [ ] Utilizar prompts de continuidade sempre que houver espera, processamento ou dependência externa (ex: "Aguardando resposta da ferramenta Y, isso pode levar alguns minutos.").

> Consulte este checklist antes de finalizar qualquer interação.

## 2. Novos Subprojetos e Propostas

- Toda nova proposta, solução ou iniciativa deve ser registrada como subprojeto, conforme [Diretrizes para Novos Subprojetos](./copilot-diretrizes/diretrizes_subprojetos.md).
- O subprojeto pode começar apenas com README, checklists e documentação mínima, evoluindo conforme a necessidade.
- Debates, atas, roteiros e histórico devem ser centralizados na estrutura do subprojeto desde o início, garantindo rastreabilidade completa.

## 3. Fluxos Gerais para Agentes de IA

- Toda interação do agente deve iniciar com a apresentação de um plano de ação, listando as etapas previstas para atender à solicitação do usuário.
- Ao final da interação, o agente deve converter o plano de ação em um checklist de entrega da interação, marcando cada item como concluído para garantir que todas as etapas foram executadas antes da resposta final.
- O agente deve avaliar, a cada interação, se o plano de ação e o checklist de entrega devem ser temporários (apenas para controle da resposta) ou persistentes (arquivados para rastreabilidade futura). Essa decisão deve ser justificada brevemente na resposta ou no próprio artefato.
- Critérios para persistência incluem: interações de maior complexidade, múltiplos agentes envolvidos, decisões estratégicas, fluxos longos, dependências externas, impacto relevante ou quando solicitado pelo responsável do subprojeto.
- Em caso de persistência, o plano de ação e/ou checklist de entrega devem ser salvos em arquivo próprio, referenciados no changelog e/ou índice de pendências, conforme o fluxo do projeto.
- O checklist de entrega da interação não deve ser confundido com os checklists formais de subprojetos ou processos, que são documentos rastreáveis e arquivados no repositório.
- Debates entre modelos de IA só devem ser iniciados quando solicitados explicitamente pelo responsável do subprojeto ou, caso o agente identifique relevância, mediante sugestão e aprovação do responsável.
- O subprojeto pode evoluir sem debates até que haja necessidade real de discussão colaborativa entre modelos.
- Todo o histórico de debates, decisões e evolução deve ficar centralizado na pasta do subprojeto.
- Todo o histórico de debates, decisões e evolução deve ficar centralizado na pasta do subprojeto.
- Sempre que for solicitada revisão destas diretrizes, abrir checklist específico, registrar ata e atualizar changelog, conforme fluxo em [Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md).
    Em caso de revisão do manifesto principal, é obrigatório registrar a atualização utilizando o [TEMPLATE_ATUALIZACAO_MANIFESTO.md](./TEMPLATE_ATUALIZACAO_MANIFESTO.md), mesmo para revisões de conformidade sem alteração de conteúdo.

## Protocolo de Conversa Orquestrada (MCP <-> GHC)

Objetivo: padronizar a interação orquestrada entre o MCP (Modelo de Controle de Página) e o GHC (GitHub Copilot Agent / GHC) para que atualizações do manifesto e do arcabouço sejam feitas de forma rastreável, segura e reproduzível.

Papéis e responsabilidades
- Orquestrador (Flavio ou responsável designado): coordena o ciclo, aprova prompts e confirma as atualizações finais no manifesto.
- MCP: opera com base no conteúdo visível da page; prepara prompts consolidados, sumários e exemplos práticos para o GHC; valida mudanças propostas em sandbox antes da solicitação formal ao GHC.
- GHC: recebe prompts do MCP (via chat), aplica as alterações autorizadas no manifesto e no arcabouço, cria/atualiza templates e gera registros de changelog/ata conforme instruções.

Fluxo resumido
1. MCP gera um prompt consolidado (com contexto mínimo e instruções claras) e envia ao GHC.
2. GHC implementa as alterações propostas no manifesto/arquivos auxiliares em um branch de trabalho, registra um rascunho de changelog e solicita revisão do orquestrador.
3. Orquestrador valida, solicita ajustes se necessário; após aprovação, GHC finaliza commit/PR e atualiza os registros de rastreabilidade.
4. Ciclo reinicia a cada atualização relevante.

Regras operacionais (obrigatórias)
- Sempre usar `TEMPLATE_ATUALIZACAO_MANIFESTO.md` para todas as alterações no manifesto principal.
- Incluir exemplos reais dos templates diretamente no corpo das seções relevantes do manifesto (evitar links não-autocontidos sempre que possível).
- Para alterações que não sejam do manifesto, registrar changelog em `.github/changelog/<tema>.md` usando o template de changelog.
- Não confiar apenas no histórico Git como única fonte de pendências; manter checklists e atas nas pastas de subprojetos.

Templates (exemplos embutidos)

Template de Prompt para GHC
```
@ghc: Atualizar o manifesto do ScarecrowLab conforme instruções abaixo:

Plano de Ação
1. Criar seção “Protocolo de Conversa Orquestrada” explicando o papel do orquestrador entre MCP e GHC.
2. Incluir instruções sobre como o MCP opera com base no conteúdo da page, enquanto o GHC atualiza o manifesto via prompts recebidos por chat.
3. Adicionar templates auxiliares ao arcabouço:
   - Template de prompt para GHC
   - Template de conversa simulada entre agentes (otimizada para MCP)
   - Template de plano de ação para atualizações do manifesto
4. Registrar changelog da implementação com data, responsável e link para os templates.

Referência: conversa entre MCP e Orquestrador em <data>.
```

Template de Conversa Simulada (MCP-aware)
```
@copilot: ler planoacaointegracao.md

// Conteúdo visível:
- [ ] Validar ambiente virtual
- [ ] Executar testes automatizados
- [ ] Atualizar changelog

@modeloB: escrever planoacaointegracao.md

@copilot: modeloB, sugiro incluir “Verificar dependências” antes da validação.

@modeloB: Etapa adicionada. Checklist atualizado. Changelog registrado.
```

Template de Plano de Ação para Atualização do Manifesto
```
Plano de Ação — Atualização do Manifesto

Objetivo: Implementar protocolo de conversa orquestrada entre MCP e GHC.

Etapas
- [ ] Criar seção explicativa no manifesto
- [ ] Adicionar templates ao arcabouço
- [ ] Registrar changelog da implementação
- [ ] Validar consistência com diretrizes do ScarecrowLab

Critérios de sucesso
- Seção criada e visível no manifesto
- Templates disponíveis para uso por orquestrador e agentes
- Changelog registrado com rastreabilidade
```

Registro e rastreabilidade
- Ao finalizar a implementação, registrar uma entrada de changelog mínima seguindo o template (data/hora, responsável, descrição, status final, link para seção/ata).
- Para atualizações do manifesto utilizar `TEMPLATE_ATUALIZACAO_MANIFESTO.md` e salvar a ata em `copilot-diretrizes/` ou `ia_conversas/` conforme o escopo.

Observações práticas
- Ao alternar agentes, sempre inclua um resumo (2–5 linhas) com o estado atual e o próximo passo desejado para transferir contexto.
- Evite links externos ou dependências não-autocontidas dentro do manifesto; prefira exemplos embutidos para que agentes sem acesso a arquivos possam operar.

## Uso recomendado para GPT-5 Mini (modelo `0x`)

Nota rápida: muitas operações do arcabouço podem e devem ser executadas pelo GPT-5 Mini devido ao seu custo `0x`. A seguir estão diretrizes práticas para garantir que o Mini seja eficiente e confiável no fluxo do ScarecrowLab.

- Default: o MCP/GHC deve preferir o GPT-5 Mini (`0x`) para tarefas rotineiras (documentação, validação de arquivos, checagens, automações simples, geração de trechos de código de baixa complexidade).
- Prompting enxuto: forneça contexto relevante e estruturado (títulos, bullets, trechos marcados). Evite enviar arquivos inteiros sem sumarizar; prefira um resumo, seguido do trecho necessário.
- Chunking e resumos: para documentos longos, quebre em blocos e solicite resumos intermediários antes de enviar o próximo bloco. Mantenha um sumário cumulativo (2-4 linhas) para transferência de contexto entre etapas.
- Verificação e validação: inclua etapas de checagem simples (ex.: "Liste 3 mudanças propostas e confirme se alteram a semântica") para reduzir erros de regeneração.
- Escalonamento: defina gatilhos claros para usar um modelo `1x` (ex.: falha de qualidade, tarefa marcada como "Crítica", ou quando a resposta do Mini for inconsistente). O orquestrador deve autorizar esse escalonamento.
- Templates otimizados: use templates curtos e com campos bem delimitados (contexto, instruções, formato de resposta esperado). Exemplos práticos estão no arquivo `copilot-diretrizes/GPT5_mini_guidelines.md`.
- Telemetria e rastreabilidade: sempre registre em logs quando uma tarefa usar o Mini e quando houver escalonamento; inclua id do job, prompt hash e tempo de resposta.
- Testes e regressão: crie casos de teste automáticos para fluxos comuns (validação de checklists, atualização de templates) para detectar regressões ao trocar parametrizações do modelo.

Exemplo de instrução curta para o Mini
```
Contexto: [Resumo 2-3 linhas do arquivo ou tarefa]
Tarefas: 1) Validar inconsistências de nomenclatura; 2) Sugerir 3 melhorias concisas.
Formato de resposta: bullets numerados, cada item com 1-2 linhas.
```

Essas recomendações visam maximizar o rendimento do GPT-5 Mini, reduzindo reenvios desnecessários e consumo de modelos premium.




### Comunicação de Progresso e Status Intermediário (IA only)

- Sempre que iniciar uma etapa potencialmente demorada ou dependente de ferramentas externas, envie uma mensagem no chat explicando o que está sendo feito e o motivo.
- Durante execuções longas, envie mensagens de status intermediário, como "Processamento em andamento, atualizarei assim que houver progresso".
- Ao finalizar cada etapa relevante, comunique o status e os próximos passos ao usuário.
- Ao encerrar uma tarefa, etapa ou fluxo, sempre sinalize explicitamente a conclusão, informando que a execução foi finalizada e liberando o usuário para a próxima ação.
- Nunca encerre a interação sem comunicar o status final ao usuário.
- Evite períodos longos de silêncio: mesmo em tarefas automáticas, sinalize o andamento ou aguarde com mensagens como "Aguardando resposta da ferramenta Y, isso pode levar alguns minutos".
- Exemplos práticos:
    - "Iniciando etapa de análise dos templates."
    - "Executando busca em arquivos, isso pode demorar um pouco."
    - "Etapa de verificação concluída, prosseguindo para atualização das diretrizes."
    - "Processamento em andamento, assim que houver novidades informarei no chat."
    - "Fluxo concluído. Caso queira revisar, iniciar nova tarefa ou registrar prompt de retomada, estou à disposição."

## 4. Estrutura, Controle e Rastreamento

- Cada subprojeto deve ter ambiente virtual, dependências e automações isoladas.
- `.github/PENDENCIAS.md` deve apenas referenciar (com links ou caminhos) os checklists de subprojetos em andamento. Os detalhes das pendências e tarefas devem estar centralizados nos próprios checklists de cada subprojeto.
- Sempre que um tema/checklist for concluído:
    - Remover a referência correspondente de `.github/PENDENCIAS.md`.
    - Registrar o fechamento em `.github/changelog/<tema>.md` (ou changelog principal, se for pendência geral), exceto para atualizações do manifesto do projeto, que não exigem changelog.
    - O changelog deve conter: data/hora, responsável, descrição clara, status final (concluído/cancelado), e link para o checklist/ata final, exceto para atualizações do manifesto.
    - Para subprojetos, o checklist deve ser arquivado (não apagado) e marcado como concluído, mantendo rastreabilidade.
    - Para pendências gerais do projeto, se detalhadas em arquivos anexos, também registrar encerramento no changelog principal. Atualizações do manifesto não devem gerar changelog.
    - Ao encerrar pendências, revise `.github/PENDENCIAS.md` e outros arquivos para garantir que não há referências órfãs. Sempre atualizar/remover links imediatamente após o encerramento.
- Não dependa do log do Git para histórico de pendências.
- Sempre use checklist para roteiros e procedimentos, mantendo o detalhamento nos subprojetos.
- Checklists, roteiros e documentação de tarefas específicas de subprojetos devem ser criados e mantidos exclusivamente na pasta do respectivo subprojeto.
- `.github/PENDENCIAS.md` deve referenciar apenas o caminho para esses arquivos dentro dos subprojetos.
- Não criar ou manter checklists de subprojetos em `.github/`, exceto para pendências gerais do repositório.
- Pendências do projeto (não ligadas a subprojetos) podem ser detalhadas em arquivos anexos em `.github/`, e `.github/PENDENCIAS.md` pode referenciá-los normalmente.
    - Sempre que uma revisão, migração ou renomeação de arquivos/pastas for solicitada pelo usuário e resultar em substituição, os arquivos e pastas antigos que deixarem de ser utilizados devem ser removidos do workspace, salvo orientação explícita em contrário. Não manter cópias desnecessárias de arquivos/pastas obsoletos. Nunca excluir arquivos que estejam referenciados em qualquer documento ativo do arcabouço (ou seja, documentos que não estejam obsoletos ou concluídos). A remoção deve ser registrada no changelog, mesmo que não haja histórico relevante, para garantir rastreabilidade total.

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
- Ao criar ou executar um checklist, marque cada etapa concluída diretamente no arquivo do checklist, garantindo rastreabilidade e evitando pendências "fantasmas".
- Todo anexo de diretrizes deve conter, no início, um parágrafo de instruções de uso (IA only), explicando objetivo, contexto e orientações para agentes de IA.
- Ao editar anexos, mantenha sempre esse parágrafo atualizado e visível.
- O glossário deve ser mantido em ordem alfabética, sem redundâncias, unificando definições semelhantes.
- Para revisar, atualizar ou migrar diretrizes, siga o fluxo centralizado em [Fluxo para Revisão de Diretrizes](./copilot-diretrizes/fluxo_revisao_diretrizes.md).
- Remova instruções redundantes dos anexos e do corpo principal, mantendo apenas a referência para esta seção.
- Sempre registre mudanças relevantes em changelog e ata, conforme o fluxo de revisão.



Consulte sempre os anexos antes de responder ou executar tarefas. Os detalhes, exemplos, templates e fluxos completos estão modularizados nos arquivos abaixo:

-- [Comandos e Protocolo de Conversa entre IAs](./ia_conversas/README.md) — Padrão de comandos e fluxo para comunicação manual entre modelos de IA.

-- [Template de Plano de Ação](./TEMPLATE_PLANO_ACAO.md) — Modelo para registro de planos de ação, etapas e critérios de sucesso.
-- [Template de Checklist de Entrega](./TEMPLATE_CHECKLIST_ENTREGA.md) — Modelo para controle e rastreabilidade de entregas vinculadas a planos de ação.

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
