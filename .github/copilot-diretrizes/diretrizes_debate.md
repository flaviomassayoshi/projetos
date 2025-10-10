
# Diretrizes para Rodadas de Debate e Encerramento

Estas diretrizes são parte do arcabouço geral de governança do Copilot e devem ser seguidas em todos os projetos que utilizam rodadas de debate entre modelos de IA.

## 1. Estrutura das Rodadas de Debate

O fluxo de debate é padronizado para todos os subprojetos, com foco em modularização, rastreabilidade e amadurecimento incremental:

1. **Elaboração de Pontos e Subpontos pelo Responsável:**
   - O responsável pode propor novos pontos ou subpontos (ex: D1.1, D1.2), criando arquivos próprios em `debates/`.
   - Recomenda-se registrar data/hora, contexto e vincular subpontos ao tema principal.

2. **Ajustes/Propostas do Copilot:**
   - O Copilot pode sugerir ajustes, alternativas ou pedir esclarecimentos antes da rodada formal.

3. **Abertura de Nova Rodada de Debate:**
   - Cada rodada/subponto deve ser numerada/sequenciada, com separadores visuais e tema claro.
   - Recomenda-se criar um `README_DEBATE.md` por debate, com índice e status dos subpontos (ex: Encerrado ✅, Em andamento 🔄, Pendente ⏳).

4. **Checkpoints Intermediários:**
   - Registrar blocos de progresso por subponto, sinalizando etapas concluídas e pendentes (ex: análise crítica, réplica, tréplica, decisão).

5. **Análise e Sugestões de Modelo Participante Externo:**
   - Análise crítica obrigatória, evitando concordância automática.
   - Todos os modelos devem justificar suas posições, promovendo debates construtivos.

6. **Réplica e Tréplica:**
   - O Copilot responde ponto a ponto, seguido de tréplica do modelo externo, sempre com argumentação fundamentada.

7. **Tabela de Decisões para Aprovação Final:**
   - Ao final de cada rodada/subponto, preencher tabela de decisões com propostas, justificativas e opções escolhidas.

- Debates podem ocorrer em paralelo, cada um com arquivos e subpontos próprios.
- O README do subprojeto deve conter sumário executivo, proposta vigente e links para debates/atas.

### Template para Nova Rodada/Subponto

Título: Rodada de Debate #N — <tema ou subponto> (Data: DD/MM/AAAA)
ID: D1.2

Ponto sugerido pelo responsável:
<Descreva o ponto, contexto, motivação, etc.>

Ajustes/Propostas do Copilot:
<Propostas de ajuste, alternativas, dúvidas ou esclarecimentos do Copilot.>

Checkpoint D1.2 — 2025-10-10
- [x] Análise crítica inicial
- [x] Réplica do MCP
- [ ] Tréplica pendente
- [ ] Consolidação de decisão

Análise e Sugestões de Modelo Participante Externo:
<Análise crítica, sugestões de melhoria, correções ou acréscimos.>

Réplica do GitHub Copilot:
<Resposta ponto a ponto do Copilot.>

Tréplica do Modelo Participante Externo:
<Resposta final do modelo externo.>

Tabela de Decisões para Aprovação Final:

| Item | Proposta | Justificativa | Opção Escolhida | Outra Opção |
|------|----------|---------------|-----------------|-------------|
| 1    | ...      | ...           | ...             | ...         |

## 2. Mecanismo de Encerramento do Debate

- O encerramento pode ser feito por subponto, com ata e atualização incremental do README_DEBATE.md e do README principal.
- Para cada subponto encerrado:
   - Marque na tabela de decisões o status (“aceito”, “rejeitado”, “em aberto”).
   - Gere ata por tema ou grupo de subpontos, nomeando conforme o assunto principal.
   - Registre consenso, maioria ou decisão unilateral, justificando na ata.
   - Atualize a proposta vigente e o índice de status dos subpontos.

- O debate geral é encerrado quando todos os subpontos relevantes estiverem resolvidos e não houver novas objeções.

## 3. Observações

- Todo o processo deve prezar por transparência, rastreabilidade e clareza.
- Recomenda-se identificar cada rodada/subponto por data e ID.
- Em caso de divergência não resolvida, o responsável pode encerrar unilateralmente, justificando na ata.
