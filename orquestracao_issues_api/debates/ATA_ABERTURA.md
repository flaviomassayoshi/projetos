# ATA — Abertura do Subprojeto "Orquestração de Issues via API e Agentes"

**Data/hora:** 2025-10-11 01:38

**Participantes:**
- GitHub Copilot (agente executor)
- @flaviomassayoshi (solicitante/orquestrador)

**Tema:** Registro e criação formal do subprojeto de orquestração do ciclo de vida de issues via API do GitHub e agentes inteligentes

## Contexto

Solicitação originada pela issue "[IA-Orquestração] Registro e avaliação de novo subprojeto: Orquestração de Issues via API e Agentes", que demanda:

1. Avaliação prévia de projetos/subprojetos existentes para evitar duplicidade ou sobreposição
2. Criação formal do subprojeto caso não haja conflito
3. Documentação completa com fluxos de orquestração e governança
4. Integração com painel central e artefatos persistentes

### Motivação

O laboratório ScarecrowLab precisa de um sistema robusto para:
- Automatizar abertura, fechamento e atualização de issues
- Permitir que agentes (Copilot, bots) atuem via menções e comentários
- Garantir rastreabilidade completa do ciclo de vida de issues
- Estabelecer governança e controles de acesso
- Aumentar eficiência no gerenciamento de demandas

### Documentação Base

- Issue original: "[IA-Orquestração] Registro e avaliação de novo subprojeto: Orquestração de Issues via API e Agentes"
- Diretrizes: [diretrizes_subprojetos.md](../../.github/copilot-diretrizes/diretrizes_subprojetos.md)
- Templates: [TEMPLATE_SUBPROJETO.md](../../.github/TEMPLATE_SUBPROJETO.md), [TEMPLATE_ATA.md](../../.github/copilot-diretrizes/TEMPLATE_ATA.md)

## Pontos Debatidos

### 1. Necessidade de Avaliação de Projetos Existentes

**Argumento A:** É mandatório avaliar subprojetos vigentes para evitar duplicidade e garantir complementaridade.

**Argumento B:** A análise deve ser documentada formalmente para rastreabilidade.

**Considerações:** 
- Realizada análise detalhada de 5 subprojetos principais
- Identificado `automacao_tarefas_lab` como mais próximo, porém complementar
- Nenhum conflito ou sobreposição crítica encontrada
- Documento [AVALIACAO_PROJETOS_EXISTENTES.md](../docs/AVALIACAO_PROJETOS_EXISTENTES.md) criado como evidência

### 2. Escopo do Novo Subprojeto

**Argumento A:** Deve focar exclusivamente em orquestração de issues via API para evitar dispersão.

**Argumento B:** Precisa definir claramente o que está incluído e excluído do escopo.

**Considerações:**
- Incluído: Automação de issues, comandos via comentários, rastreabilidade, governança
- Excluído: Automações internas do lab (já cobertas), geração de manifestos, diretrizes gerais
- Fronteiras bem definidas no README.md

### 3. Estrutura e Organização

**Argumento A:** Deve seguir rigorosamente os templates oficiais do arcabouço.

**Argumento B:** Estrutura de pastas deve facilitar evolução e adição de documentação técnica.

**Considerações:**
- Estrutura criada: `debates/`, `checklists/`, `docs/`
- Artefatos base: README.md, CHECKLIST.md, CHANGELOG.md, ATA_ABERTURA.md
- Todos os documentos seguem templates oficiais
- Links cruzados para garantir rastreabilidade

### 4. Integração com Subprojetos Existentes

**Argumento A:** Deve complementar, não duplicar funcionalidades existentes.

**Argumento B:** Interfaces de integração devem ser especificadas desde o início.

**Considerações:**
- Integração planejada com `automacao_tarefas_lab` (pode acionar orquestração)
- Uso de diretrizes do `framework_diretrizes_ia`
- Alinhamento com governança de `reestruturacao_modularizacao_lab`
- Documentado na seção de integrações do README.md

## Decisões

### 1. Aprovação da Criação do Subprojeto

**Justificativa:** Avaliação comprova ausência de conflito e identifica lacuna crítica no laboratório.

**Responsável:** GitHub Copilot (execução), @flaviomassayoshi (aprovação)

**Status:** ✅ Aprovado

### 2. Estrutura de 7 Fases de Implementação

**Justificativa:** Checklist organizado em fases sequenciais facilita planejamento e execução progressiva.

**Fases definidas:**
1. Planejamento e Estruturação
2. Definição de Requisitos
3. Prototipagem e Desenvolvimento
4. Integração e Testes
5. Documentação e Governança
6. Implantação e Monitoramento
7. Evolução Contínua

**Responsável:** GitHub Copilot

**Status:** ✅ Implementado

### 3. Comandos Iniciais para Agentes

**Justificativa:** Definir sintaxe padrão desde o início evita retrabalho e garante consistência.

**Comandos especificados:**
- `/fechar` - Fechar issue
- `/atribuir @usuario` - Atribuir responsável
- `/prioridade [alta|média|baixa]` - Definir prioridade
- `/vincular #numero` - Vincular a outra issue
- `/label nome` - Gerenciar labels

**Responsável:** GitHub Copilot

**Status:** ✅ Documentado no CHECKLIST.md

### 4. Rastreabilidade via Painel Central

**Justificativa:** Painel central é fonte única de verdade para status de subprojetos.

**Ação:** Atualizar `.github/painel_subprojetos.md` com entrada do novo subprojeto.

**Responsável:** GitHub Copilot

**Prazo:** Imediato (próximo commit)

**Status:** ⏳ Pendente

## Ações Planejadas

- [x] Criar estrutura de diretórios
- [x] Criar README.md baseado em template
- [x] Criar CHECKLIST.md com 7 fases
- [x] Criar CHANGELOG.md com entrada inicial
- [x] Criar ATA_ABERTURA.md (este documento)
- [x] Documentar avaliação de projetos existentes
- [ ] Atualizar painel central de subprojetos
- [ ] Validar rastreabilidade e links cruzados
- [ ] Comunicar conclusão na issue original

## Observações

### Alinhamento ao Arcabouço

Todos os artefatos criados seguem rigorosamente:
- [TEMPLATE_SUBPROJETO.md](../../.github/TEMPLATE_SUBPROJETO.md)
- [TEMPLATE_CHECKLIST.md](../../.github/TEMPLATE_CHECKLIST.md)
- [TEMPLATE_ATA.md](../../.github/copilot-diretrizes/TEMPLATE_ATA.md)
- [Diretrizes para Subprojetos](../../.github/copilot-diretrizes/diretrizes_subprojetos.md)

### Rastreabilidade Garantida

- Links bidirecionais entre todos os documentos
- Referência ao painel central de subprojetos
- Changelog com histórico desde criação
- ATA documenta decisões e justificativas

### Qualidade e Completude

- Avaliação formal de projetos existentes
- Escopo bem delimitado com inclusões/exclusões
- Integração planejada com subprojetos relacionados
- Checklist detalhado em 7 fases sequenciais
- Documentação técnica desde abertura

### Próximos Marcos

1. Atualização do painel central (imediato)
2. Início da Fase 2 (Definição de Requisitos)
3. Mapeamento de casos de uso prioritários
4. Especificação técnica de integrações com API

## Links Relacionados

- [README do Subprojeto](../README.md)
- [CHECKLIST Principal](../CHECKLIST.md)
- [CHANGELOG](../CHANGELOG.md)
- [Avaliação de Projetos Existentes](../docs/AVALIACAO_PROJETOS_EXISTENTES.md)
- [Painel Central de Subprojetos](../../.github/painel_subprojetos.md)
- [Diretrizes para Subprojetos](../../.github/copilot-diretrizes/diretrizes_subprojetos.md)

---

> Esta ata registra formalmente a criação do subprojeto e serve como referência para decisões futuras.
