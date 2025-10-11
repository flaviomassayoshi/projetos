# Script de Auditoria de Artefatos Órfãos

## Visão Geral

`audit_orphaned_artifacts.py` é um script Python que audita repositórios GitHub em busca de artefatos órfãos:
- Branches não mescladas sem PRs associados
- Pull Requests não mesclados (abertos, fechados, stale)
- Issues abertas sem vínculo com PRs

## Características

- **Sem dependências externas:** Usa apenas biblioteca padrão do Python (urllib, json)
- **GitHub API v3:** Compatível com tokens de autenticação padrão
- **Relatórios markdown:** Formato legível e versionável
- **Configurável:** Parâmetros via linha de comando
- **Robusto:** Tratamento de erros, rate limits e edge cases

## Requisitos

- Python 3.12+ (funciona com 3.8+)
- Token GitHub com permissões:
  - `repo` (acesso completo a repositórios privados)
  - `read:org` (se for repositório de organização)

## Uso

### Configuração Básica

```bash
# 1. Configure o token
export GITHUB_TOKEN=ghp_seu_token_aqui

# 2. Execute o script
python3 audit_orphaned_artifacts.py
```

### Opções Avançadas

```bash
# Auditar repositório específico
python3 audit_orphaned_artifacts.py --repo octocat/Hello-World

# Customizar arquivo de saída
python3 audit_orphaned_artifacts.py --output /tmp/audit.md

# Combinação de opções
python3 audit_orphaned_artifacts.py \
  --repo flaviomassayoshi/ScarecrowLab \
  --output ../relatorios/custom_audit.md
```

### Help

```bash
python3 audit_orphaned_artifacts.py --help
```

## Estrutura do Script

### Classes Principais

1. **GitHubAPIClient**
   - Gerencia comunicação com GitHub API
   - Handles autenticação, rate limits e erros
   - Métodos: `get_branches`, `get_pull_requests`, `get_issues`, `compare_branches`

2. **ArtifactAuditor**
   - Executa lógica de auditoria
   - Identifica artefatos órfãos
   - Métodos: `audit_branches`, `audit_pull_requests`, `audit_issues`

3. **ReportGenerator**
   - Gera relatórios markdown estruturados
   - Formata tabelas e estatísticas
   - Método: `generate`

### Fluxo de Execução

```
1. Parse argumentos CLI
2. Validar GITHUB_TOKEN
3. Inicializar cliente API
4. Auditar branches órfãs
   → Listar branches
   → Verificar PRs associados
   → Comparar com master
5. Auditar PRs não mesclados
   → Listar todos os PRs
   → Filtrar não mesclados
   → Classificar (abertos, fechados, stale)
6. Auditar issues órfãs
   → Listar issues abertas
   → Buscar referências em PRs
   → Identificar stale
7. Gerar relatório markdown
8. Salvar em arquivo
```

## Critérios de Classificação

### Branches Órfãs
- **Condição:** Branch tem commits não mesclados na master AND sem PR associado
- **Dados coletados:** Nome, commits à frente, último commit (data, autor, SHA)

### PRs Não Mesclados
- **Condição:** PR sem `merged_at`
- **Categorias:**
  - **Abertos:** Estado `open`
  - **Fechados não mesclados:** Estado `closed` sem merge
  - **Stale:** Sem atualização há >30 dias
- **Dados coletados:** Número, título, autor, branch, datas

### Issues Órfãs
- **Condição:** Issue aberta sem referência `#123` em body de PRs
- **Categorias:**
  - **Sem vínculo:** Issue ativa sem referência identificada
  - **Stale:** Sem atualização há >60 dias
- **Dados coletados:** Número, título, autor, labels, datas

## Configurações

### Thresholds (Limites)

Valores configuráveis no código:

```python
# Em ArtifactAuditor.audit_pull_requests():
stale_threshold = now - timedelta(days=30)  # PRs stale

# Em ArtifactAuditor.audit_issues():
stale_threshold = now - timedelta(days=60)  # Issues stale
```

### Branch Padrão

```python
# Em ArtifactAuditor.__init__():
self.default_branch = "master"  # Ajustar se usar 'main' ou outro
```

## Tratamento de Erros

### Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `GITHUB_TOKEN não configurado` | Variável de ambiente ausente | `export GITHUB_TOKEN=...` |
| `401 Unauthorized` | Token inválido/expirado | Gerar novo token |
| `403 Forbidden` | Rate limit excedido | Aguardar reset |
| `404 Not Found` | Repositório não encontrado/sem acesso | Verificar nome e permissões |

### Rate Limits

- **Autenticado:** 5000 requests/hora
- **Não autenticado:** 60 requests/hora

O script **não** implementa retry automático. Para grandes repositórios, considere:
- Executar em horários de baixa utilização
- Usar token com limite maior (GitHub App)
- Implementar paginação otimizada

## Formato do Relatório

### Estrutura

```markdown
# Relatório de Auditoria — Artefatos Órfãos

**Repositório:** owner/repo
**Data/Hora:** YYYY-MM-DD HH:MM UTC
**Gerado por:** audit_orphaned_artifacts.py

---

## Sumário Executivo
[Tabela com contagens]

---

## 1. Branches Órfãs
[Tabela com branches]

---

## 2. Pull Requests Não Mesclados
### 2.1 PRs Abertos
### 2.2 PRs Fechados Não Mesclados
### 2.3 PRs Stale

---

## 3. Issues Órfãs
### 3.1 Issues Sem Vínculo com PRs
### 3.2 Issues Stale

---

## Recomendações
[Sugestões de ação]
```

### Exemplo de Saída

Ver `../relatorios/` para exemplos de relatórios gerados.

## Extensões Futuras

Possíveis melhorias:

- [ ] **Paginação:** Suporte a repositórios com >100 branches/PRs/issues
- [ ] **Paralelização:** Requisições concorrentes para melhor performance
- [ ] **Cache:** Armazenar resultados intermediários
- [ ] **Filtros:** Excluir branches/PRs/issues específicos via regex
- [ ] **Notificações:** Integração com Slack, Discord, email
- [ ] **Métricas:** Coletar estatísticas ao longo do tempo
- [ ] **Dashboard:** Visualização gráfica dos dados
- [ ] **Ações automatizadas:** Fechar/arquivar artefatos baseado em regras

## Licença

Parte do projeto ScarecrowLab. Consulte LICENSE no repositório principal.

## Contribuindo

Para contribuir:
1. Abra issue descrevendo a melhoria/bug
2. Fork do repositório
3. Crie branch `feature/sua-feature`
4. Commit com mensagens descritivas
5. Abra PR vinculando à issue

## Suporte

Para dúvidas ou problemas:
- Consulte [Manual de Uso](../docs/MANUAL_USO.md)
- Abra issue no repositório
- Entre em contato com mantenedores

---

> Script criado como parte do subprojeto [auditoria_artefatos_orfaos](../README.md) do ScarecrowLab.
