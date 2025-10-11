# Changelog — Scarecrow AutoFlow

> Registro cronológico de alterações, decisões e marcos do subprojeto.

---

## 2025-10-11 — Criação do Subprojeto

**Responsável:** GitHub Copilot

**Contexto:** Criação do subprojeto Scarecrow AutoFlow em resposta à necessidade crítica de reduzir gargalo de aprovação manual de issues e pull requests no ScarecrowLab.

**Ações Realizadas:**
- Estrutura completa de diretórios criada (debates/, checklists/, docs/, scripts/, decisoes_automatizadas/)
- README.md elaborado com sumário executivo, proposta vigente, escopo, justificativa e fluxo operacional
- CHECKLIST.md estruturado em 10 fases (estruturação até painel de governança)
- CHANGELOG.md inicializado
- ATA_ABERTURA.md registrando decisões iniciais e alinhamento com arcabouço

**Decisões:**
1. Categorias de classificação definidas: auto-merge, needs-simulation, manual-review
2. Personas simuladas definidas: Engenheiro de Prompt, Guardião do Manifesto, DevOps Modular
3. Escopo delimitado para evitar sobreposição com automacao_tarefas_lab e orquestracao_issues_api
4. Sistema de logs versionados em decisoes_automatizadas/ para rastreabilidade total
5. Abordagem modular com scripts separados (classificador, validador, simulador)

**Rastreabilidade:**
- Issue de origem: (número da issue que originou este subprojeto)
- Painel central de subprojetos: atualizado com nova entrada
- Artefatos criados:
  - scarecrow_autoflow/README.md
  - scarecrow_autoflow/CHECKLIST.md
  - scarecrow_autoflow/CHANGELOG.md
  - scarecrow_autoflow/debates/ATA_ABERTURA.md

**Próximos Passos:**
1. Criar documentação técnica detalhada (Fase 2)
2. Implementar scripts core (Fase 3-5)
3. Configurar GitHub Actions (Fase 6)

---

> Atualize este changelog sempre que houver decisões relevantes, conclusão de fases ou mudanças de escopo.
