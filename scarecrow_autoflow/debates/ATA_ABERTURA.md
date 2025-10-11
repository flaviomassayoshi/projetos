# Ata de Abertura — Scarecrow AutoFlow

**Data:** 2025-10-11  
**Tipo:** Criação de Subprojeto  
**Responsável:** GitHub Copilot  
**Participantes:** Agente MCP/GHC  

---

## Contexto

O ScarecrowLab enfrenta gargalo crítico de aprovação manual de issues e pull requests, conforme documentado em issue do projeto. Este gargalo impacta negativamente:
- Velocidade de entrega de melhorias e correções
- Escalabilidade operacional do laboratório
- Eficiência de agentes e contribuidores
- Rastreabilidade de decisões de aprovação

## Proposta

Criar subprojeto "Scarecrow AutoFlow" para implementar sistema modular de:
1. Classificação automatizada de issues/PRs
2. Validação de conformidade com artefatos constitucionais
3. Simulação de decisões por personas especializadas
4. Aprovação automatizada com rastreabilidade total
5. Monitoramento e evolução contínua

## Objetivo

Reduzir drasticamente (alvo: 80% para casos simples) a necessidade de aprovação manual, mantendo ou aumentando qualidade das decisões através de validação rigorosa e rastreabilidade completa.

## Decisões Tomadas

### 1. Escopo e Delimitação

**Incluído:**
- Classificador automático de issues/PRs
- Validador de conformidade com manifesto, templates e diretrizes
- Simulador de decisão com personas do laboratório
- Sistema de logs versionados
- GitHub Actions workflows
- Labels automáticos

**Excluído:**
- Automação de tarefas internas não relacionadas a aprovações (coberto por automacao_tarefas_lab)
- Orquestração genérica de issues (coberto por orquestracao_issues_api)
- Alteração de artefatos constitucionais do laboratório

**Justificativa:** Evitar sobreposição com subprojetos existentes e manter foco em aprovações automatizadas.

### 2. Categorias de Classificação

**auto-merge:**
- Requisitos claramente atendidos
- Conformidade total com artefatos
- Sem risco identificado
- Exemplos: docs simples, typos, dependências sem breaking changes

**needs-simulation:**
- Requisitos parcialmente atendidos
- Necessita validação multi-perspectiva
- Exemplos: novos subprojetos, mudanças em diretrizes, alterações em templates

**manual-review:**
- Requisitos complexos ou conflitantes
- Mudanças de alto impacto
- Alterações em artefatos críticos
- Exemplos: manifesto consolidado, fluxos centrais, decisões estratégicas

**Justificativa:** Balanceamento entre automação agressiva (auto-merge) e prudência (manual-review), com categoria intermediária (needs-simulation) para casos que beneficiam de análise multi-perspectiva automatizada.

### 3. Personas Simuladas

**Engenheiro de Prompt:**
- Foco: clareza, efetividade, manutenibilidade
- Valida: templates, prompts, diretrizes de comunicação

**Guardião do Manifesto:**
- Foco: conformidade constitucional, rastreabilidade
- Valida: aderência ao manifesto, glossário, princípios centrais

**DevOps Modular:**
- Foco: automação, modularidade, integração
- Valida: scripts, workflows, integrações entre subprojetos

**Justificativa:** Cobertura das principais perspectivas de governança do laboratório (prompt engineering, conformidade institucional, infraestrutura técnica).

### 4. Estrutura de Implementação

**Modular:**
- Scripts separados: classificador.py, validador.py, simulador.py
- GitHub Actions independentes por tipo de evento
- Logs isolados em decisoes_automatizadas/

**Justificativa:** Facilita manutenção, testes isolados e evolução independente de cada componente.

### 5. Rastreabilidade

**Logs versionados:**
- Toda decisão automatizada gera log em decisoes_automatizadas/
- Estrutura: YYYY-MM-DD_tipo_id_decisao.md
- Conteúdo: categoria, critérios aplicados, resultado, personas (se simulado)

**Justificativa:** Auditabilidade total, aprendizado contínuo, reversibilidade de decisões.

## Alinhamento com Arcabouço

### Diretrizes Seguidas

- [x] Template de Subprojeto utilizado como base
- [x] Glossário consultado para termos e definições
- [x] Diretrizes de subprojetos seguidas (estrutura, nomenclatura, rastreabilidade)
- [x] Fluxos gerais para agentes respeitados (plano, checklist, changelog, ata)

### Princípios Centrais Atendidos

- [x] Modularização: scripts e workflows isolados e independentes
- [x] Rastreabilidade: logs de todas as decisões, changelog, atas
- [x] Automação: foco total em reduzir intervenção manual
- [x] Integração transparente: com automacao_tarefas_lab, orquestracao_issues_api, framework_diretrizes_ia
- [x] Templates e comandos padronizados: uso de templates existentes e labels consistentes
- [x] Documentação autoexplicativa: README completo, docs técnicos, guia de uso

## Integrações Planejadas

**automacao_tarefas_lab:**
- Fornece infraestrutura base de automação
- Pode acionar classificação/validação como parte de workflows maiores

**orquestracao_issues_api:**
- Fornece framework de orquestração de issues
- Scarecrow AutoFlow consome APIs para classificar/validar/aprovar

**framework_diretrizes_ia:**
- Fornece diretrizes normativas para validação
- Critérios de conformidade baseados em artefatos deste framework

**mapa_papeis_responsabilidades_ia:**
- Define personas e roles para simulação
- Scarecrow AutoFlow usa definições de roles para simular decisões

## Riscos Identificados

### 1. Falsos Positivos (Auto-Merge Indevido)

**Risco:** Sistema classifica como auto-merge algo que deveria ser manual-review  
**Mitigação:** 
- Validação rigorosa por múltiplos critérios
- Logs detalhados para auditoria
- Período inicial de "dry-run" (classificação sem ação)
- Revisão periódica de decisões automatizadas

### 2. Falsos Negativos (Manual-Review Excessivo)

**Risco:** Sistema classifica como manual-review algo que poderia ser auto-merge  
**Mitigação:**
- Ajuste contínuo de critérios baseado em métricas
- Análise de casos classificados como manual-review
- Evolução incremental das regras

### 3. Simulação Inconclusiva

**Risco:** Personas simuladas não chegam a consenso  
**Mitigação:**
- Regras de desempate claras (default: manual-review)
- Logs de debates inconclusivos para análise
- Refinamento de personas e lógica de deliberação

### 4. Sobrecarga de Logs

**Risco:** Volume excessivo de logs impacta performance e armazenamento  
**Mitigação:**
- Arquivamento periódico de logs antigos
- Indexação eficiente por data/tipo/resultado
- Compactação de logs após período de retenção

## Roadmap Inicial

### Curto Prazo (1-2 semanas)
- Fase 2: Documentação técnica detalhada
- Fase 3: Implementação do classificador
- Fase 4: Implementação do validador

### Médio Prazo (3-4 semanas)
- Fase 5: Implementação do simulador
- Fase 6: GitHub Actions workflows
- Fase 7: Sistema de logs e rastreabilidade

### Longo Prazo (5-6 semanas)
- Fase 8: Integração e governança
- Fase 9: Testes e validação
- Fase 10: Painel de governança (opcional)

## Próximas Ações

1. Atualizar painel central de subprojetos (.github/painel_subprojetos.md)
2. Criar documentação técnica detalhada (docs/)
3. Implementar script classificador (scripts/classificador.py)
4. Implementar script validador (scripts/validador.py)
5. Implementar script simulador (scripts/simulador.py)

## Critérios de Sucesso

### Fase 1 (Estruturação) ✅
- [x] Estrutura de diretórios criada
- [x] README.md completo
- [x] CHECKLIST.md estruturado
- [x] CHANGELOG.md inicializado
- [x] ATA_ABERTURA.md registrada

### Projeto Completo
- [ ] Taxa de automação ≥ 60% (meta: 80%)
- [ ] Tempo médio de aprovação reduzido em ≥ 50%
- [ ] Taxa de conformidade (sem reversão) ≥ 95%
- [ ] Cobertura de classificação ≥ 90%
- [ ] Integração completa com painel central
- [ ] Documentação completa e testada

## Observações

- Este subprojeto é estratégico para escalabilidade operacional do ScarecrowLab
- Deve evoluir de forma incremental, com validação contínua
- Feedback de uso real deve guiar ajustes de critérios e regras
- Rastreabilidade total é requisito não-negociável

---

**Aprovação:** Subprojeto aprovado para implementação conforme esta ata.

**Assinatura Digital:** GitHub Copilot (agente MCP/GHC), 2025-10-11

---

> Esta ata é documento persistente e rastreável. Referenciá-la em decisões futuras do subprojeto.
