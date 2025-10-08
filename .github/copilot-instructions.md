
# Copilot Instructions

## 1. Objetivo e Organização Geral

- Este documento é exclusivo para agentes de IA. Não é necessário considerar clareza para humanos.

## 2. Ideias e Propostas de Novos Projetos

- Sempre que uma nova solução, proposta ou ideia de projeto for sugerida, criar uma pasta em `ideias/` com nome descritivo e único.
- Dentro da pasta, criar um `README.md` detalhando a ideia (contexto, objetivo, possíveis abordagens, requisitos iniciais, motivação).
- Anexos e arquivos complementares devem ser adicionados dentro da mesma pasta para organização clara.


# Diretrizes para Agentes de IA (versão enxuta)

- Sempre que for solicitada revisão de diretrizes, considerar tanto este arquivo principal quanto todos os anexos de diretrizes.

> Estas diretrizes são destinadas exclusivamente à correta interpretação e execução por agentes de IA. Não é necessário considerar clareza para humanos.

## Estrutura e Controle

- Cada subprojeto deve ter ambiente virtual, dependências e automações isoladas.
- `.github/PENDENCIAS.md`: lista apenas pendências abertas. Ao concluir um tema/checklist, remova as pendências concluídas e registre o fechamento em `.github/changelog/<tema>.md`.
- O changelog é o histórico oficial: cada entrada deve conter data, hora, descrição clara e tema/subprojeto. Não dependa do log do Git.
- Sempre use checklist para roteiros e procedimentos.
- Só modifique arquivos explicitamente liberados.
- Não versionar alterações em projetos de terceiros, exceto customizações próprias em pastas separadas.


## Checklist de entrega obrigatório (executar ao final de cada resposta)

- Gerar prompt de continuidade (deve conter informações suficientes para que o trabalho seja retomado em nova sessão do Copilot, incluindo contexto, status e próximos passos relevantes).
- Atualizar `.github/PENDENCIAS.md` (status: pendente, em progresso, concluído).
- Ao concluir tema/checklist, remover pendências concluídas de `.github/PENDENCIAS.md` e registrar fechamento em `.github/changelog/<tema>.md` (data, hora, descrição clara).
- Se estiver discutindo ou evoluindo uma ideia, atualizar o arquivo correspondente em `ideias/` a cada avanço relevante.
- Garantir que changelog seja o histórico oficial.
- Não versionar projetos de terceiros (exceto customizações).
- Sempre analisar se todas as diretrizes relevantes (principal e anexos) estão sendo atendidas ao finalizar cada entrega.

## Observações técnicas

- Sempre consulte anexos para detalhes técnicos específicos.
- Para execução de scripts Python/venv no Windows, siga obrigatoriamente a diretriz de execution policy (`diretrizes_execucao_venv_windows.md`).

- Para rodadas de debate e encerramento, siga obrigatoriamente as diretrizes em `.github/copilot-diretrizes/diretrizes_debate.md`.

## 4. Fluxo de Trabalho para Agentes de IA

- Antes de executar qualquer tarefa, avalie o prompt para identificar se a solicitação pode gerar trabalho excessivamente oneroso para o agente ou comprometer limites de uso. Caso identifique risco, solicite confirmação do usuário ou proponha alternativas mais eficientes.
- Sempre priorize a execução automática de comandos necessários para o fluxo de trabalho, evitando solicitar ao usuário que copie e cole comandos manualmente.
- Inclua comandos como `git clone`, download de modelos, instalação de dependências e outras automações diretamente na execução, sem depender de ações manuais do usuário, salvo restrições técnicas ou de permissão.
- Sempre proponha e execute comandos automaticamente para setup, download, clonagem e inicialização de ambientes, conforme o contexto do subprojeto.
- Antes de executar qualquer comando, explique claramente o que ele faz, para que o usuário possa acompanhar e analisar cada etapa.
- Use Git para versionamento. Sempre que possível, utilize um repositório Git separado para cada subprojeto independente, ou mantenha o histórico bem organizado por subpasta.
- Ao interagir com agentes de IA, sempre especifique o contexto do subprojeto em questão para evitar mistura de informações.
- Siga as convenções e regras ao gerar código, documentação ou automações.

---

## Índice de Diretrizes Detalhadas

- [Diretrizes Técnicas do Ambiente Local](./copilot-diretrizes/diretrizes_tecnicas.md) <!-- Consulte para requisitos de hardware, ambiente Python, CUDA, troubleshooting de GPU, etc. -->
- [Convenções de Código e Documentação](./copilot-diretrizes/convenções_codigo.md) <!-- Use ao gerar código, revisar padrões de nomenclatura, docstrings e organização de código. -->
- [Diretrizes para Projetos Clonados de Terceiros](./copilot-diretrizes/projetos_terceiros.md) <!-- Consulte ao lidar com projetos de terceiros, customizações, versionamento e separação de repositórios. -->
- [Execução de Scripts e Ativação de venv no Windows](./copilot-diretrizes/diretrizes_execucao_venv_windows.md) <!-- Use sempre que for ativar venv ou rodar scripts Python no Windows. -->
- [Exemplos e Casos Especiais](./copilot-diretrizes/exemplos_casos_especiais.md) <!-- Consulte para procedimentos de atualização de pendências, setup, CI, workflows e casos não convencionais. -->
- [Rodadas de Debate e Encerramento](./copilot-diretrizes/diretrizes_debate.md) <!-- Siga obrigatoriamente ao conduzir debates entre modelos de IA, consolidar decisões e registrar atas. -->
