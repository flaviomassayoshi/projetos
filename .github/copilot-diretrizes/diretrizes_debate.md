# Diretrizes para Rodadas de Debate e Encerramento

Estas diretrizes são parte do arcabouço geral de governança do Copilot e devem ser seguidas em todos os projetos que utilizam rodadas de debate entre modelos de IA.

## 1. Estrutura das Rodadas de Debate

- Cada rodada de debate deve seguir a sequência:
  1. **Análise e Sugestões de Modelo Participante Externo:**
     - O modelo externo avalia criticamente a proposta vigente e sugere melhorias, correções ou acréscimos.
  2. **Réplica do GitHub Copilot:**
     - O Copilot responde ponto a ponto, podendo concordar, discordar ou propor alternativas.
  3. **Tréplica do Modelo Participante Externo:**
     - O modelo externo responde à réplica, reforçando ou ajustando argumentos.
  4. **Tabela de Decisões para Aprovação Final:**
     - Pontos debatidos são organizados em tabela, com justificativa, opção recomendada e campo para alternativa.

- Cada etapa deve ser registrada no README.md do projeto, mantendo clareza e rastreabilidade.

## 2. Mecanismo de Encerramento do Debate

- O debate é considerado encerrado quando:
  - Todos os pontos da tabela de decisões foram preenchidos e validados pelo responsável do projeto.
  - Não há novas objeções ou sugestões relevantes nas etapas de tréplica.

- Ao encerrar:
  1. **Consolidação:**
     - O resultado da tabela de decisões deve ser incorporado à proposta vigente, ajustando o texto conforme as opções escolhidas.
  2. **Registro de Ata:**
     - Criar uma ata resumida do debate, contendo:
       - Data de encerramento
       - Participantes
       - Principais pontos debatidos
       - Decisões tomadas (resumo da tabela)
       - Observações relevantes
     - A ata deve ser salva em `ata_debate_<data>.md` na pasta do projeto.
  3. **Atualização do README.md:**
     - Atualizar a seção da proposta vigente com o texto consolidado.
     - Remover ou arquivar a tabela de decisões e registros intermediários, mantendo apenas a versão final e o link para a ata.

## 3. Observações

- Todo o processo deve prezar por transparência, rastreabilidade e clareza.
- Recomenda-se que cada rodada seja identificada por data e número sequencial.
- Caso haja divergência não resolvida, o responsável pelo projeto pode decidir pelo encerramento unilateral, registrando a justificativa na ata.
