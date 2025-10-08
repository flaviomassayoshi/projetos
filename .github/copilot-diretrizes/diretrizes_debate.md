# Diretrizes para Rodadas de Debate e Encerramento

Estas diretrizes são parte do arcabouço geral de governança do Copilot e devem ser seguidas em todos os projetos que utilizam rodadas de debate entre modelos de IA.

## 1. Estrutura das Rodadas de Debate


O fluxo de debate é padronizado para todos os subprojetos:
   1. **Elaboração de Pontos pelo Responsável:**
       - O responsável pode, a qualquer momento, propor novos pontos, dúvidas ou sugestões para debate, criando um novo arquivo em uma subpasta `debates/` do subprojeto (ex: `debates/debate_<data>_<tema>.md`). Recomenda-se registrar data/hora e contexto.
  2. **Ajustes/Propostas do Copilot:**
     - O Copilot propõe ajustes, alternativas ou pede esclarecimentos antes de abrir a rodada formal.
  3. **Abertura de Nova Rodada de Debate:**
     - Cada rodada deve ser numerada/sequenciada no arquivo de debate, com separadores visuais e tema/ponto debatido.
  4. **Análise e Sugestões de Modelo Participante Externo:**
     - O modelo externo avalia criticamente os pontos propostos e sugere melhorias, correções ou acréscimos.
  5. **Réplica do GitHub Copilot:**
     - O Copilot responde ponto a ponto, podendo concordar, discordar ou propor alternativas.
  6. **Tréplica do Modelo Participante Externo:**
     - O modelo externo responde à réplica, reforçando ou ajustando argumentos.
  7. **Tabela de Decisões para Aprovação Final:**
     - Pontos debatidos são organizados em tabela, com justificativa, opção recomendada e campo para alternativa. A tabela deve ser obrigatória ao final de cada rodada, mesmo que parcial.

- O responsável pode iniciar novas rodadas a qualquer momento, bastando criar novos arquivos de debate. Não há limite de rodadas.
- Permite múltiplos pontos em paralelo, com arquivos separados.
- O README de cada subprojeto deve conter apenas o sumário executivo, proposta vigente consolidada e links para os arquivos de debate/atas.

### Template para Nova Rodada de Debate

```
### Rodada de Debate #N — <tema ou ponto debatido> (Data: DD/MM/AAAA)

**Ponto sugerido pelo responsável:**  
<Descreva o ponto, contexto, motivação, etc.>

**Ajustes/Propostas do Copilot:**  
<Propostas de ajuste, alternativas, dúvidas ou esclarecimentos do Copilot.>

#### Análise e Sugestões de Modelo Participante Externo
<Análise crítica, sugestões de melhoria, correções ou acréscimos.>

#### Réplica do GitHub Copilot
<Resposta ponto a ponto do Copilot.>

#### Tréplica do Modelo Participante Externo
<Resposta final do modelo externo.>

#### Tabela de Decisões para Aprovação Final

| Item | Proposta | Justificativa | Opção Escolhida | Outra Opção |
|------|----------|---------------|-----------------|-------------|
| 1    | ...      | ...           | ...             | ...         |
```

## 2. Mecanismo de Encerramento do Debate

- O encerramento pode ser feito por ponto/rodada, não sendo necessário aguardar o fechamento de todo o debate.
- Para cada ponto encerrado:
   - Marque na tabela de decisões se está “aceito”, “rejeitado” ou “em aberto para nova rodada”.
   - Gere uma ata por tema ou grupo de pontos relacionados, nomeando conforme o assunto principal debatido.
   - Registre explicitamente se houve consenso, maioria ou decisão unilateral do responsável, justificando no campo de observações da ata.
   - Atualize incrementalmente a proposta vigente no README, mantendo o histórico das rodadas e decisões.

- O debate geral é considerado encerrado quando todos os pontos relevantes estiverem marcados como “aceito” ou “rejeitado” e não houver novas objeções ou sugestões relevantes nas etapas de tréplica.

- Ao encerrar:
   1. **Consolidação:**
       - O resultado da tabela de decisões deve ser incorporado à proposta vigente, ajustando o texto conforme as opções escolhidas.
   2. **Registro de Ata:**
       - Criar uma ata resumida do debate, contendo:
          - Data de encerramento
          - Participantes
          - Principais pontos debatidos
          - Decisões tomadas (resumo da tabela)
          - Observações relevantes (incluindo se houve consenso, maioria ou decisão unilateral)
       - A ata deve ser salva em `ata_debate_<data>_<tema>.md` (tema ou assunto principal do debate, de forma abrangente) na pasta do projeto.
   3. **Atualização do README.md:**
       - Atualizar a seção da proposta vigente com o texto consolidado.
       - Remover ou arquivar a tabela de decisões e registros intermediários, mantendo apenas a versão final e o link para a ata.

## 3. Observações

- Todo o processo deve prezar por transparência, rastreabilidade e clareza.
- Recomenda-se que cada rodada seja identificada por data e número sequencial.
- Caso haja divergência não resolvida, o responsável pelo projeto pode decidir pelo encerramento unilateral, registrando a justificativa na ata.
