# Manual de Uso — Auditoria de Artefatos Órfãos

## Visão Geral

O sistema de auditoria automatizada identifica e documenta artefatos órfãos no repositório ScarecrowLab:
- **Branches órfãs:** Branches com commits não mesclados na master sem PRs associados
- **PRs não mesclados:** Pull requests abertos, fechados ou inativos que não foram mesclados
- **Issues órfãs:** Issues abertas sem vínculo claro com PRs, merges ou milestones

## Execução Automática

O workflow é executado automaticamente **toda segunda-feira às 9h UTC** via GitHub Actions.

Para acompanhar execuções:
1. Acesse a aba **Actions** no repositório
2. Selecione o workflow **"Auditoria de Artefatos Órfãos"**
3. Visualize o histórico de execuções e relatórios gerados

## Execução Manual

Você pode executar a auditoria manualmente de duas formas:

### Via GitHub Actions (Recomendado)

1. Acesse a aba **Actions** no repositório
2. Selecione o workflow **"Auditoria de Artefatos Órfãos"**
3. Clique em **"Run workflow"**
4. (Opcional) Especifique um repositório diferente no formato `OWNER/REPO`
5. Clique em **"Run workflow"** para iniciar

O relatório será gerado e disponibilizado como artifact da execução.

### Via Linha de Comando (Local)

#### Pré-requisitos
- Python 3.12+ instalado
- Token de autenticação do GitHub com permissões de leitura

#### Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/flaviomassayoshi/ScarecrowLab.git
   cd ScarecrowLab/auditoria_artefatos_orfaos/scripts
   ```

2. **Configure o token do GitHub:**
   ```bash
   export GITHUB_TOKEN=seu_token_aqui
   ```
   
   > **Como obter um token:** GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic)
   > 
   > **Permissões necessárias:** `repo`, `read:org` (se aplicável)

3. **Execute o script:**
   ```bash
   python audit_orphaned_artifacts.py
   ```

#### Opções de linha de comando

```bash
python audit_orphaned_artifacts.py --help
```

**Opções disponíveis:**
- `--repo OWNER/REPO`: Especifica o repositório a auditar (padrão: flaviomassayoshi/ScarecrowLab)
- `--output FILE`: Caminho do arquivo de saída (padrão: relatorios/audit_report.md)

**Exemplos:**
```bash
# Auditar repositório padrão
python audit_orphaned_artifacts.py

# Auditar repositório específico
python audit_orphaned_artifacts.py --repo octocat/Hello-World

# Customizar saída
python audit_orphaned_artifacts.py --output /tmp/my_audit.md
```

## Interpretação de Relatórios

### Estrutura do Relatório

Cada relatório contém:

1. **Sumário Executivo:** Tabela com contagem de artefatos por categoria
2. **Branches Órfãs:** Lista de branches não mescladas sem PRs
3. **Pull Requests Não Mesclados:** Dividido em:
   - PRs abertos
   - PRs fechados não mesclados
   - PRs stale (>30 dias sem atividade)
4. **Issues Órfãs:** Dividido em:
   - Issues sem vínculo com PRs
   - Issues stale (>60 dias sem atividade)
5. **Recomendações:** Sugestões de ação

### Critérios de Classificação

#### Branches Órfãs
- **Critério:** Branch possui commits não mesclados na master E não possui PR associado
- **Ação sugerida:** Avaliar se deve ser removida, associada a PR ou mesclada

#### PRs Não Mesclados
- **Critério:** PR não possui merge commit
- **Estados:**
  - **Aberto:** PR ainda está ativo
  - **Fechado não mesclado:** PR foi fechado sem merge
  - **Stale:** PR sem atividade há mais de 30 dias
- **Ação sugerida:** Revisar, atualizar, mesclar ou fechar definitivamente

#### Issues Órfãs
- **Critério:** Issue aberta sem referência em PRs (via #123)
- **Estados:**
  - **Sem vínculo:** Issue ativa sem vínculo identificado
  - **Stale:** Issue sem atividade há mais de 60 dias
- **Ação sugerida:** Vincular a PR, milestone, projeto ou fechar se não for mais relevante

### Localização de Relatórios

- **Históricos:** `auditoria_artefatos_orfaos/relatorios/audit_report_[RUN_NUMBER].md`
- **Último relatório:** `auditoria_artefatos_orfaos/relatorios/latest_report.md`
- **Artifacts:** Disponíveis na aba Actions por 90 dias

## Checklist de Revisão Manual

Ao revisar um relatório de auditoria, siga este checklist:

- [ ] **Analisar branches órfãs**
  - [ ] Identificar branches que podem ser removidas
  - [ ] Verificar se alguma branch precisa de PR
  - [ ] Documentar decisões no changelog do subprojeto
  
- [ ] **Revisar PRs não mesclados**
  - [ ] PRs abertos: revisar status e necessidade de merge
  - [ ] PRs fechados: avaliar se devem ser reabertos ou arquivados
  - [ ] PRs stale: decidir entre reativar, mesclar ou fechar
  
- [ ] **Avaliar issues órfãs**
  - [ ] Issues sem vínculo: vincular a PRs ou milestones
  - [ ] Issues stale: atualizar status ou fechar
  - [ ] Documentar decisões em comentários nas issues

- [ ] **Registrar decisões**
  - [ ] Atualizar painel central de subprojetos
  - [ ] Registrar ações tomadas no changelog
  - [ ] Criar ata se necessário para decisões importantes

## Troubleshooting

### Erro: GITHUB_TOKEN não configurado
```
❌ Erro: GITHUB_TOKEN não configurado.
```
**Solução:** Configure a variável de ambiente com seu token do GitHub:
```bash
export GITHUB_TOKEN=seu_token_aqui
```

### Erro 401: Unauthorized
```
Erro na requisição: 401 - Unauthorized
```
**Causas possíveis:**
- Token inválido ou expirado
- Token sem permissões necessárias (`repo`, `read:org`)

**Solução:** Gere um novo token com as permissões corretas.

### Erro 403: Rate limit exceeded
```
Erro na requisição: 403 - Forbidden
```
**Causa:** Limite de taxa da API do GitHub excedido (5000 requests/hora autenticado)

**Solução:** Aguarde reset do limite ou use token com limite maior.

### Nenhum artefato encontrado
Se o relatório mostra "✅" em todas as categorias, significa que não há artefatos órfãos detectados. Isso é bom!

### Script não encontra branches/PRs/issues conhecidos
**Causas possíveis:**
- Repositório incorreto especificado
- Permissões insuficientes no token
- Branch padrão diferente de "master"

**Solução:** Verifique o repositório e permissões. Se usar branch padrão diferente, ajuste `default_branch` no script.

## Integração com Governança

### Atualização do Painel Central

Após cada ciclo de auditoria, atualize o [painel central de subprojetos](../../.github/painel_subprojetos.md):

1. Acesse `auditoria_artefatos_orfaos` no painel
2. Atualize "Última Atualização" com a data da auditoria
3. Documente pendências identificadas na seção detalhada

### Registro em Changelog

Decisões importantes devem ser registradas no [CHANGELOG.md](../CHANGELOG.md):

```markdown
## [AAAA-MM-DD] Ciclo de Auditoria #N

### Artefatos Identificados
- X branches órfãs
- Y PRs não mesclados
- Z issues órfãs

### Ações Tomadas
- Removidas branches: [lista]
- PRs mesclados: [lista]
- Issues fechadas: [lista]

### Decisões
- [Descrever decisões relevantes]
```

### Criação de Atas

Para ciclos com decisões estratégicas, crie ata em `debates/ATA_AUDITORIA_AAAA-MM-DD.md`.

## Expansão Futura

O sistema pode ser expandido para incluir:

- **Auditoria de workflows inativos:** GitHub Actions sem execuções recentes
- **Arquivos órfãos:** Scripts, templates ou documentos não referenciados
- **Dependências obsoletas:** Bibliotecas desatualizadas ou não utilizadas
- **Notificações:** Alertas automáticos para artefatos críticos
- **Dashboard:** Visualização gráfica de métricas ao longo do tempo

Sugestões e contribuições são bem-vindas via issues ou PRs!

---

> Para dúvidas ou problemas, abra uma issue no repositório ou consulte o [README do subprojeto](../README.md).
