
# Painel Central de Subprojetos — ScarecrowLab

> Fonte única e oficial para status, pendências e checklists de todos os subprojetos. Estrutura enxuta, sem duplicidades, para máxima rastreabilidade e leitura por agentes IA. Toda pendência deve estar vinculada a um subprojeto e checklist/ata.

## Instruções
- Atualize este painel sempre que houver mudança de status, pendência ou checklist em qualquer subprojeto.
- Priorize pendências de acordo com prioridade/impacto e registre responsável e data.
- Não duplique pendências: mantenha cada item apenas no bloco detalhado do subprojeto.

## Subprojetos
| Subprojeto | Status | Responsável | Última Atualização |
|------------|--------|-------------|--------------------|
| ativacao_remota_ghc_web | Em andamento | (definir) | (atualizar) |
| automacao_manifesto | Em andamento | (definir) | (atualizar) |
| automacao_tarefas_lab | Em andamento | flaviomassayoshi | 2025-10-09 |
| avaliacao_engenharia_prompt | Em andamento | (definir) | (atualizar) |
| extensoes_comandos_scarecrowlab | Em andamento | (definir) | (atualizar) |
| framework_diretrizes_ia | Em andamento | (definir) | (atualizar) |
| mapa_papeis_responsabilidades_ia | Em andamento | GitHub Copilot | 2025-10-11 |
| reestruturacao_modularizacao_lab | Em andamento | (definir) | (atualizar) |
| teste_serverless_bots_telegram | Em andamento | (definir) | (atualizar) |
| python_apps/stable_diffusion_webui | Em andamento | (definir) | (atualizar) |
| python_apps/validacao_ia_multimodelo | Em andamento | (definir) | (atualizar) |
| python_apps/viabilizacao_debate_multimodelo | Em andamento | (definir) | (atualizar) |
| processamento_fragmentado | Em andamento | 1 | (definir) | 2025-10-10 |
| agente-integrador | Em andamento | flaviomassayoshi | 2025-10-09 |
| extensoes/xyz | Em andamento | userY | 2025-10-07 |
| validacao_ia_multimodelo | Concluído | userX | 2025-10-08 |
| arcabouço_governanca | Em andamento | GitHub Copilot | 2025-10-10 |
| orquestracao_issues_api | Em andamento | GitHub Copilot | 2025-10-11 |

---

## Pendências Detalhadas por Subprojeto

### ativacao_remota_ghc_web
- [ ] [Checklist principal](../ativacao_remota_ghc_web/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### automacao_manifesto
- [ ] [Checklist entrega](../automacao_manifesto/checklists/CHECKLIST_ENTREGA.md): (descrever pendência, prioridade, impacto, critério de sucesso)
- [ ] [Checklist reformulação](../automacao_manifesto/checklists/CHECKLIST_REFORMULACAO.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### automacao_tarefas_lab
- [ ] [Checklist principal](../automacao_tarefas_lab/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### avaliacao_engenharia_prompt
- [ ] [Checklist principal](../avaliacao_engenharia_prompt/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### extensoes_comandos_scarecrowlab

**Última Atualização (2025-10-11):**
- [x] Comando #lab documentado para verificação de contexto persistente
- [x] README atualizado com sintaxe, comportamento e exemplos
- [x] Integrado ao glossário e copilot-instructions.md

**Próximas Pendências:**
- [ ] Definir sintaxe para demais comandos customizados (/checklist, /ata, /aprovar, etc.)

### framework_diretrizes_ia
- [ ] [Checklist principal](../framework_diretrizes_ia/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### mapa_papeis_responsabilidades_ia

**Status:** Em andamento

**Últimas Atualizações (2025-10-11):**
- [x] Estrutura inicial criada com README e ATA_ABERTURA
- [x] Documento de governança automatizada por personas/roles criado
- [x] Links e referências cruzadas estabelecidos

**Próximas Pendências:**
- [ ] Formalizar definição de cada persona/role com responsabilidades detalhadas
    - Prioridade: Alta
    - Impacto: Alto
    - Critérios de sucesso: Documento estruturado com definições claras de Orquestrador, Executor, Auditor, Debatedor e Especialista Temático
- [ ] Criar templates de auditoria para cada tipo de artefato
    - Prioridade: Média
    - Impacto: Alto
- [ ] Implementar scripts de validação automatizada
    - Prioridade: Média
    - Impacto: Alto

**Links Principais:**
- [README](mapa_papeis_responsabilidades_ia/README.md)
- [Ata de Abertura](mapa_papeis_responsabilidades_ia/ATA_ABERTURA.md)
- [Governança por Personas/Roles](mapa_papeis_responsabilidades_ia/debates/GOVERNANCA_PERSONAS_ROLES.md)

### reestruturacao_modularizacao_lab

**Status:** Fase 1 (Consolidação Inicial) concluída. Fase 2 (Proposição de Inovações) pendente.

**Últimas Atualizações (2025-10-10):**
- [x] Estrutura completa de diretórios criada (`debates/`, `checklists/`, `docs/`)
- [x] README.md atualizado com sumário executivo, fases e referências completas
- [x] CHECKLIST.md reorganizado em fases sequenciais
- [x] CHANGELOG.md expandido com histórico detalhado
- [x] ATA_ABERTURA.md padronizada seguindo template oficial
- [x] Criado documento de análise de artefatos ([ANALISE_ARTEFATOS.md](../reestruturacao_modularizacao_lab/docs/ANALISE_ARTEFATOS.md))
- [x] Criado documento de aprendizados ([APRENDIZADOS_REORGANIZACAO.md](../reestruturacao_modularizacao_lab/docs/APRENDIZADOS_REORGANIZACAO.md))
- [x] Rastreabilidade total garantida com links cruzados

**Próximas Pendências:**
- [ ] Executar [Checklist de Modularização de Artefatos Globais](../reestruturacao_modularizacao_lab/checklists/CHECKLIST_MODULARIZACAO_ARTEFATOS_GLOBAIS.md)
    - Pendência: Levantar, modularizar e separar artefatos globais em `.github/`
    - Prioridade: Alta
    - Impacto: Crítico para governança e automação
    - Critérios de sucesso: Estrutura modularizada criada, markup separado de instruções, validação automatizada implementada
- [ ] Mapear categorias e propor nova estrutura de diretórios
    - Prioridade: Média
    - Impacto: Alto
- [ ] Pesquisar e comparar novos artefatos de governança (cards, kanban, dashboards)
    - Prioridade: Média
    - Impacto: Médio

**Links Principais:**
- [README](../reestruturacao_modularizacao_lab/README.md)
- [Checklist Principal](../reestruturacao_modularizacao_lab/CHECKLIST.md)
- [Changelog](../reestruturacao_modularizacao_lab/CHANGELOG.md)
- [Ata de Abertura](../reestruturacao_modularizacao_lab/debates/ATA_ABERTURA.md)
- [Análise de Artefatos](../reestruturacao_modularizacao_lab/docs/ANALISE_ARTEFATOS.md)
- [Aprendizados](../reestruturacao_modularizacao_lab/docs/APRENDIZADOS_REORGANIZACAO.md)

### teste_serverless_bots_telegram
- [ ] [Checklist principal](../teste_serverless_bots_telegram/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### python_apps/stable_diffusion_webui
- [ ] (Adicionar checklist se aplicável): (descrever pendência, prioridade, impacto, critério de sucesso)

### python_apps/validacao_ia_multimodelo
- [ ] (Adicionar checklist se aplicável): (descrever pendência, prioridade, impacto, critério de sucesso)


### processamento_fragmentado
- [ ] [Plano de Ação — Convenção de Arquivos Temporários Persistidos](../processamento_fragmentado/checklists/PLANO_ACAO_CONVENCAO_TMP.md):
    - Pendência: Implementar e validar convenção de arquivos temporários persistidos
    - Prioridade: Alta
    - Impacto: Alto
    - Critérios de sucesso: Diretriz formalizada, templates e automações aderentes, rastreabilidade garantida

### agente-integrador
- [ ] [Checklist principal](../agente-integrador/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### extensoes/xyz
- [ ] [Checklist integração Z](../extensoes/xyz/CHECKLIST.md): (descrever pendência, prioridade, impacto, critério de sucesso)

### validacao_ia_multimodelo
- [x] [Checklist de validação IA](../validacao_ia_multimodelo/CHECKLIST.md): concluído

### arcabouço_governanca
- [x] Regeneração de templates oficiais ausentes:
    - Pendência: Criar templates referenciados mas ausentes no repositório
    - Prioridade: Alta
    - Impacto: Crítico para rastreabilidade e autossuficiência do MCP
    - Status: Concluído
    - Critérios de sucesso: Todos os templates referenciados em copilot-instructions.md devem estar acessíveis
    - Resultado: ✅ TEMPLATE_SUBPROJETO.md relocado para .github/, TEMPLATE_ATA.md criado, templates_index.md atualizado

---

> Toda pendência deve ser rastreável ao subprojeto e checklist/ata correspondente. Atualize sempre que houver avanço ou mudança de status.

# Painel Central de Subprojetos — ScarecrowLab

> Fonte única e oficial para status, pendências e checklists de todos os subprojetos. Estrutura e campos podem ser expandidos conforme necessidade do laboratório. Deve ser referenciado por manifestos, templates e pelo MCP/GHC para validação, rastreabilidade e atuação proativa.

## Instruções Gerais
- Atualize este painel sempre que houver mudança de status, pendência ou checklist em qualquer subprojeto.
- O MCP/GHC deve consumir este painel para validação automática e geração de relatórios/status.
- Todos os templates e manifestos devem referenciar este painel como fonte única de subprojetos.
- Utilize os campos de links para facilitar navegação e rastreabilidade.

## Instruções de Priorização
- Ordene os subprojetos por prioridade e impacto para facilitar a atuação dos agentes.
- Pendências críticas (Prioridade Alta, Impacto Crítico) devem ser tratadas primeiro.
- Atualize as colunas conforme avaliação periódica dos responsáveis.


| Subprojeto                        | Status Geral   | Pendências Abertas | Prioridade | Impacto | Checklists Vinculados                                                                                                   | Responsável      | Última Atualização |
|------------------------------------|----------------|--------------------|-----------|---------|----------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------|
| ativacao_remota_ghc_web            | Em andamento   | 1                  | Média     | Médio   | [Checklist](../ativacao_remota_ghc_web/CHECKLIST.md) | (definir)         | (atualizar)        |
| automacao_manifesto                | Em andamento   | 1                  | Alta      | Alto    | [Checklist entrega](../automacao_manifesto/checklists/CHECKLIST_ENTREGA.md), [Checklist reformulação](../automacao_manifesto/checklists/CHECKLIST_REFORMULACAO.md) | (definir)         | (atualizar)        |
| automacao_tarefas_lab              | Em andamento   | 1                  | Alta      | Alto    | [Checklist](../automacao_tarefas_lab/CHECKLIST.md) | flaviomassayoshi   | 2025-10-09         |
| avaliacao_engenharia_prompt        | Em andamento   | 1                  | Média     | Médio   | [Checklist](../avaliacao_engenharia_prompt/CHECKLIST.md) | (definir)         | (atualizar)        |
| extensoes_comandos_scarecrowlab    | Em andamento   | 0                  | Média     | Médio   | [README](../extensoes_comandos_scarecrowlab/README.md) | GitHub Copilot    | 2025-10-11         |
| framework_diretrizes_ia            | Em andamento   | 1                  | Alta      | Alto    | [Checklist](../framework_diretrizes_ia/CHECKLIST.md) | (definir)         | (atualizar)        |
| mapa_papeis_responsabilidades_ia   | Em andamento   | 3                  | Alta      | Alto    | [README](mapa_papeis_responsabilidades_ia/README.md), [Ata Abertura](mapa_papeis_responsabilidades_ia/ATA_ABERTURA.md), [Governança Personas](mapa_papeis_responsabilidades_ia/debates/GOVERNANCA_PERSONAS_ROLES.md) | GitHub Copilot | 2025-10-11 |
| reestruturacao_modularizacao_lab   | Em andamento (Fase 1 concluída) | 0 | Alta | Crítico | [README](../reestruturacao_modularizacao_lab/README.md), [Checklist Principal](../reestruturacao_modularizacao_lab/CHECKLIST.md), [Checklist Modularização](../reestruturacao_modularizacao_lab/checklists/CHECKLIST_MODULARIZACAO_ARTEFATOS_GLOBAIS.md), [Changelog](../reestruturacao_modularizacao_lab/CHANGELOG.md) | GitHub Copilot | 2025-10-10 |
| teste_serverless_bots_telegram     | Em andamento   | 1                  | Média     | Médio   | [Checklist](../teste_serverless_bots_telegram/CHECKLIST.md) | (definir)         | (atualizar)        |
| python_apps/stable_diffusion_webui | Em andamento   | 1                  | Média     | Médio   | (Adicionar checklist se aplicável) | (definir)         | (atualizar)        |
| python_apps/validacao_ia_multimodelo | Em andamento | 1                  | Média     | Médio   | (Adicionar checklist se aplicável) | (definir)         | (atualizar)        |
| python_apps/viabilizacao_debate_multimodelo | Em andamento | 1           | Média     | Médio   | (Adicionar checklist se aplicável) | (definir)         | (atualizar)        |
| agente-integrador                  | Em andamento   | 2                  | Alta      | Crítico | [Checklist principal](../agente-integrador/CHECKLIST.md), Revisar ata de 2025-10-12 (✔️), Atualizar README (⏳), Criar changelog (⏳), Vincular checklist (⏳) | flaviomassayoshi | 2025-10-09         |
| extensoes/xyz                      | Em andamento   | 1                  | Média     | Médio   | [Checklist integração Z](../extensoes/xyz/CHECKLIST.md), Implementar integração Z (⏳), Revisar documentação (⏳) | userY            | 2025-10-07         |
| validacao_ia_multimodelo           | Concluído      | 0                  | -         | -       | [Checklist de validação IA](../validacao_ia_multimodelo/CHECKLIST.md) (✔️) | userX            | 2025-10-08         |
| orquestracao_issues_api            | Em andamento (Fase 1 concluída) | 1 | Alta | Alto | [README](../orquestracao_issues_api/README.md), [Checklist Principal](../orquestracao_issues_api/CHECKLIST.md), [Changelog](../orquestracao_issues_api/CHANGELOG.md), [ATA Abertura](../orquestracao_issues_api/debates/ATA_ABERTURA.md) | GitHub Copilot | 2025-10-11 |

## Pendências Detalhadas

### agente-integrador
- Pendência: Atualizar README do subprojeto "agente-integrador"
    - Contexto: Novo fluxo de integração aprovado na ata de 2025-10-12
    - Critérios de sucesso: README atualizado, changelog registrado

### extensoes/xyz
- Pendência: Implementar integração Z
    - Contexto: Nova extensão aprovada
    - Critérios de sucesso: integração funcional, documentação revisada

### orquestracao_issues_api

**Status:** Fase 1 (Planejamento e Estruturação) 100% concluída

**Últimas Atualizações (2025-10-11):**
- [x] Avaliação formal de projetos/subprojetos existentes (sem conflitos identificados)
- [x] Estrutura completa de diretórios criada (`debates/`, `checklists/`, `docs/`)
- [x] README.md com sumário executivo, proposta vigente e integrações
- [x] CHECKLIST.md estruturado em 7 fases (planejamento até evolução contínua)
- [x] CHANGELOG.md com entrada inicial de criação
- [x] ATA_ABERTURA.md documentando decisões e justificativas
- [x] Documentação de avaliação de projetos existentes
- [x] Atualização do painel central de subprojetos
- [x] Validação de rastreabilidade e links cruzados (todos funcionais e bidirecionais)

**Próximas Pendências:**
- [ ] Iniciar Fase 2 (Definição de Requisitos)
    - Pendência: Mapear casos de uso prioritários e especificar comandos
    - Prioridade: Alta
    - Impacto: Alto
    - Critérios de sucesso: Casos de uso documentados, comandos especificados, requisitos de segurança definidos

**Links Principais:**
- [README](../orquestracao_issues_api/README.md)
- [Checklist Principal](../orquestracao_issues_api/CHECKLIST.md)
- [Changelog](../orquestracao_issues_api/CHANGELOG.md)
- [ATA de Abertura](../orquestracao_issues_api/debates/ATA_ABERTURA.md)
- [Avaliação de Projetos Existentes](../orquestracao_issues_api/docs/AVALIACAO_PROJETOS_EXISTENTES.md)

## Observação sobre PENDENCIAS.md
- Recomenda-se migrar ou referenciar todas as pendências e checklists do arquivo `PENDENCIAS.md` para este painel central, tornando-o a única fonte de verdade para priorização e rastreabilidade. Após a migração, o arquivo pode ser removido para evitar redundância.
