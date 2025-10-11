# Checklist Principal — Scarecrow AutoFlow

> Checklist persistente vinculado ao roadmap de implementação do sistema de aprovação automatizada.

## Fase 1: Estruturação e Planejamento (Concluída)

- [x] Criar estrutura de diretórios do subprojeto
- [x] Criar README.md com sumário executivo e proposta vigente
- [x] Criar CHECKLIST.md seguindo template padrão
- [x] Criar CHANGELOG.md inicial
- [x] Criar ATA_ABERTURA.md documentando decisões iniciais

## Fase 2: Documentação de Critérios e Regras

- [ ] Documentar critérios de classificação detalhados (docs/CRITERIOS_CLASSIFICACAO.md)
- [ ] Documentar regras de validação de conformidade (docs/REGRAS_VALIDACAO.md)
- [ ] Documentar processo de simulação de decisões (docs/PROCESSO_SIMULACAO.md)
- [ ] Criar guia de uso para contribuidores (docs/GUIA_USO.md)
- [ ] Documentar estrutura de logs de decisões (decisoes_automatizadas/README.md)

## Fase 3: Implementação do Classificador

- [ ] Criar script de classificação (scripts/classificador.py)
- [ ] Implementar análise de metadados de issues/PRs
- [ ] Implementar análise semântica de conteúdo
- [ ] Implementar lógica de categorização (auto-merge/needs-simulation/manual-review)
- [ ] Criar testes unitários do classificador
- [ ] Documentar API do classificador

## Fase 4: Implementação do Validador

- [ ] Criar script de validação (scripts/validador.py)
- [ ] Implementar verificação de conformidade com manifesto
- [ ] Implementar verificação de conformidade com templates
- [ ] Implementar checklist semântico por tipo de fluxo
- [ ] Criar testes unitários do validador
- [ ] Documentar API do validador

## Fase 5: Implementação do Simulador

- [ ] Criar script de simulação (scripts/simulador.py)
- [ ] Implementar personas (Engenheiro de Prompt, Guardião do Manifesto, DevOps Modular)
- [ ] Implementar lógica de debate multi-perspectiva
- [ ] Implementar geração automática de atas de simulação
- [ ] Criar templates de resposta por persona
- [ ] Criar testes do simulador
- [ ] Documentar API do simulador

## Fase 6: GitHub Actions e Automação

- [ ] Criar workflow para classificação automática de issues (.github/workflows/autoflow-classify-issue.yml)
- [ ] Criar workflow para classificação automática de PRs (.github/workflows/autoflow-classify-pr.yml)
- [ ] Criar workflow para validação e aprovação (.github/workflows/autoflow-validate.yml)
- [ ] Configurar labels automáticos (autoflow:auto-merge, autoflow:needs-simulation, autoflow:manual-review)
- [ ] Implementar triggers de eventos (issue_opened, pull_request_opened, etc.)
- [ ] Testar workflows em ambiente de desenvolvimento

## Fase 7: Sistema de Logs e Rastreabilidade

- [ ] Criar estrutura de diretório decisoes_automatizadas/ com versionamento
- [ ] Implementar logging automático de todas as decisões
- [ ] Criar templates para logs de decisão (decisoes_automatizadas/template_log.md)
- [ ] Implementar indexação de logs por data/tipo/resultado
- [ ] Garantir rastreabilidade bidirecional (issue/PR <-> log)
- [ ] Implementar arquivamento periódico de logs antigos

## Fase 8: Integração e Governança

- [ ] Atualizar painel central de subprojetos (.github/painel_subprojetos.md)
- [ ] Criar entrada no README principal do repositório
- [ ] Integrar com automacao_tarefas_lab
- [ ] Integrar com orquestracao_issues_api
- [ ] Documentar integrações com outros subprojetos
- [ ] Criar documentação de evolução contínua

## Fase 9: Testes e Validação (Opcional)

- [ ] Testar classificador com issues/PRs históricos
- [ ] Testar validador com casos de conformidade conhecidos
- [ ] Testar simulador com cenários de decisão complexos
- [ ] Coletar métricas de eficácia (taxa de automação, tempo médio, conformidade)
- [ ] Ajustar critérios baseado nos resultados
- [ ] Documentar resultados dos testes

## Fase 10: Painel de Governança (Opcional)

- [ ] Definir métricas a serem rastreadas
- [ ] Implementar coleta automática de métricas
- [ ] Criar dashboard de visualização (GitHub Pages ou similar)
- [ ] Configurar atualização automática do painel
- [ ] Documentar interpretação das métricas

---

**Status Atual:** Fase 1 concluída, iniciando Fase 2

**Próximos Passos:** 
1. Criar documentação técnica detalhada (critérios, regras, processos)
2. Implementar scripts core (classificador, validador, simulador)
3. Configurar GitHub Actions workflows

**Responsável:** GitHub Copilot

**Última Atualização:** 2025-10-11

---

> Este checklist é persistente e deve ser atualizado conforme o progresso do subprojeto. Registre mudanças significativas no CHANGELOG.md.
