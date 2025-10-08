# 💡 Proposta de Expansão das Diretrizes para Agentes de IA e GitHub Copilot

## Contexto

O sistema atual de diretrizes para agentes de IA está modular, automatizado e rastreável. Com o aumento dos subprojetos e integração do GitHub Copilot, é necessário expandir práticas para garantir escalabilidade, clareza e colaboração inteligente.

## Ideias de Melhoria

1. **Níveis de Checklist por Complexidade**
   - Definir níveis de checklist (mínimo, intermediário, completo) conforme a tarefa.
   - Tarefas simples: apenas prompt de continuidade; tarefas complexas: changelog e pendências.

2. **Indexação Inteligente de Ideias**
   - Criar `ideias/index.md` com tags (tema, status, responsável).
   - Copilot sugere nomes únicos/descritivos para novas ideias.

3. **Sugestões Guiadas do Copilot**
   - Bloco de contexto padrão para Copilot entender o escopo do subprojeto.
   - Copilot pode propor refatorações/testes com base em pendências abertas.

4. **Automação de Changelog e Pendências**
   - Automatizar atualização de `.github/PENDENCIAS.md` e `changelog/<tema>.md` via commits/ações do agente.
   - Copilot pode gerar entradas de changelog a partir de diffs/contexto.

5. **Interpretação de Reações como Confirmação**
   - Validar se 👍 ou “ok” podem ser interpretados como autorização explícita pelo Copilot em fluxos interativos.

## Objetivo

Expandir as diretrizes para que o GitHub Copilot colabore de forma mais contextual, segura e produtiva com agentes de IA, respeitando versionamento, escopo e documentação.
