# ATA DE ABERTURA — Governança Template Issue Lab

> Consulte também:
> - [Glossário](../../.github/copilot-diretrizes/glossario.md)
> - [Diretrizes de Debate](../../.github/copilot-diretrizes/diretrizes_debate.md)
> - [Template de Ata](../../.github/copilot-diretrizes/TEMPLATE_ATA.md)

**Data/hora:** 2025-10-11 07:30 UTC

**Participantes:**
- GitHub Copilot (agente executor)
- Issue Original: [Governança] Proposta e Validação de Template Oficial de Issue Operacional do Lab

**Tema:** Criação e validação do template oficial `.github/ISSUE_TEMPLATE/issue-lab.md`

## Contexto

No processo de aprimoramento dos fluxos operacionais do ScarecrowLab, foi identificada a necessidade de um template oficial para registro de tarefas, problemas, propostas e execuções híbridas (automação + humanos) no GitHub. O template deve ser autosuficiente, aderente à governança do Lab e servir de base para automações futuras.

## Pontos Debatidos

### 1. Análise de Templates Existentes

- **Argumento A:** Template `orchestrated-issue.md` já existe mas é específico para orquestração de IA
- **Argumento B:** Necessidade de template mais genérico para demandas operacionais diversas
- **Considerações:** O novo template deve complementar (não substituir) os existentes

### 2. Estrutura e Seções Essenciais

- **Argumento A:** Template deve incluir seções para rastreabilidade (artefatos, subprojetos, links)
- **Argumento B:** Deve suportar tanto demandas simples quanto complexas com debates
- **Considerações:** Flexibilidade através de seções opcionais marcadas como "se aplicável"

### 3. Integração com Arcabouço

- **Argumento A:** Template deve referenciar diretrizes, glossário e painel central
- **Argumento B:** Deve seguir padrão de metadados YAML do GitHub
- **Considerações:** Aderência total aos templates e fluxos do arcabouço

### 4. Pipeline de Debate Automatizado

- **Argumento A:** Template deve prever seção para registro de rodadas de debate
- **Argumento B:** Deve listar personas participantes e vincular atas geradas
- **Considerações:** Alinhamento com diretrizes de debate e governança por personas

## Decisões

### 1. Criação do Template Inicial

- **Decisão:** Template `.github/ISSUE_TEMPLATE/issue-lab.md` criado com base em requisitos
- **Justificativa:** Consolida boas práticas de templates existentes e atende requisitos da issue
- **Responsável:** GitHub Copilot
- **Status:** ✅ Concluído

### 2. Estrutura do Subprojeto

- **Decisão:** Criar subprojeto `governanca_template_issue_lab/` para centralizar debates e artefatos
- **Justificativa:** Garante rastreabilidade e organização conforme diretrizes
- **Responsável:** GitHub Copilot
- **Status:** ✅ Concluído

### 3. Processo de Validação por Debates

- **Decisão:** Implementar até 3 rodadas de debate simulado entre personas especializadas
- **Justificativa:** Atende requisito da issue e garante validação colaborativa
- **Responsável:** GitHub Copilot
- **Status:** 🔄 Em andamento (Rodada 1 a ser executada)

## Ações Planejadas

- [x] Criar template inicial issue-lab.md
- [x] Criar estrutura do subprojeto
- [x] Registrar ata de abertura
- [ ] Executar rodada 1 de debate entre personas
- [ ] Registrar ata de rodada 1
- [ ] Consolidar ajustes se necessário
- [ ] Executar rodadas adicionais conforme necessidade (até 3 total)
- [ ] Registrar decisão final e versão aprovada
- [ ] Atualizar painel central de subprojetos

## Observações

### Aprendizados

- Template deve ser autosuficiente mas flexível
- Integração com arcabouço é essencial para governança
- Debates simulados agregam múltiplas perspectivas

### Recomendações

- Manter seções opcionais para demandas simples
- Garantir compatibilidade com automações futuras
- Referenciar sempre artefatos relacionados

### Alertas

- Template não deve substituir templates específicos existentes
- Validação deve seguir ciclo completo de debates (até 3 rodadas)
- Todos os artefatos devem ser anexados à issue original

## Links Relacionados

- Issue Original: [Governança] Proposta e Validação de Template Oficial de Issue Operacional do Lab
- [Template Proposto](../../.github/ISSUE_TEMPLATE/issue-lab.md)
- [Checklist Principal](../CHECKLIST.md)
- [README do Subprojeto](../README.md)
- [Documento de Personas/Roles](../../.github/mapa_papeis_responsabilidades_ia/debates/GOVERNANCA_PERSONAS_ROLES.md)

---

> Esta ata documenta o início formal do processo de governança para validação do template oficial de issues operacionais do Lab.
