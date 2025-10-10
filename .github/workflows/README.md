# Workflows do GitHub Actions — ScarecrowLab

Este diretório contém os workflows de automação do laboratório, implementados via GitHub Actions.

## Workflows Disponíveis

### 1. Auto Approve PRs (`auto-approve-pr.yml`)

**Objetivo:** Aprovar automaticamente Pull Requests que atendam a critérios específicos de confiança.

**Gatilho:** Acionado quando um PR é aberto, sincronizado ou reaberto.

**Critérios de Auto-Aprovação:**

Um PR será aprovado automaticamente se **qualquer** um dos seguintes critérios for atendido:

1. **Label "auto-approve"**: PR possui a label `auto-approve`
2. **Bot confiável**: PR criado por `dependabot[bot]` ou `renovate[bot]`
3. **Dono do repositório**: PR criado pelo dono do repositório

**Comportamento:**
- Aprova o PR automaticamente se os critérios forem atendidos
- Adiciona um comentário explicativo no PR informando sobre a aprovação automática
- Não faz merge automático (apenas aprova)

**Segurança:**
- Utiliza `GITHUB_TOKEN` padrão (escopo limitado ao repositório)
- Permissões mínimas necessárias: `pull-requests: write`, `contents: read`

**Como Usar:**

Para aprovar um PR automaticamente, você pode:

1. Adicionar a label `auto-approve` ao PR
2. Criar PR com bot confiável (dependabot, renovate)
3. Criar PR como dono do repositório

**Exemplo de Uso:**

```bash
# Adicionar label ao PR via CLI
gh pr edit 123 --add-label "auto-approve"

# O workflow será acionado automaticamente e aprovará o PR
```

**Personalização:**

Para adicionar novos critérios de auto-aprovação, edite o arquivo `.github/workflows/auto-approve-pr.yml` e modifique a condição `if` nos steps `Auto approve` e `Add comment on auto-approval`.

**Limitações:**

- O workflow apenas **aprova** o PR, não faz merge automático
- Para merge automático, será necessário workflow adicional
- Depende da configuração de branch protection rules do repositório

## Próximos Workflows Planejados

- Geração automática do ManifestoMCP.md
- Validação automática de checklists
- Atualização automática do painel de subprojetos
- Testes automatizados de integridade

## Referências

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [hmarr/auto-approve-action](https://github.com/hmarr/auto-approve-action)
- Subprojeto relacionado: [automacao_tarefas_lab](../../automacao_tarefas_lab/)
- Painel central: [.github/painel_subprojetos.md](../painel_subprojetos.md)

---

> Consulte as diretrizes do ScarecrowLab em `.github/copilot-diretrizes/` para mais informações sobre automação e workflows.
