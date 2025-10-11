# Checklist Principal — Auditoria Automatizada de Artefatos Órfãos

**Objetivo:** Implementar e documentar sistema completo de auditoria automatizada de artefatos órfãos (branches, PRs, issues) no ScarecrowLab, garantindo rastreabilidade, governança e eficiência.

## Instruções de Execução

- Este checklist deve ser atualizado conforme progresso do subprojeto
- Marque itens concluídos com `[x]` e atualize o CHANGELOG.md correspondente
- Registre decisões importantes em atas na pasta `debates/`
- Mantenha links atualizados com documentação técnica e artefatos gerados
- Atualize o painel central de subprojetos a cada marco relevante

---

## Fase 1: Planejamento e Estruturação

- [x] Criar estrutura de diretórios do subprojeto
- [x] Criar README.md do subprojeto
- [x] Criar CHECKLIST.md (este arquivo)
- [x] Criar CHANGELOG.md
- [x] Criar ATA_ABERTURA.md
- [ ] Atualizar painel central de subprojetos
- [ ] Validar rastreabilidade e links cruzados

## Fase 2: Desenvolvimento do Script de Auditoria

- [x] Implementar autenticação com GitHub API
  - [x] Suporte a GITHUB_TOKEN via variável de ambiente
  - [x] Tratamento de erros de autenticação
  - [x] Validação de rate limits
- [x] Implementar auditoria de branches
  - [x] Listar todas as branches do repositório
  - [x] Identificar branches não mescladas na master
  - [x] Verificar ausência de PRs associados
  - [x] Coletar metadados (último commit, autor, data)
- [x] Implementar auditoria de pull requests
  - [x] Listar PRs abertos sem merge
  - [x] Listar PRs fechados sem merge
  - [x] Identificar PRs inativos (sem atividade por X dias)
  - [x] Coletar metadados (autor, reviewers, labels, idade)
- [x] Implementar auditoria de issues
  - [x] Listar issues abertas
  - [x] Verificar vínculo com PRs ou merges
  - [x] Identificar issues sem movimentação recente
  - [x] Coletar metadados (labels, assignees, idade)
- [x] Implementar geração de relatório
  - [x] Formato markdown estruturado
  - [x] Sumário executivo com estatísticas
  - [x] Seções separadas por tipo de artefato
  - [x] Timestamp e metadados da auditoria

## Fase 3: Criação de Workflow GitHub Actions

- [x] Criar workflow de auditoria periódica
  - [x] Configurar trigger de schedule (semanal)
  - [x] Configurar trigger manual (workflow_dispatch)
  - [x] Definir job de auditoria
  - [x] Configurar permissões necessárias
- [x] Implementar execução do script
  - [x] Checkout do código
  - [x] Setup de Python 3.x
  - [x] Instalação de dependências
  - [x] Execução do script de auditoria
- [x] Implementar armazenamento de relatórios
  - [x] Upload de relatório como artifact
  - [x] Commit de relatório no repositório (opcional)
  - [x] Notificação em caso de falha

## Fase 4: Documentação e Integração

- [x] Criar manual de uso
  - [x] Instruções de execução local
  - [x] Configuração de variáveis de ambiente
  - [x] Interpretação de relatórios
  - [x] Troubleshooting
- [x] Criar checklist de revisão manual
  - [x] Template para análise de artefatos órfãos
  - [x] Critérios de decisão (manter/remover/arquivar)
  - [x] Processo de documentação de decisões
- [x] Documentar integração com governança
  - [x] Atualização do painel central
  - [x] Registro em changelogs
  - [x] Vínculo com outros subprojetos

## Fase 5: Testes e Validação

- [x] Testar script localmente
  - [x] Validar estrutura e sintaxe Python
  - [x] Verificar help e argumentos
  - [x] Validar imports e dependências (stdlib only)
- [x] Testar workflow em branch de desenvolvimento
  - [x] Validar sintaxe YAML
  - [x] Verificar triggers configurados
  - [x] Confirmar permissões adequadas
- [ ] Revisar relatórios gerados (requer execução real)
  - [ ] Verificar completude dos dados
  - [ ] Validar formato e estrutura
  - [ ] Confirmar rastreabilidade

## Fase 6: Implantação e Monitoramento

- [ ] Merge do código para master
- [ ] Configurar execução periódica
- [ ] Monitorar primeira execução automática
- [ ] Validar integração com painel central
- [ ] Documentar primeiro ciclo de auditoria

## Fase 7: Evolução Contínua

- [ ] Coletar feedback de uso
- [ ] Avaliar expansão de escopo (arquivos órfãos, workflows inativos)
- [ ] Implementar melhorias identificadas
- [ ] Manter documentação atualizada

## Links Relacionados

- [README do Subprojeto](README.md)
- [Changelog](CHANGELOG.md)
- [Ata de Abertura](debates/ATA_ABERTURA.md)
- [Manual de Uso](docs/MANUAL_USO.md)
- [Painel Central de Subprojetos](../.github/painel_subprojetos.md)

---

> Mantenha este checklist sincronizado com o progresso real do subprojeto. Use o report_progress para commits frequentes.
