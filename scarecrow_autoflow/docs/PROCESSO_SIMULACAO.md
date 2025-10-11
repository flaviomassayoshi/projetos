# Processo de Simulação — Scarecrow AutoFlow

> Funcionamento da simulação de decisões por personas especializadas.

---

## Visão Geral

Para issues/PRs classificados como **needs-simulation**, o sistema simula uma rodada de debate entre personas especializadas do laboratório, gerando ata rastreável e decisão fundamentada.

**Objetivo:** Aproximar qualidade de decisão humana multi-perspectiva através de simulação automatizada.

## Personas Participantes

### 1. Engenheiro de Prompt

**Perfil:**
- Especialista em prompts, templates e comunicação clara
- Foco em efetividade e manutenibilidade de instruções
- Perspectiva: "Este prompt/template é claro e útil?"

**Critérios de Avaliação:**
- Clareza da linguagem
- Completude de instruções
- Ausência de ambiguidades
- Facilidade de uso por agentes/humanos
- Exemplos práticos incluídos

**Voto:** Aprovar / Aprovar com ajustes / Rejeitar

### 2. Guardião do Manifesto

**Perfil:**
- Especialista em governança e conformidade institucional
- Foco em rastreabilidade e aderência a princípios
- Perspectiva: "Isto está alinhado com o arcabouço?"

**Critérios de Avaliação:**
- Conformidade com manifesto consolidado
- Respeito aos princípios centrais
- Rastreabilidade de decisões
- Consistência terminológica (glossário)
- Impacto em governança

**Voto:** Aprovar / Aprovar com ajustes / Rejeitar

### 3. DevOps Modular

**Perfil:**
- Especialista em automação, CI/CD e infraestrutura
- Foco em modularidade e integrações
- Perspectiva: "Isto é automatizável e integrável?"

**Critérios de Avaliação:**
- Modularidade da solução
- Viabilidade de automação
- Integração com sistemas existentes
- Performance e escalabilidade
- Manutenibilidade técnica

**Voto:** Aprovar / Aprovar com ajustes / Rejeitar

## Fluxo de Simulação

### Etapa 1: Análise Individual

Cada persona recebe:
- Conteúdo completo do issue/PR
- Contexto de classificação (por que needs-simulation)
- Resultado de validação de conformidade
- Links para artefatos relacionados

Cada persona produz:
- Análise escrita dos critérios relevantes
- Lista de pontos positivos
- Lista de pontos de atenção/melhoria
- Voto preliminar (Aprovar / Aprovar com ajustes / Rejeitar)

### Etapa 2: Deliberação

Sistema consolida análises e identifica:
- **Consenso total:** Todos aprovam OU todos rejeitam
- **Consenso parcial:** Maioria aprova/rejeita, minoria diverge
- **Dissenso:** Empate ou divergências significativas

**Regras de deliberação:**

**Caso 1: Consenso Total (Aprovação)**
- Todos votam "Aprovar" ou "Aprovar com ajustes"
- Decisão: **Aprovado para merge**
- Ata: Registra análises e consenso

**Caso 2: Consenso Total (Rejeição)**
- Todos votam "Rejeitar"
- Decisão: **Rejeitado, classificar como manual-review**
- Ata: Registra razões de rejeição

**Caso 3: Consenso Parcial (Aprovação)**
- 2 de 3 personas votam "Aprovar" ou "Aprovar com ajustes"
- Decisão: **Aprovado com ajustes** (merge após ajustes menores)
- Ata: Registra análises, voto majoritário e pontos de atenção da minoria

**Caso 4: Consenso Parcial (Rejeição)**
- 2 de 3 personas votam "Rejeitar"
- Decisão: **Rejeitado, classificar como manual-review**
- Ata: Registra razões de rejeição e pontos da minoria

**Caso 5: Dissenso**
- Empate ou divergências irreconciliáveis
- Decisão: **Classificar como manual-review** (desempate humano)
- Ata: Registra todas as perspectivas e razão do dissenso

### Etapa 3: Geração de Ata

Sistema gera ata estruturada no formato:

```markdown
# Ata de Simulação — [Título do Issue/PR]

**Issue/PR:** #[número]  
**Data:** YYYY-MM-DD HH:MM  
**Categoria:** needs-simulation  
**Personas:** Engenheiro de Prompt, Guardião do Manifesto, DevOps Modular

---

## Contexto

[Resumo do issue/PR e razão para needs-simulation]

## Análises das Personas

### Engenheiro de Prompt

**Voto:** [Aprovar / Aprovar com ajustes / Rejeitar]

**Análise:**
[Texto da análise]

**Pontos Positivos:**
- [Lista]

**Pontos de Atenção:**
- [Lista]

### Guardião do Manifesto

[Mesma estrutura]

### DevOps Modular

[Mesma estrutura]

## Deliberação

**Resultado dos Votos:**
- Aprovar: X
- Aprovar com ajustes: Y
- Rejeitar: Z

**Tipo de Consenso:** [Consenso total / Consenso parcial / Dissenso]

**Decisão Final:** [Aprovado / Aprovado com ajustes / Rejeitado / Manual-review]

**Justificativa:**
[Explicação da decisão baseada nos votos e análises]

## Recomendações

**Para o Autor:**
[Lista de ações sugeridas]

**Para Revisores (se manual-review):**
[Pontos de atenção para revisão humana]

## Rastreabilidade

**Log da Decisão:** decisoes_automatizadas/YYYY-MM-DD_simulation_[ID].md  
**Artefatos Relacionados:** [Links]  
**Próximos Passos:** [Ações]

---

**Assinatura Digital:** Scarecrow AutoFlow v1.0, 2025-10-11
```

## Implementação Técnica

### Simulação de Personas

**Abordagem 1: Prompts Especializados**
- Cada persona = prompt específico com contexto e critérios
- LLM (GPT-4, Claude, etc.) gera análise para cada persona
- Sistema consolida resultados

**Abordagem 2: Regras Determinísticas**
- Cada persona = conjunto de regras de validação
- Sistema aplica regras e gera análise estruturada
- Mais previsível, menos flexível

**Recomendação:** Abordagem 1 para MVP (maior flexibilidade), evoluir para híbrido (regras + LLM).

### Parâmetros de Entrada

Cada persona recebe JSON estruturado:

```json
{
  "issue_pr": {
    "number": 123,
    "type": "pull_request",
    "title": "...",
    "body": "...",
    "labels": [...],
    "files_changed": [...]
  },
  "classification": {
    "category": "needs-simulation",
    "confidence_score": 85,
    "reason": "Proposes new template"
  },
  "validation": {
    "conformity_score": 78,
    "approved": true,
    "concerns": [...]
  },
  "context": {
    "related_artifacts": [...],
    "subproject": "governance_templates"
  }
}
```

### Parâmetros de Saída

Cada persona retorna JSON estruturado:

```json
{
  "persona": "Engenheiro de Prompt",
  "vote": "aprovar_com_ajustes",
  "confidence": 80,
  "analysis": {
    "summary": "...",
    "positive_points": [...],
    "concerns": [...],
    "recommendations": [...]
  }
}
```

## Casos de Teste

### Caso 1: Novo Template de Checklist

**Input:** PR adicionando novo template em `.github/TEMPLATE_CHECKLIST_EXECUCAO.md`

**Análise Esperada:**
- Engenheiro de Prompt: Aprovar (template claro e útil)
- Guardião do Manifesto: Aprovar com ajustes (adicionar referência ao glossário)
- DevOps Modular: Aprovar (template facilita automação)

**Decisão Esperada:** Aprovado com ajustes

### Caso 2: Alteração em Diretriz de Debate

**Input:** PR modificando `.github/copilot-diretrizes/diretrizes_debate.md`

**Análise Esperada:**
- Engenheiro de Prompt: Aprovar com ajustes (alguns exemplos podem ser mais claros)
- Guardião do Manifesto: Aprovar (mantém conformidade)
- DevOps Modular: N/A (impacto técnico mínimo)

**Decisão Esperada:** Aprovado com ajustes

### Caso 3: Reestruturação de Múltiplos Subprojetos

**Input:** PR movendo arquivos entre subprojetos e alterando estrutura

**Análise Esperada:**
- Engenheiro de Prompt: Rejeitar (impacto em clareza de navegação)
- Guardião do Manifesto: Rejeitar (rastreabilidade comprometida)
- DevOps Modular: Aprovar com ajustes (melhora modularidade, mas requer ajustes em integrações)

**Decisão Esperada:** Rejeitado (consenso parcial de rejeição)

## Métricas de Qualidade

### Taxa de Consenso
- **Meta:** ≥ 70% de simulações resultem em consenso (total ou parcial)
- **Medição:** (Consensos total + parcial) / Total de simulações

### Taxa de Reversão
- **Meta:** ≤ 10% de decisões "Aprovado" sejam revertidas por humanos
- **Medição:** Aprovações revertidas / Total de aprovações

### Tempo de Simulação
- **Meta:** ≤ 5 minutos por simulação
- **Medição:** Tempo médio de execução do simulador

## Evolução das Personas

### Ajuste de Critérios

Baseado em feedback e métricas:
1. Identificar padrões de decisões revertidas
2. Analisar divergências entre simulação e revisão humana
3. Ajustar pesos e critérios das personas
4. Re-testar com casos históricos

### Adição de Novas Personas

Futuras personas (prioridade baixa):
- **Especialista em Documentação:** Foco em clareza para usuários finais
- **Auditor de Segurança:** Foco em riscos e vulnerabilidades
- **Arquiteto de Dados:** Foco em estrutura e integridade de dados

**Critério:** Adicionar nova persona apenas se métricas indicarem gap de cobertura.

---

**Versão:** 1.0  
**Data:** 2025-10-11  
**Responsável:** GitHub Copilot  
**Próxima Revisão:** 2025-11-11 ou após 30 simulações  

---

> Este processo deve ser transparente, rastreável e evolutivo.
