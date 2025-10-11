# Decisões Automatizadas — Logs de Rastreabilidade

> Diretório para armazenamento versionado de todas as decisões automatizadas do Scarecrow AutoFlow.

---

## Propósito

Este diretório contém logs detalhados de todas as decisões automatizadas (classificação, validação, simulação, aprovação/rejeição) realizadas pelo sistema. Cada decisão gera um arquivo markdown individual para rastreabilidade total e auditoria.

## Estrutura de Arquivos

### Nomenclatura

```
YYYY-MM-DD_[tipo]_[id]_[resultado].md
```

**Componentes:**
- `YYYY-MM-DD`: Data da decisão
- `[tipo]`: Tipo de decisão (classification, validation, simulation, approval)
- `[id]`: ID da issue ou PR (ex: issue-123, pr-456)
- `[resultado]`: Resultado resumido (approved, rejected, simulation-needed, manual-needed)

**Exemplos:**
- `2025-10-11_classification_issue-123_automerge.md`
- `2025-10-11_validation_pr-456_approved.md`
- `2025-10-11_simulation_pr-789_approved-with-adjustments.md`
- `2025-10-11_approval_pr-456_merged.md`

### Organização

```
decisoes_automatizadas/
├── README.md                              # Este arquivo
├── 2025-10/                               # Logs por mês
│   ├── 2025-10-11_classification_issue-123_automerge.md
│   ├── 2025-10-11_validation_pr-456_approved.md
│   ├── 2025-10-11_simulation_pr-789_approved.md
│   └── ...
├── 2025-11/
│   └── ...
└── archive/                               # Logs antigos (> 6 meses)
    └── 2025-04/
        └── ...
```

## Template de Log

### Classificação

```markdown
# Log de Classificação — [Título]

**Issue/PR:** #[número]  
**Tipo:** Issue | Pull Request  
**Data:** YYYY-MM-DD HH:MM:SS  
**Versão do Sistema:** 1.0

---

## Metadados Analisados

**Labels:** [lista]  
**Milestone:** [nome ou N/A]  
**Assignees:** [lista ou N/A]  
**Template usado:** [nome ou N/A]  
**Arquivos modificados:** [número] (apenas PRs)  
**Linhas modificadas:** +XXX -YYY (apenas PRs)

## Análise

**Critérios aplicados:**
- [x] Critério 1: [resultado]
- [x] Critério 2: [resultado]
- [ ] Critério 3: [não aplicável]

**Score de confiança:** XX/100

## Decisão

**Categoria:** auto-merge | needs-simulation | manual-review

**Justificativa:**
[Explicação detalhada da decisão]

**Próximos passos:**
- [Ação 1]
- [Ação 2]

---

**Link:** [URL do issue/PR]  
**Log gerado por:** Scarecrow AutoFlow v1.0
```

### Validação

```markdown
# Log de Validação — [Título]

**Issue/PR:** #[número]  
**Tipo:** Issue | Pull Request  
**Data:** YYYY-MM-DD HH:MM:SS  
**Versão do Sistema:** 1.0

---

## Artefatos de Referência

**Validados contra:**
- copilot-instructions.md (versão: commit SHA)
- TEMPLATE_SUBPROJETO.md (versão: commit SHA)
- ...

## Validações Realizadas

### Validação 1: Template Oficial
- Status: ✅ Aprovado | ❌ Reprovado | ⚠️ Aprovado com ressalvas
- Detalhes: [...]

### Validação 2: Princípios Centrais
- Status: ✅ Aprovado
- Detalhes: [...]

## Score de Conformidade

**Total:** XX/100

**Breakdown:**
- Validações críticas: X/Y (peso 10)
- Validações importantes: X/Y (peso 5)
- Validações opcionais: X/Y (peso 2)

## Decisão

**Resultado:** Aprovado | Reprovado | Aprovado com ressalvas

**Não-conformidades (se aplicável):**
- [Lista de problemas identificados]

**Recomendações:**
- [Ações sugeridas]

---

**Link:** [URL do issue/PR]  
**Log gerado por:** Scarecrow AutoFlow v1.0
```

### Simulação

```markdown
# Log de Simulação — [Título]

**Issue/PR:** #[número]  
**Tipo:** Issue | Pull Request  
**Data:** YYYY-MM-DD HH:MM:SS  
**Versão do Sistema:** 1.0  
**Personas:** Engenheiro de Prompt, Guardião do Manifesto, DevOps Modular

---

## Contexto da Simulação

**Razão:** [Por que needs-simulation]  
**Validação prévia:** Score XX/100 (Aprovado com ressalvas)

## Análises das Personas

### Engenheiro de Prompt

**Voto:** Aprovar | Aprovar com ajustes | Rejeitar  
**Confiança:** XX%

**Análise:**
[Texto completo]

**Pontos positivos:**
- [...]

**Pontos de atenção:**
- [...]

### Guardião do Manifesto

[Mesma estrutura]

### DevOps Modular

[Mesma estrutura]

## Deliberação

**Resultado dos votos:**
- Aprovar: X
- Aprovar com ajustes: Y
- Rejeitar: Z

**Tipo de consenso:** Consenso total | Consenso parcial | Dissenso

**Decisão final:** Aprovado | Aprovado com ajustes | Rejeitado | Manual-review

**Justificativa:**
[Explicação consolidada]

## Recomendações

**Para o autor:**
- [Lista de ações]

**Para revisores (se manual-review):**
- [Pontos de atenção]

---

**Link:** [URL do issue/PR]  
**Ata publicada:** [Link para comentário no issue/PR]  
**Log gerado por:** Scarecrow AutoFlow v1.0
```

## Política de Retenção

### Logs Ativos (0-6 meses)
- Mantidos em `decisoes_automatizadas/YYYY-MM/`
- Acesso direto e indexação completa

### Logs Arquivados (6-24 meses)
- Movidos para `decisoes_automatizadas/archive/YYYY-MM/`
- Compactados (.zip) por mês
- Indexação básica mantida

### Logs Históricos (> 24 meses)
- Movidos para repositório de longo prazo (GitHub Releases ou similar)
- Backup completo, acesso sob demanda
- Indexação via metadados

## Indexação

### Arquivo de Índice

`decisoes_automatizadas/INDEX.md` (gerado automaticamente):

```markdown
# Índice de Decisões Automatizadas

## Por Tipo
- [Classificações](./2025-10/classifications.md)
- [Validações](./2025-10/validations.md)
- [Simulações](./2025-10/simulations.md)

## Por Resultado
- [Auto-merges](./2025-10/automerges.md)
- [Rejeições](./2025-10/rejections.md)
- [Manual-reviews](./2025-10/manual-reviews.md)

## Por Mês
- [2025-10](./2025-10/README.md) — XX decisões
- [2025-11](./2025-11/README.md) — XX decisões

## Estatísticas
- Total de decisões: XXXX
- Taxa de automação: XX%
- Taxa de reversão: XX%
```

## Auditoria e Compliance

### Rastreabilidade Bidirecional

Cada log contém:
- Link para issue/PR original
- Commit SHA dos artefatos validados
- Versão do sistema que gerou a decisão

Cada issue/PR contém:
- Comentário com resumo da decisão
- Link para log completo em decisoes_automatizadas/

### Assinatura Digital

Cada log é assinado com:
```
Log gerado por: Scarecrow AutoFlow v[versão]
Commit SHA: [hash do commit do sistema]
Timestamp: [ISO 8601]
```

### Imutabilidade

- Logs não devem ser editados após criação
- Correções devem gerar novo log com referência ao original
- Versionamento via Git garante histórico completo

## Métricas Derivadas

### Taxa de Automação

```
(Auto-merges + Simulações aprovadas) / Total de decisões
```

### Taxa de Reversão

```
Decisões revertidas / Total de aprovações automatizadas
```

### Tempo Médio de Decisão

```
Média(timestamp_decisão - timestamp_criação)
```

### Distribuição por Categoria

```
Gráfico de pizza: auto-merge | needs-simulation | manual-review
```

## Acesso Programático

### CLI (futuro)

```bash
# Listar decisões de hoje
autoflow logs --date today

# Buscar por issue/PR
autoflow logs --issue 123

# Buscar por tipo
autoflow logs --type simulation

# Gerar relatório
autoflow logs --report --month 2025-10
```

### API (futuro)

```
GET /autoflow/logs?date=2025-10-11
GET /autoflow/logs/issue/123
GET /autoflow/stats?month=2025-10
```

---

**Versão:** 1.0  
**Data:** 2025-10-11  
**Última Atualização:** 2025-10-11  

---

> Este diretório é crítico para rastreabilidade e auditoria. Não modifique logs manualmente.
