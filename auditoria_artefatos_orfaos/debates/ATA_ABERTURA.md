# ATA DE ABERTURA — Auditoria Automatizada de Artefatos Órfãos

> Consulte também:
> - [Glossário](../../.github/copilot-diretrizes/glossario.md) para definições essenciais.
> - [Diretrizes de Debate](../../.github/copilot-diretrizes/diretrizes_debate.md) para estrutura de debates.
> - [Protocolo de Orquestração](../../.github/copilot-diretrizes/protocolo_orquestracao_chat.md) para comunicação entre agentes.

**Data/hora:** 2025-10-11 04:30 UTC

**Participantes:**
- GitHub Copilot (agente executor/implementador)
- @flaviomassayoshi (solicitante humano, via issue)

**Tema:** Criação do subprojeto de auditoria automatizada de artefatos órfãos no ScarecrowLab

## Contexto

Durante interações frequentes via chat web/mobile, sessões encerradas precocemente ou múltiplas automações, torna-se difícil garantir que todo o trabalho (branches, PRs, issues) esteja devidamente registrado, rastreável e integrado à branch principal (master) do repositório.

A issue [IA-Orquestração] Auditoria automatizada: Levantamento de artefatos órfãos solicitou implementação de sistema de auditoria recorrente ou sob demanda para mapear:
- Branches com commits não mesclados e sem PRs associados
- Pull Requests não mesclados (abertos, fechados ou inativos)
- Issues abertas sem vínculo claro com atividades
- (Futuro) Artefatos órfãos adicionais

## Pontos Debatidos

1. **Escopo inicial do subprojeto**
   - Argumento A: Começar com branches, PRs e issues como MVP
   - Argumento B: Incluir auditoria de arquivos/código órfão desde início
   - Considerações: MVP permite validação rápida e iteração. Arquivos órfãos podem ser adicionados em fase futura.

2. **Tecnologia de implementação**
   - Argumento A: Script Python + GitHub API (PyGithub)
   - Argumento B: GitHub CLI + shell script
   - Considerações: Python oferece melhor estruturação, tratamento de erros e geração de relatórios. GitHub CLI seria mais simples mas menos flexível.

3. **Frequência de execução**
   - Argumento A: Execução diária automática
   - Argumento B: Execução semanal com opção manual
   - Considerações: Semanal reduz ruído e custos de API, mantendo visibilidade adequada. Manual permite auditorias sob demanda.

4. **Formato de relatórios**
   - Argumento A: Markdown estruturado versionado no repositório
   - Argumento B: JSON para consumo por outras ferramentas
   - Considerações: Markdown facilita revisão humana e integração com governança existente. JSON pode ser adicionado futuramente se necessário.

## Decisões

1. **Aprovação da criação do subprojeto**
   - Justificativa: Preenche lacuna crítica de governança e rastreabilidade
   - Responsável: GitHub Copilot
   - Prazo: 2025-10-11

2. **Escopo MVP: branches, PRs e issues**
   - Justificativa: Permite validação rápida e iteração incremental
   - Responsável: GitHub Copilot
   - Prazo: Fase 1 até 2025-10-11

3. **Implementação via Python + GitHub Actions**
   - Justificativa: Melhor estruturação, flexibilidade e integração com CI/CD
   - Responsável: GitHub Copilot
   - Prazo: Fases 2-3 até 2025-10-11

4. **Execução semanal automática + opção manual**
   - Justificativa: Equilíbrio entre visibilidade e eficiência
   - Responsável: GitHub Copilot
   - Prazo: Fase 3 até 2025-10-11

5. **Relatórios em markdown versionados**
   - Justificativa: Facilita revisão humana e rastreabilidade
   - Responsável: GitHub Copilot
   - Prazo: Fase 2 até 2025-10-11

## Ações Planejadas

- [x] Criar estrutura do subprojeto (debates/, scripts/, docs/, relatorios/)
- [x] Criar README.md com sumário executivo e proposta vigente
- [x] Criar CHECKLIST.md com 7 fases de implementação
- [x] Criar CHANGELOG.md com entrada inicial
- [x] Criar ATA_ABERTURA.md (este arquivo)
- [ ] Implementar script Python de auditoria (audit_orphaned_artifacts.py)
- [ ] Criar workflow GitHub Actions (.github/workflows/audit-orphaned-artifacts.yml)
- [ ] Criar manual de uso (docs/MANUAL_USO.md)
- [ ] Atualizar painel central de subprojetos
- [ ] Testar e validar implementação

## Observações

- Subprojeto alinhado com diretrizes de novos subprojetos do arcabouço
- Estrutura segue padrão estabelecido (README, CHECKLIST, CHANGELOG, debates/)
- Rastreabilidade garantida via links cruzados e painel central
- Implementação iterativa permite ajustes baseados em feedback
- Pode integrar-se com orquestracao_issues_api e automacao_tarefas_lab no futuro

## Links Relacionados

- [README do Subprojeto](../README.md)
- [Checklist Principal](../CHECKLIST.md)
- [Changelog](../CHANGELOG.md)
- [Issue de Origem](../../.github/) (vincular quando disponível)
- [Painel Central de Subprojetos](../../.github/painel_subprojetos.md)
- [Diretrizes para Novos Subprojetos](../../.github/copilot-diretrizes/diretrizes_subprojetos.md)

---

> Ata criada seguindo [TEMPLATE_ATA.md](../../.github/copilot-diretrizes/TEMPLATE_ATA.md). Vinculada aos artefatos do subprojeto para rastreabilidade total.
