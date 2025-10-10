# Guia de Uso: Auto-Aprovação de Pull Requests

## O que é?

O workflow de auto-aprovação permite que Pull Requests sejam aprovados automaticamente quando atendem a critérios específicos de confiança, reduzindo o tempo de espera para mudanças de baixo risco.

## Como funciona?

Quando um PR é aberto, atualizado ou reaberto, o workflow verifica se ele atende a algum dos critérios de auto-aprovação. Se sim:
1. ✅ O PR é aprovado automaticamente
2. 💬 Um comentário é adicionado explicando a aprovação
3. ⏸️ O PR permanece aberto (não há merge automático)

## Critérios de Auto-Aprovação

Um PR será aprovado automaticamente se **qualquer** condição for verdadeira:

### 1. Label "auto-approve"
```bash
# Adicionar label via GitHub CLI
gh pr edit 123 --add-label "auto-approve"

# Ou adicionar via interface web do GitHub
```

**Quando usar:**
- PRs de documentação
- Mudanças triviais (correções de typo, formatação)
- Atualizações aprovadas previamente pelo time

### 2. Bot confiável
- `dependabot[bot]` - atualizações de dependências
- `renovate[bot]` - atualizações de dependências

**Automático:** Estes bots já são reconhecidos automaticamente.

### 3. Dono do repositório
- PRs criados pelo usuário `flaviomassayoshi` (dono do repositório)

**Automático:** Reconhecimento baseado no proprietário do repo.

## Exemplos de Uso

### Exemplo 1: Aprovar PR de documentação

```bash
# 1. Criar PR
git checkout -b docs/update-readme
git commit -m "docs: atualizar README"
git push origin docs/update-readme
gh pr create --title "Atualizar README" --body "Correções de documentação"

# 2. Adicionar label para aprovação automática
gh pr edit --add-label "auto-approve"

# ✅ O workflow aprovará automaticamente o PR
```

### Exemplo 2: Dependabot

```yaml
# Configurar Dependabot no repositório (.github/dependabot.yml)
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

✅ PRs do Dependabot serão aprovados automaticamente.

### Exemplo 3: Dono do repositório

Como dono do repositório (`flaviomassayoshi`), todos os seus PRs serão aprovados automaticamente.

## Segurança

### Permissões necessárias
- O workflow usa `GITHUB_TOKEN` padrão
- Permissões: `pull-requests: write`, `contents: read`
- Não requer tokens adicionais ou secrets

### Limitações de segurança
- ✅ Apenas aprova, não faz merge automático
- ✅ Branch protection rules são respeitadas
- ✅ Checks de CI devem passar antes do merge
- ✅ Aprovação não bypassa regras de proteção

## Personalização

Para adicionar novos critérios, edite `.github/workflows/auto-approve-pr.yml`:

```yaml
if: |
  (
    contains(github.event.pull_request.labels.*.name, 'auto-approve') ||
    github.event.pull_request.user.login == 'dependabot[bot]' ||
    github.event.pull_request.user.login == 'renovate[bot]' ||
    github.actor == github.repository_owner ||
    # ADICIONE NOVOS CRITÉRIOS AQUI
    contains(github.event.pull_request.labels.*.name, 'seu-novo-criterio')
  )
```

## Merge Automático (Opcional)

Para habilitar merge automático após aprovação:

```bash
# Habilitar auto-merge no PR
gh pr merge 123 --auto --squash

# Ou via interface web: "Enable auto-merge"
```

⚠️ **Atenção:** Auto-merge requer:
- Todas as branch protection rules satisfeitas
- Todos os checks de CI passando
- Número mínimo de aprovações atingido

## Troubleshooting

### PR não foi aprovado automaticamente?

Verifique:
1. ✅ O PR atende a algum critério?
2. ✅ O workflow foi executado? (Aba "Actions" do PR)
3. ✅ Há erros nos logs do workflow?

### Como desabilitar temporariamente?

Renomeie o arquivo do workflow:
```bash
mv .github/workflows/auto-approve-pr.yml .github/workflows/auto-approve-pr.yml.disabled
```

### Como ver histórico de aprovações?

```bash
# Ver execuções do workflow
gh run list --workflow=auto-approve-pr.yml

# Ver detalhes de uma execução
gh run view 123456
```

## Referências

- [Documentação dos Workflows](README.md)
- [Subprojeto automacao_tarefas_lab](../../automacao_tarefas_lab/README.md)
- [hmarr/auto-approve-action](https://github.com/hmarr/auto-approve-action)
- [GitHub Actions: Pull Request Events](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request)

---

> **Dúvidas?** Abra uma issue no repositório ou consulte a documentação completa em `.github/workflows/README.md`.
