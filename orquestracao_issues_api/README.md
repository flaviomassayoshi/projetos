# Orquestração de Issues via API e Agentes

## Sumário Executivo

Este subprojeto estabelece um framework para orquestração completa do ciclo de vida de issues no GitHub através da API oficial e agentes inteligentes (GitHub Copilot, bots, rotinas IA). O objetivo é permitir abertura, fechamento, atualização e automação de issues baseada em comentários e menções, garantindo rastreabilidade, governança e eficiência no gerenciamento de demandas do ScarecrowLab.

## Proposta Vigente

### Objetivos Principais

1. **Orquestração via API:** Implementar fluxos automatizados para manipulação de issues usando a API do GitHub
2. **Agentes Inteligentes:** Permitir que agentes (Copilot, bots) atuem em issues via menções e comentários
3. **Rastreabilidade:** Garantir registro completo de ações, decisões e mudanças de estado
4. **Governança:** Estabelecer políticas, validações e controles de acesso
5. **Integração:** Conectar com painéis centrais, checklists e outros artefatos do laboratório

### Escopo

**Incluído:**
- Automação de abertura/fechamento/atualização de issues via API
- Interpretação de comandos em comentários (ex: `/fechar`, `/atribuir @usuario`)
- Notificações e triggers baseados em eventos de issues
- Validação de permissões e políticas de acesso
- Logs e auditoria de operações
- Integração com painel central de subprojetos

**Não incluído (fora de escopo):**
- Automação de tarefas internas do laboratório não relacionadas a issues (coberto por `automacao_tarefas_lab`)
- Geração de manifestos (coberto por `automacao_manifesto`)
- Diretrizes gerais para agentes (coberto por `framework_diretrizes_ia`)

### Justificativa

Conforme [avaliação de projetos existentes](docs/AVALIACAO_PROJETOS_EXISTENTES.md), não há subprojeto vigente que abranja orquestração específica de issues via API. Este subprojeto preenche lacuna crítica para:
- Gerenciamento escalável de demandas
- Automação de fluxos de trabalho
- Rastreabilidade de decisões e ações
- Governança de processos

## Histórico de Debates e Atas

- [ATA_ABERTURA](debates/ATA_ABERTURA.md) — Criação do subprojeto e definição de escopo inicial

## Checklists

- [Checklist Principal](CHECKLIST.md) — Roadmap e tarefas do subprojeto

## Documentação Técnica

- [Avaliação de Projetos Existentes](docs/AVALIACAO_PROJETOS_EXISTENTES.md) — Análise de sobreposição com subprojetos vigentes

## Estrutura do Subprojeto

```
orquestracao_issues_api/
├── README.md                              # Este arquivo
├── CHECKLIST.md                           # Checklist principal
├── CHANGELOG.md                           # Histórico de alterações
├── debates/                               # Atas e discussões
│   └── ATA_ABERTURA.md
├── checklists/                            # Checklists específicos
└── docs/                                  # Documentação técnica
    └── AVALIACAO_PROJETOS_EXISTENTES.md
```

## Referências ao Arcabouço

### Diretrizes

- [Diretrizes para Subprojetos](../.github/copilot-diretrizes/diretrizes_subprojetos.md)
- [Glossário](../.github/copilot-diretrizes/glossario.md)
- [Fluxos Gerais para Agentes](../.github/copilot-diretrizes/fluxos_gerais_agentes.md)
- [Protocolo de Orquestração via Chat](../.github/copilot-diretrizes/protocolo_orquestracao_chat.md)

### Templates Utilizados

- [Template de Subprojeto](../.github/TEMPLATE_SUBPROJETO.md)
- [Template de Checklist](../.github/TEMPLATE_CHECKLIST.md)
- [Template de Ata](../.github/copilot-diretrizes/TEMPLATE_ATA.md)

### Rastreabilidade

- [Painel Central de Subprojetos](../.github/painel_subprojetos.md): Fonte única de status e pendências

## Integração com Outros Subprojetos

- **automacao_tarefas_lab:** Pode acionar orquestração de issues para atualizar painéis e status
- **framework_diretrizes_ia:** Fornece diretrizes normativas para agentes que atuam em issues
- **reestruturacao_modularizacao_lab:** Garante alinhamento com governança e estruturação do laboratório

---

> Siga as diretrizes do repositório e utilize o painel central de subprojetos para rastreabilidade total.
