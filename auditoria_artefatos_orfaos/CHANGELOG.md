# CHANGELOG — Auditoria Automatizada de Artefatos Órfãos

> Registro de todas as alterações, decisões e marcos relevantes do subprojeto.

---

## [2025-10-11] Criação Inicial do Subprojeto

### Contexto
Issue [IA-Orquestração] Auditoria automatizada: Levantamento de artefatos órfãos (branches, PRs, issues) não integrados à master solicitou implementação de sistema de auditoria automatizada para garantir rastreabilidade e governança no ScarecrowLab.

### Descrição
Subprojeto criado para centralizar e executar iniciativas de auditoria de artefatos órfãos no repositório, facilitando retomada de contexto e governança.

### Artefatos Criados
- README.md (sumário executivo, proposta vigente, escopo)
- CHECKLIST.md (7 fases de implementação sequencial)
- CHANGELOG.md (este arquivo)
- Estrutura de diretórios: debates/, scripts/, docs/, relatorios/

### Decisões
- Aprovada criação do subprojeto
- Definido escopo inicial focado em branches, PRs e issues
- Escolhida implementação via Python + GitHub Actions
- Definida execução periódica (semanal) com opção manual

### Próximos Passos
- Testar script localmente e validar funcionamento
- Testar workflow GitHub Actions em branch
- Validar relatórios gerados
- Merge para master após testes

---

## [2025-10-11] Implementação Completa (Fases 2-4)

### Contexto
Continuação da implementação do subprojeto com desenvolvimento do script de auditoria, workflow GitHub Actions e documentação completa.

### Descrição
Implementadas fases 2 (Script de Auditoria), 3 (Workflow GitHub Actions) e 4 (Documentação e Integração) do checklist principal.

### Artefatos Criados
- **scripts/audit_orphaned_artifacts.py** (16.5KB): Script Python completo de auditoria
  - Cliente GitHub API v3 sem dependências externas
  - Auditoria de branches órfãs
  - Auditoria de PRs não mesclados (abertos, fechados, stale)
  - Auditoria de issues órfãs (sem vínculo, stale)
  - Gerador de relatórios em markdown
- **.github/workflows/audit-orphaned-artifacts.yml** (2.9KB): Workflow GitHub Actions
  - Trigger semanal (segundas às 9h UTC)
  - Trigger manual via workflow_dispatch
  - Upload de relatórios como artifacts
  - Commit automático de relatórios no repositório
- **docs/MANUAL_USO.md** (7.5KB): Manual completo de uso
  - Instruções de execução local e via GitHub Actions
  - Interpretação de relatórios
  - Checklist de revisão manual
  - Troubleshooting
  - Integração com governança
- **relatorios/.gitkeep**: Diretório para armazenamento de relatórios

### Alterações Realizadas
- ✅ Atualizado CHECKLIST.md com progresso (Fases 1-4 completas)
- ✅ Atualizado painel central de subprojetos com novo subprojeto
- ✅ Criado script Python sem dependências externas (usa urllib)
- ✅ Implementada lógica de detecção de artefatos órfãos
- ✅ Configurado workflow com execução periódica e manual
- ✅ Documentação completa de uso e integração

### Decisões Técnicas
- **Python stdlib only:** Sem dependências externas para facilitar execução
- **Relatórios markdown:** Formato legível por humanos e fácil versionamento
- **Execução semanal:** Equilíbrio entre visibilidade e custo de API
- **Artifacts + Commit:** Dupla persistência para máxima rastreabilidade
- **Manual completo:** Autonomia para usuários e futuros mantenedores

### Próximos Passos
- Testar script localmente com GITHUB_TOKEN
- Validar workflow em execução manual
- Revisar primeiro relatório gerado
- Ajustar thresholds (stale days) se necessário
- Merge após validação bem-sucedida

---

> Mantenha este changelog atualizado a cada alteração relevante. Use o [template de changelog](../.github/copilot-diretrizes/template_changelog.md) como referência.
