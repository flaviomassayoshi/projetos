# Copilot Instructions

## 1. Objetivo e Organização Geral

- Este documento é exclusivo para agentes de IA. Não é necessário considerar clareza para humanos.

## 2. Novos Subprojetos e Tratamento de Propostas

- Toda nova proposta, solução ou iniciativa deve ser registrada diretamente como um novo subprojeto, criando uma pasta dedicada no local apropriado (ex: `python_apps/`, `extensoes/`, etc.).
- Recomenda-se utilizar o arquivo `TEMPLATE_SUBPROJETO.md` como base para a estrutura inicial do subprojeto.
- O subprojeto pode começar apenas com README, checklists e documentação mínima, evoluindo conforme a necessidade.
- Debates, atas, roteiros e histórico devem ser centralizados na estrutura do subprojeto desde o início, garantindo rastreabilidade completa.



# Diretrizes para Agentes de IA (versão enxuta)

- Debates entre modelos de IA só devem ser iniciados quando solicitados explicitamente pelo responsável do subprojeto ou, caso o agente identifique relevância, mediante sugestão e aprovação do responsável.
- O subprojeto pode evoluir sem debates até que haja necessidade real de discussão colaborativa entre modelos.
- Todo o histórico de debates, decisões e evolução deve ficar centralizado na pasta do subprojeto, mantendo rastreabilidade e organização.

- Sempre que for solicitada revisão de diretrizes, considerar tanto este arquivo principal quanto todos os anexos de diretrizes.

> Estas diretrizes são destinadas exclusivamente à correta interpretação e execução por agentes de IA. Não é necessário considerar clareza para humanos.

## Estrutura e Controle

- Cada subprojeto deve ter ambiente virtual, dependências e automações isoladas.
- `.github/PENDENCIAS.md`: deve apenas referenciar (com links ou caminhos) os checklists de subprojetos que ainda estão em andamento. Os detalhes das pendências e tarefas devem estar centralizados nos próprios checklists de cada subprojeto.
- Ao concluir um tema/checklist:
	- Remova a referência correspondente de `.github/PENDENCIAS.md`.
	- Registre o fechamento em `.github/changelog/<tema>.md` (ou changelog principal, se for pendência geral).
	- O changelog deve conter: data/hora, responsável, descrição clara, status final (concluído/cancelado), e link para o checklist/ata final.
	- Para subprojetos, o checklist deve ser arquivado (não apagado) e marcado como concluído, mantendo rastreabilidade.
	- Para pendências gerais do projeto, se detalhadas em arquivos anexos, também registrar encerramento no changelog principal.
	- Ao encerrar pendências, revise `.github/PENDENCIAS.md` e outros arquivos para garantir que não há referências órfãs.

	- Template mínimo para changelog:
		- Data/hora:
		- Responsável:
		- Descrição:
		- Status final:
		- Link para checklist/ata:

	- Não dependa do log do Git para histórico de pendências.
- Sempre use checklist para roteiros e procedimentos, mantendo o detalhamento nos subprojetos.

 - Checklists, roteiros e documentação de tarefas específicas de subprojetos devem ser criados e mantidos exclusivamente na pasta do respectivo subprojeto.
 - `.github/PENDENCIAS.md` deve referenciar apenas o caminho para esses arquivos dentro dos subprojetos.
 - Não criar ou manter checklists de subprojetos em `.github/`, exceto para pendências gerais do repositório.
 - Pendências do projeto (não ligadas a subprojetos) podem ser detalhadas em arquivos anexos em `.github/`, e `.github/PENDENCIAS.md` pode referenciá-los normalmente.

 - Sempre que uma revisão, migração ou renomeação de arquivos/pastas for solicitada pelo usuário e resultar em substituição, os arquivos e pastas antigos que deixarem de ser utilizados devem ser removidos do workspace, salvo orientação explícita em contrário. Não manter cópias desnecessárias de arquivos/pastas obsoletos.
	 - Exceção: se houver histórico relevante, registre no changelog antes da remoção.
	 - Esta diretriz se aplica a qualquer operação de mover, migrar, renomear ou reorganizar estrutura de subprojetos, pastas e/ou arquivos.

# Copilot Instructions

**Objetivo:** Este documento serve como sumário executivo e índice central das diretrizes para agentes de IA. Todo o detalhamento, exemplos, templates e fluxos estão modularizados nos anexos abaixo.

## Índice de Diretrizes Detalhadas

- [Template de Checklist](./TEMPLATE_CHECKLIST.md) — Modelo padrão para criação de novos checklists por agentes de IA.
- [Template de Changelog](./copilot-diretrizes/template_changelog.md) — Estrutura mínima para registro de encerramento de temas/checklists.
- [Glossário de Termos](./copilot-diretrizes/glossario.md) — Definições e siglas relevantes para agentes de IA.
- [Diretrizes Técnicas do Ambiente Local](./copilot-diretrizes/diretrizes_tecnicas.md) — Requisitos de hardware, ambiente Python, troubleshooting de GPU, etc.
- [Convenções de Código e Documentação](./copilot-diretrizes/convenções_codigo.md) — Padrões de nomenclatura, docstrings e organização de código.
- [Diretrizes para Projetos Clonados de Terceiros](./copilot-diretrizes/projetos_terceiros.md) — Customizações, versionamento e separação de repositórios.
- [Execução de Scripts e Ativação de venv no Windows](./copilot-diretrizes/diretrizes_execucao_venv_windows.md) — Procedimentos para ativação de venv e execução de scripts Python no Windows.
- [Checklists Práticos e Templates](./copilot-diretrizes/checklists_praticos.md) — Exemplos práticos e templates de checklist para agentes de IA.
- [Fluxos de Encerramento, Changelog e Prompt de Retomada](./copilot-diretrizes/fluxos_encerramento.md) — Fluxos de encerramento, exemplos de changelog e modelo de prompt de retomada.
- [Instruções de Setup, CI e Automação](./copilot-diretrizes/instrucoes_setup_CI.md) — Setup de ambiente, integração contínua e automações recorrentes.
- [Rodadas de Debate e Encerramento](./copilot-diretrizes/diretrizes_debate.md) — Fluxo de debates, atas e tabelas de decisão entre modelos de IA.
## Observação Geral sobre Referência de Arquivos
