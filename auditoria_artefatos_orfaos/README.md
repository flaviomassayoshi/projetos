# Auditoria Automatizada de Artefatos Órfãos

## Sumário Executivo

Este subprojeto implementa um sistema de auditoria automatizada para identificar e documentar artefatos órfãos no repositório ScarecrowLab, incluindo branches não mescladas, pull requests inativos e issues sem vínculo. O objetivo é garantir rastreabilidade, governança e facilitar a retomada de contexto em ciclos longos ou sessões interrompidas.

## Proposta Vigente

### Objetivos Principais

1. **Auditoria de Branches:** Identificar branches com commits não mesclados na master sem PRs associados
2. **Rastreamento de PRs:** Mapear pull requests abertos, fechados ou inativos que não foram mesclados
3. **Mapeamento de Issues:** Listar issues abertas sem vínculo claro com PRs, merges ou milestones
4. **Automação Periódica:** Execução recorrente via GitHub Actions com possibilidade de execução manual
5. **Governança:** Registro de cada ciclo de auditoria com artefatos encontrados e decisões tomadas

### Escopo

**Incluído:**
- Script Python para auditoria via GitHub API
- Workflow GitHub Actions para execução periódica (semanal) e manual
- Geração de relatórios estruturados em markdown
- Checklist de revisão manual para decisões sobre artefatos órfãos
- Integração com painel central de subprojetos e changelog

**Não incluído (fora de escopo):**
- Remoção automática de artefatos (requer aprovação manual)
- Auditoria de arquivos/código órfão (pode ser expandido futuramente)
- Sincronização com ferramentas externas de gestão de projetos

### Justificativa

Durante interações frequentes via chat web/mobile, sessões encerradas precocemente ou múltiplas automações, é difícil garantir que todo trabalho esteja devidamente registrado e integrado. Este subprojeto preenche lacuna crítica ao fornecer visibilidade completa de artefatos pendentes, facilitando governança e retomada de contexto.

## Estrutura do Subprojeto

```
auditoria_artefatos_orfaos/
├── README.md                    # Este arquivo
├── CHECKLIST.md                 # Checklist principal de implementação
├── CHANGELOG.md                 # Histórico de alterações
├── debates/                     # Atas e discussões
│   └── ATA_ABERTURA.md
├── scripts/                     # Scripts de auditoria
│   └── audit_orphaned_artifacts.py
├── docs/                        # Documentação técnica
│   └── MANUAL_USO.md
└── relatorios/                  # Armazenamento de relatórios históricos
    └── .gitkeep
```

## Histórico de Debates e Atas

- [Ata de Abertura — 2025-10-11](debates/ATA_ABERTURA.md): Aprovação do subprojeto e criação de artefatos iniciais

## Checklists

- [Checklist Principal do Subprojeto](CHECKLIST.md): Lista completa de tarefas e entregas

## Documentação Técnica

- [Manual de Uso](docs/MANUAL_USO.md): Instruções de execução, configuração e interpretação de relatórios
- [Changelog](CHANGELOG.md): Histórico de alterações e decisões

## Integração com Outros Subprojetos

- **orquestracao_issues_api:** Pode utilizar dados da auditoria para acionar ações automatizadas em issues órfãs
- **automacao_tarefas_lab:** Pode executar auditoria como parte de rotinas de manutenção
- **reestruturacao_modularizacao_lab:** Garante alinhamento com governança e estruturação do laboratório

## Referências ao Arcabouço

### Diretrizes Aplicadas
- [Diretrizes para Novos Subprojetos](../.github/copilot-diretrizes/diretrizes_subprojetos.md)
- [Fluxos Gerais para Agentes de IA](../.github/copilot-diretrizes/fluxos_gerais_agentes.md)
- [Instruções de Setup e CI](../.github/copilot-diretrizes/instrucoes_setup_CI.md)

### Templates Utilizados
- [TEMPLATE_SUBPROJETO.md](../.github/TEMPLATE_SUBPROJETO.md)
- [TEMPLATE_ATA.md](../.github/copilot-diretrizes/TEMPLATE_ATA.md)
- [TEMPLATE_CHECKLIST.md](../.github/TEMPLATE_CHECKLIST.md)

### Rastreabilidade
- **Painel Central:** [.github/painel_subprojetos.md](../.github/painel_subprojetos.md)
- **Issue de Origem:** [IA-Orquestração] Auditoria automatizada: Levantamento de artefatos órfãos
- **Responsável:** GitHub Copilot
- **Status:** Em desenvolvimento (Fase 1 concluída)

---

> Siga as diretrizes do repositório para governança, debates e versionamento. Toda alteração deve ser registrada no CHANGELOG.md e refletida no painel central de subprojetos.
