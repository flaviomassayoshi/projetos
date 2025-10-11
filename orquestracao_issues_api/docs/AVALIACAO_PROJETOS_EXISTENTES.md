# Avaliação de Projetos/Subprojetos Existentes

**Data:** 2025-10-11  
**Responsável:** GitHub Copilot  
**Objetivo:** Avaliar se há sobreposição ou conflito com subprojetos existentes antes de criar "Orquestração de Issues via API e Agentes"

## Metodologia

Análise dos subprojetos vigentes no laboratório para identificar:
1. Escopo similar ou sobreposto
2. Funcionalidades que possam conflitar
3. Oportunidades de integração
4. Justificativa para criação como subprojeto independente

## Subprojetos Analisados

### 1. automacao_tarefas_lab

**Escopo:** Automação de tarefas repetitivas do laboratório (atualização de painéis, geração de changelogs, validação de checklists).

**Sobreposição identificada:** Parcial
- automacao_tarefas_lab foca em automações internas do laboratório
- Não aborda especificamente orquestração de issues via API do GitHub
- Não trata de agentes externos atuando sobre issues

**Conclusão:** Complementar, não conflitante

### 2. automacao_manifesto

**Escopo:** Automação da geração do ManifestoMCP.md a partir de templates.

**Sobreposição identificada:** Nenhuma
- Foco específico em geração de manifesto
- Não aborda gestão de issues

**Conclusão:** Não há conflito

### 3. reestruturacao_modularizacao_lab

**Escopo:** Reestruturação, agrupamento e modularização de subprojetos e artefatos.

**Sobreposição identificada:** Nenhuma
- Foco em governança e estruturação do laboratório
- Não aborda orquestração de issues

**Conclusão:** Não há conflito

### 4. ativacao_remota_ghc_web

**Escopo:** Ativação remota do GitHub Copilot via web.

**Sobreposição identificada:** Nenhuma
- Foco em interface web para ativação de agente
- Não aborda orquestração de issues

**Conclusão:** Não há conflito

### 5. framework_diretrizes_ia

**Escopo:** Framework de diretrizes para agentes de IA.

**Sobreposição identificada:** Nenhuma direta
- Define diretrizes e protocolos para agentes
- Não implementa orquestração de issues
- Pode servir como base normativa para o novo subprojeto

**Conclusão:** Complementar, não conflitante

## Análise de Artefatos Relacionados

### ATA_ORQUESTRACAO_IA_ARCABOUCO.md

Este documento em `automacao_tarefas_lab/` discute orquestração entre agentes IA baseada em artefatos do arcabouço, mas não especifica orquestração de issues via API do GitHub.

**Relevância:** Fornece fundamento conceitual, mas não aborda a gestão técnica de issues via API.

## Conclusão da Avaliação

**Parecer:** NÃO há subprojeto existente que abranja ou conflite diretamente com a proposta de "Orquestração de Issues via API e Agentes".

**Justificativa para criação do novo subprojeto:**

1. **Escopo distinto:** Foco específico em ciclo de vida de issues do GitHub (abertura, fechamento, atualização, automação baseada em comentários/menções)

2. **Complementaridade:** Integra-se com subprojetos existentes sem duplicar funcionalidades:
   - Pode utilizar diretrizes do `framework_diretrizes_ia`
   - Pode ser acionado por `automacao_tarefas_lab`
   - Alinha-se à governança de `reestruturacao_modularizacao_lab`

3. **Lacuna identificada:** Não existe solução atual para:
   - Orquestração de issues via API do GitHub
   - Uso de agentes (Copilot, bots) para atuar via menções/comentários
   - Rastreabilidade e governança específica do ciclo de vida de issues

4. **Impacto positivo:** Promove:
   - Rastreabilidade de demandas
   - Automação de fluxos de trabalho
   - Governança e auditoria de decisões
   - Eficiência no gerenciamento de issues

## Recomendação

✅ **APROVAR** a criação do subprojeto "Orquestração de Issues via API e Agentes" como iniciativa independente, com integração planejada aos subprojetos relacionados.

## Próximos Passos

1. Criar estrutura formal do subprojeto
2. Definir escopo detalhado e fronteiras com subprojetos existentes
3. Estabelecer interfaces de integração
4. Registrar no painel central de subprojetos

---

> Este documento serve como base para decisão de criação do subprojeto e deve ser referenciado na ATA de abertura.
