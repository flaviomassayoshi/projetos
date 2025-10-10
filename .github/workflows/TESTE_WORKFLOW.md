# Como Testar o Workflow de Auto-Aprovação

## Cenário 1: Testar com Label "auto-approve"

### Passo 1: Criar um PR de teste
```bash
# 1. Criar branch de teste
git checkout -b test/auto-approve-feature

# 2. Fazer uma mudança simples
echo "# Teste de auto-approve" >> TEST_AUTO_APPROVE.md
git add TEST_AUTO_APPROVE.md
git commit -m "test: adicionar arquivo de teste"

# 3. Enviar para GitHub
git push origin test/auto-approve-feature

# 4. Criar PR
gh pr create \
  --title "TEST: Auto-approve workflow" \
  --body "Este PR testa a funcionalidade de auto-aprovação"
```

### Passo 2: Adicionar label
```bash
# Obter número do PR (ex: 123)
PR_NUM=$(gh pr view --json number -q .number)

# Adicionar label
gh pr edit $PR_NUM --add-label "auto-approve"
```

### Passo 3: Verificar execução
```bash
# Ver execuções do workflow
gh run list --workflow=auto-approve-pr.yml --limit 1

# Ver detalhes da execução
gh run view --log
```

### Resultado Esperado
- ✅ PR aprovado automaticamente
- ✅ Comentário adicionado no PR
- ✅ Workflow executado com sucesso

---

## Cenário 2: Testar com PR do Dono do Repositório

Se você é `flaviomassayoshi` (dono do repositório):

```bash
# 1. Criar branch e fazer mudança
git checkout -b test/owner-approval
echo "# Teste owner" >> OWNER_TEST.md
git add OWNER_TEST.md
git commit -m "test: testar aprovação de owner"
git push origin test/owner-approval

# 2. Criar PR (será aprovado automaticamente)
gh pr create \
  --title "TEST: Owner auto-approval" \
  --body "Teste de aprovação automática para owner"
```

### Resultado Esperado
- ✅ PR aprovado automaticamente sem necessidade de label
- ✅ Comentário explicativo adicionado

---

## Cenário 3: Verificar que PRs sem Critérios NÃO são Aprovados

```bash
# 1. Criar PR sem label e de outro usuário (se possível)
git checkout -b test/no-auto-approve
echo "# Sem aprovação automática" >> NO_AUTO_APPROVE.md
git add NO_AUTO_APPROVE.md
git commit -m "test: PR sem auto-aprovação"
git push origin test/no-auto-approve

gh pr create \
  --title "TEST: No auto-approve" \
  --body "Este PR NÃO deve ser aprovado automaticamente"
```

### Resultado Esperado
- ✅ Workflow executa mas não aprova
- ✅ PR permanece sem aprovação
- ✅ Sem comentário automático

---

## Verificar Logs do Workflow

### Ver todas as execuções
```bash
gh run list --workflow=auto-approve-pr.yml
```

### Ver logs de uma execução específica
```bash
# Obter ID da execução
gh run list --workflow=auto-approve-pr.yml --limit 1 --json databaseId -q '.[0].databaseId'

# Ver logs detalhados
gh run view <RUN_ID> --log
```

### Ver logs em tempo real
```bash
gh run watch
```

---

## Testar Localmente (Validação de Sintaxe)

### Validar sintaxe YAML
```bash
# Usando Python + PyYAML
python3 -c "
import yaml
with open('.github/workflows/auto-approve-pr.yml') as f:
    yaml.safe_load(f)
print('✅ Sintaxe válida')
"
```

### Usar act para simular localmente (opcional)
```bash
# Instalar act: https://github.com/nektos/act
act pull_request \
  --workflows .github/workflows/auto-approve-pr.yml \
  --dryrun
```

---

## Troubleshooting

### Workflow não executou?

Verifique:
```bash
# 1. Verificar se o workflow existe
ls -la .github/workflows/auto-approve-pr.yml

# 2. Verificar permissões do repositório
# GitHub > Settings > Actions > General > Workflow permissions
# Deve estar em "Read and write permissions"
```

### Workflow executou mas não aprovou?

```bash
# Ver logs detalhados
gh run view --log

# Verificar se a condição foi atendida
gh pr view <PR_NUM> --json labels,author -q .
```

### Erro de permissões?

Certifique-se de que:
1. Actions estão habilitadas no repositório
2. Workflow permissions estão corretas
3. Branch protection rules não impedem aprovação

---

## Limpeza Após Testes

```bash
# Deletar PRs de teste
gh pr close <PR_NUM> --delete-branch

# Deletar branches locais
git branch -D test/auto-approve-feature
git branch -D test/owner-approval
git branch -D test/no-auto-approve

# Deletar branches remotas
git push origin --delete test/auto-approve-feature
git push origin --delete test/owner-approval
git push origin --delete test/no-auto-approve
```

---

## Referências

- [GitHub Actions: Testing Workflows](https://docs.github.com/en/actions/automating-builds-and-tests)
- [act - Run GitHub Actions Locally](https://github.com/nektos/act)
- [GitHub CLI: gh run](https://cli.github.com/manual/gh_run)
