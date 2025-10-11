# Guia de Uso — Scarecrow AutoFlow

> Como usar o sistema de aprovação automatizada (para contribuidores e mantenedores).

---

## Para Contribuidores

### Criando Issues

**O sistema classifica automaticamente sua issue quando você:**
1. Abre uma nova issue no repositório
2. Usa template oficial (recomendado)
3. Adiciona labels apropriados

**Labels importantes:**
- `documentation`: Mudanças apenas em documentação → candidato a auto-merge
- `typo`: Correção de erros de digitação → candidato a auto-merge
- `enhancement`: Melhoria ou nova funcionalidade → candidato a needs-simulation
- `breaking-change`: Mudança que quebra compatibilidade → forçará manual-review
- `security`: Questões de segurança → forçará manual-review

**O que acontece depois:**
- Sistema adiciona label `autoflow:auto-merge`, `autoflow:needs-simulation` ou `autoflow:manual-review`
- Para auto-merge: aprovação e fechamento automático (se validação OK)
- Para needs-simulation: rodada de debate simulado entre personas
- Para manual-review: aguarda revisão humana

### Criando Pull Requests

**O sistema classifica automaticamente seu PR quando você:**
1. Abre um novo PR
2. Preenche descrição clara do que foi alterado
3. Aguarda conclusão de checks CI/CD

**Dicas para aprovação rápida:**
- **Para auto-merge:**
  - Faça PRs pequenos (≤ 100 linhas)
  - Modifique apenas documentação ou correções simples
  - Garanta que todos os checks CI/CD passem
  - Use labels `documentation` ou `typo`
  
- **Para needs-simulation:**
  - PRs de complexidade média (100-500 linhas)
  - Mudanças em templates ou scripts não-críticos
  - Use labels `enhancement` ou `refactor`
  
- **Manual-review (inevitável):**
  - PRs grandes (> 500 linhas)
  - Mudanças em arquivos críticos (manifesto, diretrizes principais, workflows)
  - Primeiro PR no repositório

**O que acontece depois:**
- Sistema adiciona label de classificação
- Para auto-merge: merge automático após validação
- Para needs-simulation: debate simulado + decisão em minutos
- Para manual-review: aguarda reviewer humano

### Forçando Classificação Específica

**Quando usar:**
- Você sabe que seu PR deve ser auto-merge, mas sistema classifica como needs-simulation
- Você quer pular simulação e ir direto para manual-review

**Como fazer:**
Adicione label manualmente:
- `autoflow:auto-merge` → Força tentativa de auto-merge (ainda valida conformidade)
- `autoflow:needs-simulation` → Força simulação
- `autoflow:manual-review` → Força revisão humana
- `autoflow:skip` → Desabilita processamento automático

**Nota:** Forçar auto-merge não pula validação de conformidade. Se validação falhar, será reclassificado.

### Respondendo a Feedback de Simulação

**Quando seu PR recebe `needs-simulation`:**
1. Sistema gera ata de simulação em comentário do PR
2. Ata contém análise de 3 personas + decisão + recomendações
3. Leia as recomendações e ajuste seu PR se necessário
4. Push de novos commits re-trigga validação

**Exemplo de ata:**
```markdown
## Simulação AutoFlow

**Decisão:** Aprovado com ajustes

**Recomendações:**
- Adicionar exemplo prático no template (Engenheiro de Prompt)
- Incluir link para glossário (Guardião do Manifesto)
- Atualizar tests de integração (DevOps Modular)

Após ajustes, PR será aprovado automaticamente.
```

## Para Mantenedores

### Monitorando Decisões Automatizadas

**Dashboard (futuro):**
- Taxa de automação por categoria
- Tempo médio de aprovação
- Decisões revertidas (falsos positivos)

**Logs de decisões:**
- Todas as decisões são registradas em `scarecrow_autoflow/decisoes_automatizadas/`
- Estrutura: `YYYY-MM-DD_[tipo]_[id].md`
- Conteúdo: categoria, critérios, resultado, personas (se simulado)

**Exemplo de navegação:**
```bash
# Ver decisões de hoje
ls scarecrow_autoflow/decisoes_automatizadas/2025-10-11_*.md

# Ver decisões de auto-merge
ls scarecrow_autoflow/decisoes_automatizadas/*_automerge_*.md

# Ver simulações
ls scarecrow_autoflow/decisoes_automatizadas/*_simulation_*.md
```

### Revisando Decisões de Simulação

**Quando revisar:**
- Issue/PR marcado como `autoflow:needs-simulation`
- Ata de simulação gerada em comentário
- Resultado: "Aprovado com ajustes" ou "Manual-review recomendado"

**Como revisar:**
1. Leia a ata completa de simulação
2. Verifique análises das 3 personas
3. Valide consenso e justificativa
4. Se concordar: aprove o PR
5. Se discordar: adicione comentário explicando e reclassifique

**Revertendo decisão:**
- Adicione label `autoflow:override-manual`
- Adicione comentário explicando razão
- Sistema registra reversão no log

### Ajustando Critérios de Classificação

**Quando ajustar:**
- Taxa de falsos positivos > 10%
- Muitos auto-merges sendo revertidos
- Muitos manual-reviews que poderiam ser automatizados

**Como ajustar:**
1. Edite `scarecrow_autoflow/docs/CRITERIOS_CLASSIFICACAO.md`
2. Atualize regras e limiares
3. Documente mudanças no CHANGELOG
4. Crie PR com label `autoflow:config`
5. Teste ajustes em ambiente de staging (futuro)

### Ajustando Regras de Validação

**Quando ajustar:**
- Validações reprovando incorretamente
- Novas conformidades necessárias
- Feedback recorrente de contribuidores

**Como ajustar:**
1. Edite `scarecrow_autoflow/docs/REGRAS_VALIDACAO.md`
2. Atualize checklists e pesos
3. Documente mudanças no CHANGELOG
4. Teste com PRs históricos

### Configurando Personas de Simulação

**Quando ajustar:**
- Simulações gerando consenso artificial
- Perspectivas importantes faltando
- Feedback de qualidade baixa

**Como ajustar:**
1. Edite `scarecrow_autoflow/docs/PROCESSO_SIMULACAO.md`
2. Ajuste critérios de cada persona
3. Atualize prompts/regras no script `simulador.py`
4. Teste com casos conhecidos

## Workflows Automáticos

### Issues

**Trigger:** `issues: opened`, `issues: labeled`

**Fluxo:**
1. Classificador analisa issue → adiciona label
2. Se auto-merge: valida conformidade → fecha issue com comentário
3. Se needs-simulation: simula debate → adiciona comentário com ata
4. Se manual-review: apenas adiciona label, aguarda humano

### Pull Requests

**Trigger:** `pull_request: opened`, `pull_request: synchronize`, `pull_request: labeled`

**Fluxo:**
1. Aguarda conclusão de CI/CD checks
2. Classificador analisa PR → adiciona label
3. Se auto-merge: valida conformidade → merge automático
4. Se needs-simulation: simula debate → adiciona comentário com ata → merge se aprovado
5. Se manual-review: apenas adiciona label, aguarda humano

### Re-classificação

**Trigger:** `pull_request: synchronize` (novos commits)

**Fluxo:**
1. Remove label antigo de classificação
2. Re-executa classificador
3. Re-executa validador
4. Adiciona novo label
5. Atualiza comentário com nova decisão

## Comandos Customizados (Futuro)

### Via Comentários

**Sintaxe:** `/autoflow [comando]`

**Comandos planejados:**
- `/autoflow reclassify` → Re-executa classificação
- `/autoflow force-merge` → Tenta auto-merge (requer permissão)
- `/autoflow simulate` → Força simulação
- `/autoflow skip` → Desabilita automação
- `/autoflow status` → Mostra status e logs

## Troubleshooting

### Issue/PR não foi classificado

**Causas possíveis:**
- Workflow não foi trigado (verifique Actions)
- Issue/PR está em draft (sistema pula drafts)
- Label `autoflow:skip` presente

**Solução:**
- Remova draft
- Remova `autoflow:skip`
- Adicione/remova label qualquer para re-trigar

### Auto-merge falhou

**Causas possíveis:**
- Validação de conformidade reprovou
- Conflitos de merge presentes
- CI/CD checks falharam

**Solução:**
- Leia comentário do sistema com detalhes da falha
- Corrija problemas identificados
- Push novos commits

### Simulação inconclusiva

**Causas possíveis:**
- Dissenso entre personas
- Critérios ambíguos

**Solução:**
- Sistema automaticamente marca como manual-review
- Revisor humano avalia e decide

### Decisão errada do sistema

**Causas possíveis:**
- Critérios de classificação imprecisos
- Validação incompleta

**Solução:**
- Adicione label `autoflow:override-manual`
- Comente explicando o erro
- Mantenedor ajusta critérios para evitar repetição

## Métricas e Relatórios (Futuro)

### Dashboard de Governança

**Métricas rastreadas:**
- Taxa de automação por categoria
- Tempo médio de aprovação
- Taxa de conformidade (sem reversão)
- Cobertura de classificação

**Acesso:**
- GitHub Pages: `https://[repo].github.io/scarecrow-autoflow/dashboard`
- Atualização: diária via GitHub Actions

## Suporte

**Para dúvidas:**
- Abra issue com label `question` + `autoflow`
- Consulte documentação técnica em `scarecrow_autoflow/docs/`

**Para reportar bugs:**
- Abra issue com label `bug` + `autoflow`
- Inclua link para issue/PR afetado
- Inclua log da decisão (se disponível)

**Para sugerir melhorias:**
- Abra issue com label `enhancement` + `autoflow`
- Descreva problema atual e solução proposta

---

**Versão:** 1.0  
**Data:** 2025-10-11  
**Última Atualização:** 2025-10-11  

---

> Este guia evolui com o sistema. Feedback é bem-vindo!
