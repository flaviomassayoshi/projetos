# Regras de Validação — Scarecrow AutoFlow

> Critérios de conformidade com artefatos constitucionais do ScarecrowLab.

---

## Visão Geral

O validador verifica conformidade de issues/PRs com:
- Manifesto consolidado
- Templates oficiais
- Diretrizes do arcabouço
- Princípios centrais do laboratório
- Checklists e padrões estabelecidos

**Resultado:** Aprovado / Reprovado + lista de não-conformidades

## Artefatos de Referência

### Primários (Críticos)
1. `.github/copilot-instructions.md` — Índice central de diretrizes
2. `.github/copilot-diretrizes/glossario.md` — Terminologia oficial
3. `.github/copilot-diretrizes/fluxos_gerais_agentes.md` — Fluxos operacionais
4. `.github/copilot-diretrizes/diretrizes_subprojetos.md` — Regras para subprojetos
5. `ManifestoMCP.md` — Manifesto consolidado

### Secundários (Importantes)
6. `.github/TEMPLATE_SUBPROJETO.md`
7. `.github/TEMPLATE_CHECKLIST.md`
8. `.github/TEMPLATE_PLANO_ACAO.md`
9. `.github/copilot-diretrizes/TEMPLATE_ATA.md`
10. `.github/painel_subprojetos.md` — Status e pendências

## Validações por Tipo

### Issues: Template Oficial

**Checklist:**
- [ ] Usa template `.github/ISSUE_TEMPLATE/issue-lab.md` (se aplicável)
- [ ] Título é claro e descritivo (≥ 10 caracteres)
- [ ] Corpo contém contexto/motivação
- [ ] Labels apropriados aplicados
- [ ] Artefatos relacionados referenciados (se aplicável)
- [ ] Responsável definido ou indicado
- [ ] Critérios de sucesso definidos (para propostas/tarefas)

**Não-conformidades que reprovam:**
- Título vazio ou genérico demais ("Update", "Fix", "Change")
- Corpo vazio ou apenas "TODO"
- Proposta de novo subprojeto sem seguir estrutura mínima

### Pull Requests: Mudanças em Subprojetos

**Checklist:**
- [ ] Se cria novo subprojeto: segue estrutura de TEMPLATE_SUBPROJETO.md
- [ ] README.md presente com seções obrigatórias:
  - Sumário Executivo
  - Proposta Vigente
  - Referências ao Arcabouço
- [ ] CHECKLIST.md presente e estruturado
- [ ] CHANGELOG.md presente com entrada inicial
- [ ] debates/ATA_ABERTURA.md presente (se relevante)
- [ ] Estrutura de diretórios correta (debates/, checklists/, docs/)

**Não-conformidades que reprovam:**
- Novo subprojeto sem README.md
- Novo subprojeto sem CHECKLIST.md
- Estrutura de diretórios inconsistente com padrão

### Pull Requests: Mudanças em Templates

**Checklist:**
- [ ] Template mantém estrutura base esperada
- [ ] Comentários de orientação preservados (<!-- -->)
- [ ] Frontmatter YAML válido (se aplicável)
- [ ] Seções obrigatórias mantidas
- [ ] Mudanças documentadas em PR description

**Não-conformidades que reprovam:**
- Remoção de seções obrigatórias sem justificativa
- Quebra de compatibilidade com uso existente
- Frontmatter YAML inválido

### Pull Requests: Mudanças em Diretrizes

**Checklist:**
- [ ] Alteração justificada em PR description
- [ ] Exemplos atualizados (se aplicável)
- [ ] Glossário atualizado (se introduz novos termos)
- [ ] Não conflita com princípios centrais
- [ ] Mantém tom e estilo de outras diretrizes

**Não-conformidades que reprovam:**
- Contradição com princípios centrais
- Remoção de seção crítica sem substituição
- Introdução de ambiguidade grave

## Validações Semânticas

### Conformidade com Princípios Centrais

**Princípios (de copilot-instructions.md):**
1. Modularização e separação de subprojetos
2. Rastreabilidade total de decisões, entregas e debates
3. Automação de fluxos e validação por checklists
4. Integração transparente entre agentes
5. Uso de templates e comandos padronizados
6. Documentação autoexplicativa e sem dependências externas

**Validação:**
- Issue/PR promove ou mantém estes princípios? (Sim/Não/N/A)
- Issue/PR viola algum destes princípios? (Sim/Não)

**Regra:** Se viola qualquer princípio → Reprovado

### Conformidade com Glossário

**Validação:**
- Termos usados estão definidos no glossário?
- Termos usados de forma consistente com definições?
- Novos termos devem ser adicionados ao glossário?

**Regra:** Se usa termo crítico de forma inconsistente → Reprovado

**Termos críticos:**
- Arcabouço, Artefato persistente, Ata, Changelog, Checklist de entrega, Manifesto, Pendência, Plano de ação, Prompt de retomada, Subprojeto, Tema

### Rastreabilidade

**Validação:**
- Issue/PR referencia artefatos relacionados?
- Issue/PR vincula-se a subprojeto (se aplicável)?
- Issue/PR está listada no painel central (se relevante)?
- Issue/PR contém links bidirecionais corretos?

**Regra:** Para changes de alta complexidade, rastreabilidade é obrigatória. Ausência → Reprovado.

## Checklists Específicos por Fluxo

### Fluxo: Criação de Subprojeto

**Validação estrita:**
1. Estrutura completa criada (README, CHECKLIST, CHANGELOG, debates/, docs/)
2. README contém todas as seções obrigatórias
3. Justificativa clara de não-sobreposição com subprojetos existentes
4. Referências ao arcabouço presentes
5. Integração com painel central documentada

**Reprovação automática se:**
- Estrutura incompleta (falta README ou CHECKLIST)
- README não segue template
- Não documenta relação com outros subprojetos

### Fluxo: Atualização de Diretriz

**Validação estrita:**
1. Mudança justificada com contexto/motivação
2. Exemplos atualizados ou adicionados
3. Changelog da diretriz atualizado (se existir)
4. Não contradiz outras diretrizes
5. Mantém autossuficiência do documento

**Reprovação automática se:**
- Sem justificativa clara
- Contradição com outra diretriz
- Quebra de autossuficiência (adiciona dependência externa)

### Fluxo: Alteração em Template

**Validação estrita:**
1. Template testado com uso real (exemplo fornecido)
2. Retrocompatibilidade mantida ou migração documentada
3. Comentários de orientação atualizados
4. Mudanças não quebram templates derivados

**Reprovação automática se:**
- Quebra retrocompatibilidade sem plano de migração
- Remoção de seção usada em artefatos existentes
- Template resultante é ambíguo ou incompleto

## Validações Automatizadas

### Sintaxe Markdown

**Ferramentas:** markdownlint, markdown-link-check

**Validação:**
- Markdown válido (sem erros de sintaxe)
- Links internos não quebrados
- Imagens/diagramas acessíveis
- Estrutura de headers consistente (H1 único, hierarquia correta)

**Regra:** Erros críticos de markdown → Reprovado

### Frontmatter YAML

**Validação (para templates de issue/PR):**
- YAML válido e parseável
- Campos obrigatórios presentes
- Tipos de dados corretos
- Labels existem no repositório

**Regra:** YAML inválido → Reprovado

### Links e Referências

**Validação:**
- Links relativos corretos (`../.github/` vs `.github/`)
- Arquivos referenciados existem
- Links para painel central corretos
- Links para glossário/diretrizes funcionais

**Regra:** Links quebrados para artefatos críticos → Reprovado

## Pontuação de Conformidade

Cada validação recebe pontuação:
- **Crítica:** 0 (reprovado) ou 10 (aprovado)
- **Importante:** 0-5 pontos
- **Opcional:** 0-2 pontos

**Score final:** Soma de pontos / Total possível × 100

**Regra de aprovação:**
- Score ≥ 90: Aprovado
- Score 75-89: Aprovado com ressalvas (needs-simulation)
- Score < 75: Reprovado

**Exceção:** Qualquer validação crítica reprovada → Reprovação automática, independente do score.

## Logs de Validação

Cada validação gera log estruturado:

```markdown
## Validação — [ID do Issue/PR]

**Data:** YYYY-MM-DD HH:MM  
**Tipo:** Issue | Pull Request  
**Categoria:** [auto-merge | needs-simulation | manual-review]

### Resultados

**Score de Conformidade:** XX/100

**Validações Aprovadas:**
- [x] Template oficial usado
- [x] Princípios centrais respeitados
- ...

**Não-Conformidades:**
- [ ] Link para painel central ausente (Importante, -5 pontos)
- ...

**Decisão:** Aprovado | Reprovado | Aprovado com ressalvas

**Justificativa:** [Explicação da decisão]

**Próximos Passos:** [Ações recomendadas]
```

## Evolução e Ajustes

### Feedback de Revisores Humanos

Quando manual-review resulta em aprovação/rejeição:
- Comparar com validação automatizada
- Identificar gaps ou falsos positivos/negativos
- Ajustar regras e pesos

### Versionamento de Regras

Cada versão deste documento:
1. Registra data e responsável
2. Lista mudanças de regras
3. Justifica ajustes com dados

---

**Versão:** 1.0  
**Data:** 2025-10-11  
**Responsável:** GitHub Copilot  
**Próxima Revisão:** 2025-11-11 ou após 50 validações  

---

> Este documento deve evoluir com base em uso real e feedback de revisores.
