# Critérios de Classificação — Scarecrow AutoFlow

> Regras detalhadas para classificação automática de issues e pull requests.

---

## Visão Geral

O classificador analisa metadados e conteúdo de issues/PRs para determinar a categoria apropriada:
- **auto-merge:** Aprovação automática imediata
- **needs-simulation:** Requer deliberação simulada entre personas
- **manual-review:** Requer revisão humana obrigatória

## Metadados Analisados

### Issues
- **Labels:** Presença de labels específicos (bug, documentation, enhancement, etc.)
- **Milestone:** Associação com milestone crítico ou não
- **Assignees:** Número de assignees (múltiplos podem indicar complexidade)
- **Template usado:** Qual template de issue foi utilizado
- **Tamanho:** Número de caracteres no corpo da issue

### Pull Requests
- **Arquivos modificados:** Número e tipo de arquivos alterados
- **Linhas modificadas:** Total de adições/remoções
- **Labels:** Similar a issues
- **Branch base:** Se é merge para main/master ou outra branch
- **Conflitos:** Presença de conflitos de merge
- **Testes:** Status de CI/CD checks

## Regras de Classificação

### Categoria: auto-merge

**Condições necessárias (TODAS devem ser atendidas):**

#### Para Issues
1. Usa template oficial (`.github/ISSUE_TEMPLATE/issue-lab.md` ou similar)
2. Label presente: `documentation`, `typo`, `dependencies` OU `good first issue`
3. NÃO possui labels: `breaking-change`, `security`, `architecture`, `manifesto`
4. Tamanho < 2000 caracteres
5. NÃO menciona artefatos críticos: manifesto consolidado, copilot-instructions.md, fluxos centrais
6. Checklist embutido está completamente preenchido (se aplicável)

#### Para Pull Requests
1. Modificações apenas em:
   - Arquivos .md em subprojetos (exceto README.md de raiz)
   - Arquivos de documentação (docs/, debates/, checklists/)
   - Correções de typos
   - package.json/requirements.txt (apenas version bumps minor/patch)
2. Total de linhas modificadas ≤ 100
3. NÃO modifica:
   - `.github/copilot-instructions.md`
   - `.github/copilot-diretrizes/*.md`
   - `ManifestoMCP.md`
   - `.github/workflows/*.yml`
   - Scripts de automação (scripts/, python_apps/)
4. Todos os checks CI/CD passaram (verde)
5. Sem conflitos de merge
6. Label presente: `documentation`, `typo`, `dependencies`
7. NÃO possui labels: `breaking-change`, `security`, `needs-discussion`

**Exemplos de auto-merge:**
- Correção de typo em README de subprojeto
- Atualização de data/status em CHANGELOG
- Adição de link em documentação
- Atualização de dependência patch (1.2.3 -> 1.2.4)

### Categoria: needs-simulation

**Condições necessárias (PELO MENOS UMA deve ser atendida):**

#### Para Issues
1. Propõe criação de novo subprojeto
2. Propõe alteração em template existente
3. Propõe alteração em diretriz não-crítica
4. Label presente: `enhancement`, `proposal`, `governance`
5. Menciona múltiplos subprojetos ou integrações
6. Tamanho entre 2000-5000 caracteres
7. NÃO se qualifica para auto-merge nem manual-review

#### Para Pull Requests
1. Modifica múltiplos arquivos em diferentes subprojetos
2. Adiciona novo template ou checklist
3. Modifica estrutura de diretórios
4. Total de linhas modificadas entre 100-500
5. Modifica scripts não-críticos
6. Label presente: `enhancement`, `refactor`, `governance`
7. NÃO se qualifica para auto-merge nem manual-review

**Exemplos de needs-simulation:**
- Proposta de novo template de checklist
- Reorganização de estrutura de docs/ em subprojeto
- Alteração em script de validação não-crítico
- Atualização de múltiplos READMEs com novo padrão

### Categoria: manual-review

**Condições necessárias (PELO MENOS UMA deve ser atendida):**

#### Para Issues
1. Label presente: `breaking-change`, `security`, `architecture`, `manifesto`, `critical`
2. Propõe alteração no manifesto consolidado
3. Propõe alteração em copilot-instructions.md ou anexos principais
4. Propõe mudança em princípios centrais do laboratório
5. Tamanho > 5000 caracteres (alta complexidade)
6. Menciona mudança estratégica ou de identidade do lab
7. Criada por usuário sem histórico de contribuições (primeira issue)

#### Para Pull Requests
1. Modifica arquivos críticos:
   - `.github/copilot-instructions.md`
   - `.github/copilot-diretrizes/*.md` (diretrizes principais)
   - `ManifestoMCP.md`
   - `.github/workflows/*.yml`
   - Scripts de automação críticos
2. Total de linhas modificadas > 500
3. Label presente: `breaking-change`, `security`, `architecture`, `needs-discussion`
4. Falha em checks CI/CD críticos
5. Conflitos de merge presentes
6. Modifica múltiplos subprojetos com impacto estrutural
7. Criada por usuário sem histórico de contribuições (primeiro PR)

**Exemplos de manual-review:**
- Alteração no manifesto consolidado
- Mudança em fluxo operacional central
- Novo GitHub Actions workflow
- Refatoração de estrutura de múltiplos subprojetos
- Mudança em script crítico de automação

## Regras de Prioridade

**Ordem de avaliação:**
1. Verificar se qualifica para manual-review (caso positivo, classificar e parar)
2. Verificar se qualifica para auto-merge (caso positivo, classificar e parar)
3. Classificar como needs-simulation (categoria padrão)

**Justificativa:** Segurança primeiro (manual-review), depois automação agressiva (auto-merge), depois deliberação (needs-simulation).

## Casos Especiais

### Issues/PRs com Label Explícito

Se issue/PR possui label:
- `autoflow:auto-merge` → Forçar auto-merge (sobrescreve regras, mas mantém validação)
- `autoflow:needs-simulation` → Forçar needs-simulation
- `autoflow:manual-review` → Forçar manual-review
- `autoflow:skip` → Não processar automaticamente

**Justificativa:** Permitir override manual quando necessário.

### Issues/PRs Criados por Bots

Issues/PRs criados por:
- `dependabot[bot]`
- `github-actions[bot]`
- Bots conhecidos do lab

**Regra:** Classificar normalmente, mas aplicar critérios mais lenientes para auto-merge (ex: aceitar dependências major se descrição explicar breaking changes).

### Pull Requests em Draft

PRs marcados como draft:
**Regra:** Classificar como `autoflow:skip` até que draft seja removido.

**Justificativa:** Respeitar intenção do autor de não mergear ainda.

## Métricas de Qualidade

Para cada classificação, calcular "score de confiança" (0-100):
- **100:** Todos os critérios claramente atendidos
- **75-99:** Maioria dos critérios atendidos
- **50-74:** Critérios atendidos com ressalvas
- **0-49:** Critérios parcialmente atendidos ou ambíguos

**Regra de segurança:** Se score < 75 para auto-merge, reclassificar como needs-simulation.

## Evolução Contínua

### Ajustes Baseados em Feedback

- Revisar mensalmente decisões auto-merge revertidas → ajustar critérios
- Coletar feedback de revisores humanos em manual-review → identificar padrões
- Analisar tempo de resolução em needs-simulation → otimizar personas

### Versionamento de Critérios

Cada versão deste documento deve:
1. Registrar data e responsável
2. Explicar mudanças em relação à versão anterior
3. Justificar ajustes com dados ou feedback

---

**Versão:** 1.0  
**Data:** 2025-10-11  
**Responsável:** GitHub Copilot  
**Próxima Revisão:** 2025-11-11 ou após 100 classificações  

---

> Este documento é vivo e deve evoluir baseado em uso real do sistema.
