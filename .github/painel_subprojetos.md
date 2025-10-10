
# Painel Central de Subprojetos — ScarecrowLab

> Fonte única e oficial para status, pendências e checklists de todos os subprojetos. Estrutura enxuta, sem duplicidades, para máxima rastreabilidade e leitura por agentes IA. Toda pendência deve estar vinculada a um subprojeto e checklist/ata.

## Instruções Gerais
- Atualize este painel sempre que houver mudança de status, pendência ou checklist em qualquer subprojeto.
- O MCP/GHC deve consumir este painel para validação automática e geração de relatórios/status.
- Todos os templates e manifestos devem referenciar este painel como fonte única de subprojetos.
- Utilize os campos de links para facilitar navegação e rastreabilidade.

## Instruções de Priorização
- Ordene os subprojetos por prioridade e impacto para facilitar a atuação dos agentes.
- Pendências críticas (Prioridade Alta, Impacto Crítico) devem ser tratadas primeiro.
- Atualize as colunas conforme avaliação periódica dos responsáveis.

---

## Tabela de Subprojetos

| Subprojeto                        | Status Geral   | Pendências Abertas | Prioridade | Impacto | Responsável      | Última Atualização |
|------------------------------------|----------------|--------------------|-----------|---------|------------------|--------------------|
| reestruturacao_modularizacao_lab   | Em andamento   | 2                  | Alta      | Crítico | GitHub Copilot   | 2025-10-10         |
| automacao_manifesto                | Em andamento   | 2                  | Alta      | Alto    | GitHub Copilot   | 2025-10-10         |
| automacao_tarefas_lab              | Em andamento   | 1                  | Alta      | Alto    | GitHub Copilot   | 2025-10-10         |
| framework_diretrizes_ia            | Em andamento   | 1                  | Alta      | Alto    | GitHub Copilot   | 2025-10-10         |
| processamento_fragmentado          | Em andamento   | 1                  | Alta      | Alto    | GitHub Copilot   | 2025-10-10         |
| ativacao_remota_ghc_web            | Em andamento   | 1                  | Média     | Médio   | GitHub Copilot   | 2025-10-10         |
| avaliacao_engenharia_prompt        | Em andamento   | 1                  | Média     | Médio   | GitHub Copilot   | 2025-10-10         |
| extensoes_comandos_scarecrowlab    | Em andamento   | 0                  | Média     | Médio   | GitHub Copilot   | 2025-10-10         |
| teste_serverless_bots_telegram     | Análise concluída | 0               | Baixa     | Baixo   | GitHub Copilot   | 2025-10-10         |
| python_apps/validacao_ia_multimodelo | Em andamento | 1                  | Média     | Médio   | GitHub Copilot   | 2025-10-10         |
| python_apps/viabilizacao_debate_multimodelo | Em andamento | 1        | Média     | Médio   | GitHub Copilot   | 2025-10-10         |
| validacao_ia_multimodelo           | Concluído      | 0                  | -         | -       | GitHub Copilot   | 2025-10-10         |

---

## Pendências Detalhadas por Subprojeto

### reestruturacao_modularizacao_lab
**Status:** Em andamento | **Prioridade:** Alta | **Impacto:** Crítico

**Checklists vinculados:**
- [Checklist principal](../reestruturacao_modularizacao_lab/CHECKLIST.md)
- [Checklist modularização de artefatos globais](../reestruturacao_modularizacao_lab/checklists/CHECKLIST_MODULARIZACAO_ARTEFATOS_GLOBAIS.md)

**Pendências:**
- [ ] Consolidar checklists, ideias e discussões existentes no subprojeto
- [ ] Mapear categorias e propor nova estrutura de diretórios
- Critérios de sucesso: Estrutura modularizada, documentação atualizada, checklists concluídos

---

### automacao_manifesto
**Status:** Em andamento | **Prioridade:** Alta | **Impacto:** Alto

**Checklists vinculados:**
- [Checklist de entrega](../automacao_manifesto/checklists/CHECKLIST_ENTREGA.md)
- [Checklist reformulação manifesto](../automacao_manifesto/checklists/CHECKLIST_REFORMULACAO.md)

**Pendências:**
- [ ] Implementar script de geração automática do manifesto
- [ ] Configurar workflow GitHub Actions para geração
- Critérios de sucesso: Script funcional, workflow configurado, manifesto gerado automaticamente

---

### automacao_tarefas_lab
**Status:** Em andamento | **Prioridade:** Alta | **Impacto:** Alto

**Checklists vinculados:**
- [Checklist principal](../automacao_tarefas_lab/CHECKLIST.md)

**Pendências:**
- [ ] Identificar e documentar tarefas recorrentes do laboratório
- Critérios de sucesso: Tarefas identificadas, automações implementadas

---

### framework_diretrizes_ia
**Status:** Em andamento | **Prioridade:** Alta | **Impacto:** Alto

**Checklists vinculados:**
- [Checklist principal](../framework_diretrizes_ia/CHECKLIST.md)

**Pendências:**
- [ ] Estruturar framework de diretrizes para agentes de IA
- Critérios de sucesso: Framework documentado, diretrizes claras e aplicáveis

---

### processamento_fragmentado
**Status:** Em andamento | **Prioridade:** Alta | **Impacto:** Alto

**Checklists vinculados:**
- [Plano de Ação — Convenção de Arquivos Temporários Persistidos](../processamento_fragmentado/checklists/PLANO_ACAO_CONVENCAO_TMP.md)

**Pendências:**
- [ ] Implementar e validar convenção de arquivos temporários persistidos
- Prioridade: Alta | Impacto: Alto
- Critérios de sucesso: Diretriz formalizada, templates e automações aderentes, rastreabilidade garantida

---

### ativacao_remota_ghc_web
**Status:** Em andamento | **Prioridade:** Média | **Impacto:** Médio

**Checklists vinculados:**
- [Checklist principal](../ativacao_remota_ghc_web/CHECKLIST.md)

**Pendências:**
- [ ] Implementar sistema de ativação remota do GitHub Copilot via web
- Critérios de sucesso: Sistema funcional, documentação completa

---

### avaliacao_engenharia_prompt
**Status:** Em andamento | **Prioridade:** Média | **Impacto:** Médio

**Checklists vinculados:**
- [Checklist principal](../avaliacao_engenharia_prompt/CHECKLIST.md)

**Pendências:**
- [ ] Avaliar técnicas e padrões de engenharia de prompt
- Critérios de sucesso: Relatório de avaliação, recomendações documentadas

---

### extensoes_comandos_scarecrowlab
**Status:** Em andamento | **Prioridade:** Média | **Impacto:** Médio

**Checklists vinculados:**
- (Checklist a ser criado conforme necessidade)

**Pendências:**
- Nenhuma pendência registrada no momento
- Critérios de sucesso: Extensões documentadas e funcionais conforme necessidade

---

### teste_serverless_bots_telegram
**Status:** Análise concluída | **Prioridade:** Baixa | **Impacto:** Baixo

**Checklists vinculados:**
- [Checklist principal](../teste_serverless_bots_telegram/CHECKLIST.md)

**Pendências:**
- Nenhuma pendência aberta. Análise crítica e ATA de validação concluídas em 2025-10-09
- Critérios de sucesso: Análise concluída, relatório disponível

---

### python_apps/validacao_ia_multimodelo
**Status:** Em andamento | **Prioridade:** Média | **Impacto:** Médio

**Checklists vinculados:**
- [Checklist principal](../python_apps/validacao_ia_multimodelo/CHECKLIST.md)

**Pendências:**
- [ ] Validar modelos de IA multimodelo
- Critérios de sucesso: Validação concluída, resultados documentados

---

### python_apps/viabilizacao_debate_multimodelo
**Status:** Em andamento | **Prioridade:** Média | **Impacto:** Médio

**Checklists vinculados:**
- [Checklist principal](../python_apps/viabilizacao_debate_multimodelo/CHECKLIST.md)

**Pendências:**
- [ ] Viabilizar debate entre múltiplos modelos de IA
- Critérios de sucesso: Sistema de debate funcional, documentação completa

---

### validacao_ia_multimodelo
**Status:** Concluído | **Prioridade:** - | **Impacto:** -

**Checklists vinculados:**
- [Checklist de validação IA](../validacao_ia_multimodelo/CHECKLIST.md) ✔️

**Pendências:**
- Todas as pendências concluídas
- Projeto finalizado em 2025-10-08

---

## Notas sobre Pendências Gerais (migradas de PENDENCIAS.md)

As seguintes pendências gerais do laboratório devem ser consideradas em contexto transversal aos subprojetos:

1. **Avaliação prévia de custo/complexidade:** Incluir diretriz em copilot-instructions.md para avaliação de custo antes de execuções onerosas
2. **Configuração de CI:** Avaliar necessidade de integração contínua conforme evolução dos subprojetos
3. **Arquivos de configuração:** Adicionar .editorconfig e linters conforme padrões do laboratório
4. **Documentação do projeto:** Atualizar README.md principal do repositório

> **Recomendação:** Considerar a remoção do arquivo `.github/PENDENCIAS.md` após consolidação completa das informações neste painel, para evitar redundância e garantir fonte única de verdade.

---

> Toda pendência deve ser rastreável ao subprojeto e checklist/ata correspondente. Atualize sempre que houver avanço ou mudança de status.
