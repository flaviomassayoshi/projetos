# AVISO IMPORTANTE

Para instruções detalhadas de atualização, checklist MVP e critérios, consulte exclusivamente o template `.github/copilot-diretrizes/TEMPLATE_ATUALIZACAO_MANIFESTO.md` e o arcabouço em `.github/copilot-diretrizes/`. O manifesto consolidado não deve conter instruções operacionais ou fluxos de atualização: mantenha o foco em fluxos, exemplos, painéis e glossário.

# MANIFESTO CONSOLIDADO — SCARECROWLAB (MCP)

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
- .github/copilot-diretrizes/TEMPLATE_ATUALIZACAO_MANIFESTO.md
- .github/copilot-diretrizes/TEMPLATE_CHECKLIST.md
- .github/copilot-diretrizes/TEMPLATE_CHECKLIST_ENTREGA.md
- .github/copilot-diretrizes/TEMPLATE_PLANO_ACAO.md
- .github/copilot-diretrizes/TEMPLATE_SUBPROJETO.md
- .github/ia_conversas/TEMPLATE_CONVERSA_IA.md
- .github/painel_subprojetos.md
- python_apps/validacao_ia_multimodelo/README.md
- python_apps/validacao_ia_multimodelo/CHECKLIST.md
- python_apps/viabilizacao_debate_multimodelo/README.md
- python_apps/viabilizacao_debate_multimodelo/CHECKLIST.md
- python_apps/viabilizacao_debate_multimodelo/ATA_MIGRACAO_MANIFESTO.md

---

## Resumos Funcionais dos Anexos

### Diretrizes e Fluxos Globais
- **Glossário:** Termos essenciais: arcabouço (conjunto de diretrizes, templates e regras do laboratório), artefato persistente (documento ou registro obrigatório para rastreabilidade), checklist de entrega (lista de etapas executadas em uma interação), changelog (registro de alterações e decisões), MCP (Microsoft Copilot), GHC (GitHub Copilot Agent), painel central de subprojetos (fonte única de status e pendências), plano de ação (sequência de etapas para atingir um objetivo), prompt de retomada (mensagem de continuidade após uma etapa), subprojeto (iniciativa registrada com pasta própria).
- **Fluxo Geral de Agentes:** Todo agente deve apresentar um plano de ação com etapas previstas antes de executar tarefas. Cada etapa deve ser sinalizada (início, andamento, conclusão) e convertida em checklist de entrega ao final. Justifique se o checklist/plano será temporário ou persistente, conforme critérios do laboratório. Registre artefatos persistentes (checklist, changelog, ata) para rastreabilidade. Alterações no manifesto consolidado só podem ser feitas via template, nunca diretamente. Critérios para persistência: complexidade, múltiplos agentes, decisões estratégicas, fluxos longos, dependências externas, impacto relevante ou solicitação do responsável.
- **Checklist de Comunicação:** Sinalize início, andamento e encerramento de cada etapa relevante. Informe status intermediário em execuções longas ou dependentes. Evite períodos longos de silêncio: comunique sempre o que está sendo feito ou aguardado. Utilize prompts de continuidade sempre que houver espera, processamento ou dependência externa.
- **Fluxos de Encerramento, Changelog e Prompt de Retomada:** Ao encerrar uma pendência, registre o encerramento em changelog, com data, responsável, descrição e status final. Gere sempre um prompt de continuidade ao finalizar etapas, contendo contexto resumido, status e próximos passos sugeridos. Use o template de changelog para rastreabilidade e mantenha prompts de retomada claros para o MCP.
- **Diretrizes para Subprojetos:** Toda nova proposta ou solução deve ser registrada como subprojeto, com pasta dedicada e README inicial. Use o template de subprojeto para estrutura inicial. Centralize debates, atas e histórico na estrutura do subprojeto desde o início, garantindo rastreabilidade. O painel central de subprojetos é a fonte única para status, pendências e checklists.
- **Protocolo de Orquestração:** Toda recomendação do MCP só pode ser implementada pelo GHC após aprovação explícita do orquestrador humano. O fluxo de orquestração é sempre mediado por chat humano, nunca por comandos de arquivo. O MCP prepara prompts consolidados e exemplos práticos para o GHC, validando mudanças em sandbox antes da solicitação formal. O GHC aplica as alterações, registra changelog e solicita revisão do orquestrador. O orquestrador valida, solicita ajustes se necessário e aprova a finalização. Toda comunicação entre modelos deve ser mediada por chat humano/orquestrador, usando blocos markdown simples para artefatos. Utilize sempre o template de conversa IA e o protocolo de orquestração como fonte de verdade para prompts e fluxos.
- **Diretrizes Técnicas:** Siga as recomendações técnicas para ambiente local, escolha de modelos de IA e integração de agentes. Priorize compatibilidade, segurança e eficiência nos fluxos automatizados.
- **Convenções de Código:** Siga padrões de nomenclatura, indentação e organização definidos pelo laboratório. Utilize comentários claros e mantenha o código limpo e auditável.
- **Projetos de Terceiros:** Adote regras específicas para integração e customização de projetos de terceiros. Documente adaptações e mantenha rastreabilidade de alterações externas.
- **Execução de venv no Windows:** Siga as diretrizes para criação, ativação e uso de ambientes virtuais Python no Windows. Garanta que scripts e automações sejam compatíveis com o ambiente do laboratório.
- **Diretrizes de Debate:** Estruture debates entre IAs com checkpoints, atas incrementais e registro de decisões. Utilize prompts padronizados e mantenha rastreabilidade de argumentos e conclusões.
- **Fluxo de Revisão de Diretrizes:** Toda revisão deve ser registrada em checklist específico e changelog. Alterações no manifesto devem ser feitas via template, nunca diretamente. Remova ou atualize referências órfãs e garanta alinhamento entre manifesto e anexos.
- **Setup, CI e Automação:** Para configurar o ambiente, autentique o GitHub CLI e execute os comandos necessários para o setup do subprojeto. Para integração contínua (CI), adicione arquivos de workflow e documente cada etapa relevante. Sempre especifique o contexto do subprojeto ao configurar workflows ou automações. Caso o arquivo `.github/PENDENCIAS.md` seja citado, consulte, atualize ou remova pendências conforme instrução do fluxo. Todas as automações e setups devem ser rastreáveis e documentados no changelog e nos checklists do subprojeto correspondente.

### Templates
- **Template de Atualização do Manifesto:** Todas as alterações no manifesto devem ser feitas exclusivamente neste template. O template orienta a estrutura, exemplos e critérios para atualização do manifesto consolidado.
- **Template de Checklist:** Use este template para criar checklists de entrega, revisão ou execução. Garanta que cada etapa seja clara, rastreável e marcada como concluída ou pendente.
- **Template de Checklist de Entrega:** Checklist específico para controle e validação de entregas vinculadas a planos de ação. Deve ser preenchido e referenciado em changelogs e atas.
- **Template de Plano de Ação:** Estruture planos de ação com etapas previstas, critérios de sucesso e justificativa de persistência. Use para registrar e acompanhar execuções relevantes.
- **Template de Conversa IA:** Padroniza prompts e registros de interação entre agentes MCP, GHC e orquestrador. Inclui campos para contexto, tarefas, critérios de sucesso e referência a arquivos relevantes.

### Painel Central e Subprojetos
- **Painel Central de Subprojetos:** Fonte única e oficial para status, pendências e checklists de todos os subprojetos. Deve ser atualizado sempre que houver mudança de status, pendência ou checklist.
- **README — Validação IA Multimodelo:** Documenta objetivos, fluxos, pendências e critérios do subprojeto de validação multimodelo.
- **Checklist — Validação IA Multimodelo:** Lista de tarefas e critérios de sucesso para validação de IA multimodelo.
- **README — Viabilização Debate Multimodelo:** Documenta objetivos, fluxos e pendências do subprojeto de debate multimodelo.
- **Checklist — Viabilização Debate Multimodelo:** Lista de tarefas e critérios de sucesso para o subprojeto de debate multimodelo.
- **Ata Migração Manifesto — Debate Multimodelo:** Registro formal de decisões e histórico de migração do manifesto no contexto do debate multimodelo.

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

---

(Fluxo segue normalmente, sem avisos ou índices duplicados, e com todos os resumos funcionais agrupados em uma seção própria.)
