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
- Só modifique arquivos explicitamente liberados.
- Não versionar alterações em projetos de terceiros, exceto customizações próprias em pastas separadas.


## Checklist de entrega obrigatório (executar ao final de cada resposta)

- Gerar prompt de continuidade (deve conter informações suficientes para que o trabalho seja retomado em nova sessão do Copilot, incluindo contexto, status e próximos passos relevantes).
- Atualizar `.github/PENDENCIAS.md` (status: pendente, em progresso, concluído).
- Ao concluir tema/checklist, remover pendências concluídas de `.github/PENDENCIAS.md` e registrar fechamento em `.github/changelog/<tema>.md` (data, hora, descrição clara).

- Garantir que changelog seja o histórico oficial.
- Não versionar projetos de terceiros (exceto customizações).
- Sempre analisar se todas as diretrizes relevantes (principal e anexos) estão sendo atendidas ao finalizar cada entrega.

## Observações técnicas

- Sempre consulte anexos para detalhes técnicos específicos.
- Para execução de scripts Python/venv no Windows, siga obrigatoriamente a diretriz de execution policy (`diretrizes_execucao_venv_windows.md`).
- Ao ler arquivos:
	- Prefira ler em bloco (chunk) apenas quando o objetivo for leitura ou análise de contexto.
	- Quando o objetivo for edição, leia o arquivo inteiro para garantir integridade e evitar inconsistências.
- Para rodadas de debate e encerramento, siga obrigatoriamente as diretrizes em `.github/copilot-diretrizes/diretrizes_debate.md`.

## 4. Fluxo de Trabalho para Agentes de IA

- Antes de executar qualquer tarefa, avalie o prompt para identificar se a solicitação pode gerar trabalho excessivamente oneroso para o agente ou comprometer limites de uso. Caso identifique risco, solicite confirmação do usuário ou proponha alternativas mais eficientes.
- Sempre explique claramente ao usuário o que está sendo feito antes de exibir mensagens como "Working" ou executar ações demoradas. Evite mensagens genéricas sem contexto; detalhe o objetivo ou etapa em andamento para que o usuário saiba exatamente o que está sendo processado.
- Sempre priorize a execução automática de comandos necessários para o fluxo de trabalho, evitando solicitar ao usuário que copie e cole comandos manualmente.
- Antes de executar qualquer comando, explique claramente em linguagem natural o que ele faz, para que o usuário compreenda o propósito da ação antes da execução. Só então peça permissão para rodar comandos, exceto em casos de automações rotineiras ou quando explicitamente liberado nas diretrizes.
- Inclua comandos como `git clone`, download de modelos, instalação de dependências e outras automações diretamente na execução, sem depender de ações manuais do usuário, salvo restrições técnicas ou de permissão.
- Sempre proponha e execute comandos automaticamente para setup, download, clonagem e inicialização de ambientes, conforme o contexto do subprojeto.
- Use Git para versionamento. Sempre que possível, utilize um repositório Git separado para cada subprojeto independente, ou mantenha o histórico bem organizado por subpasta.
- Ao interagir com agentes de IA, sempre especifique o contexto do subprojeto em questão para evitar mistura de informações.
- Siga as convenções e regras ao gerar código, documentação ou automações.

---


## Glossário

- **MCP**: Microsoft Copilot (Copilot integrado ao VS Code, Windows, Microsoft 365, etc.)
- **GHB**: GitHub Copilot (Copilot tradicional, integrado ao GitHub e editores de código)

## Índice de Diretrizes Detalhadas

- [Diretrizes Técnicas do Ambiente Local](./copilot-diretrizes/diretrizes_tecnicas.md) <!-- Consulte para requisitos de hardware, ambiente Python, CUDA, troubleshooting de GPU, etc. -->
- [Convenções de Código e Documentação](./copilot-diretrizes/convenções_codigo.md) <!-- Use ao gerar código, revisar padrões de nomenclatura, docstrings e organização de código. -->
- [Diretrizes para Projetos Clonados de Terceiros](./copilot-diretrizes/projetos_terceiros.md) <!-- Consulte ao lidar com projetos de terceiros, customizações, versionamento e separação de repositórios. -->
- [Execução de Scripts e Ativação de venv no Windows](./copilot-diretrizes/diretrizes_execucao_venv_windows.md) <!-- Use sempre que for ativar venv ou rodar scripts Python no Windows. -->
- [Exemplos e Casos Especiais](./copilot-diretrizes/exemplos_casos_especiais.md) <!-- Consulte para procedimentos de atualização de pendências, setup, CI, workflows e casos não convencionais. -->
- [Rodadas de Debate e Encerramento](./copilot-diretrizes/diretrizes_debate.md) <!-- Siga obrigatoriamente ao conduzir debates entre modelos de IA, consolidar decisões e registrar atas. -->
