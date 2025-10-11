# Relatório de Auditoria — Artefatos Órfãos

**Repositório:** flaviomassayoshi/ScarecrowLab  
**Data/Hora:** 2025-10-11 04:30 UTC  
**Gerado por:** audit_orphaned_artifacts.py

---

## Sumário Executivo

| Categoria | Quantidade |
|-----------|------------|
| Branches órfãs | 2 |
| PRs abertos não mesclados | 1 |
| PRs fechados não mesclados | 1 |
| PRs stale (>30 dias sem atividade) | 0 |
| Issues sem vínculo | 3 |
| Issues stale (>60 dias sem atividade) | 1 |

---

## 1. Branches Órfãs

**Critério:** Branches com commits não mesclados na master e sem PRs associados.

| Branch | Commits à frente | Último commit | Autor | SHA |
|--------|------------------|---------------|-------|-----|
| `feature/experimental-ui` | 5 | 2025-09-15T10:30:00Z | John Doe | `a1b2c3d` |
| `hotfix/legacy-api` | 2 | 2025-08-20T14:22:00Z | Jane Smith | `e4f5g6h` |

---

## 2. Pull Requests Não Mesclados

### 2.1 PRs Abertos (1)

| # | Título | Autor | Branch | Criado | Atualizado |
|---|--------|-------|--------|--------|------------|
| #123 | Add new feature X | octocat | `feature/new-feature-x` | 2025-10-01 | 2025-10-10 |

### 2.2 PRs Fechados Não Mesclados (1)

| # | Título | Autor | Branch | Criado | Atualizado |
|---|--------|-------|--------|--------|------------|
| #118 | Refactor database layer | developer | `refactor/database` | 2025-09-10 | 2025-09-15 |

### 2.3 PRs Stale (>30 dias sem atividade) (0)

✅ Nenhum PR stale.

---

## 3. Issues Órfãs

### 3.1 Issues Sem Vínculo com PRs (3)

| # | Título | Autor | Labels | Criado | Atualizado |
|---|--------|-------|--------|--------|------------|
| #125 | Investigate performance bottleneck | maintainer | bug, performance | 2025-10-05 | 2025-10-08 |
| #120 | Update documentation for API v2 | contributor | documentation | 2025-09-28 | 2025-10-02 |
| #115 | Add tests for user authentication | tester | testing, enhancement | 2025-09-18 | 2025-09-25 |

### 3.2 Issues Stale (>60 dias sem atividade) (1)

| # | Título | Autor | Labels | Criado | Atualizado |
|---|--------|-------|--------|--------|------------|
| #95 | Improve error handling in CLI | olduser | enhancement | 2025-07-15 | 2025-08-01 |

---

## Recomendações

1. **Branches órfãas:** Avaliar se devem ser removidas ou associadas a PRs
2. **PRs não mesclados:** Revisar se devem ser mesclados, fechados ou atualizados
3. **Issues órfãas:** Vincular a PRs, milestones ou fechar se não forem mais relevantes
4. **Artefatos stale:** Considerar arquivamento ou atualização para reativar

---

> Relatório gerado automaticamente. Para mais informações, consulte [Manual de Uso](../docs/MANUAL_USO.md).
