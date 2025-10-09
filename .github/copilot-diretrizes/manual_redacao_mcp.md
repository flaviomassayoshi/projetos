# Manual de Redação para o MCP — Minimificado

Objetivo: Padronizar estrutura e estilo dos conteúdos do manifesto para garantir legibilidade, rastreabilidade e atuação eficiente do MCP.

## 1. Estrutura Recomendada
- Usar títulos hierárquicos (##, ###) para segmentar seções
- Agrupar pendências em blocos com checklist e plano de ação
- Manter glossário, exemplos e templates em seções separadas
- Evitar narrativas longas ou instruções misturadas com artefatos

## 2. Artefatos Embutidos
- Incluir conteúdo bruto de arquivos diretamente no corpo do manifesto
- Permitir que MCP ou GHC analisem o conteúdo sem depender de links externos

## 3. Resumo Funcional
- Cada artefato referenciado deve conter:
  - Título claro
  - Resumo breve de função
  - Exemplo funcional (checklist, plano de ação, changelog etc.)

Exemplo:
Título: .github/copilot-diretrizes/checklist_comunicacao.md
Resumo: Define critérios mínimos para comunicação entre agentes MCP e GHC
Checklist:
- [x] Mensagem clara
- [x] Referência ao template
- [ ] Validação pelo orquestrador

## 4. Minimificação de Markdown
- Evitar narrativas desnecessárias
- Padronizar listas e checklists
- Usar nomes de arquivos como títulos
- Centralizar templates em seção única
- Evitar duplicidade de artefatos

## 5. Bloco Padronizado
Título: .github/TEMPLATE_PLANO_ACAO.md
Resumo: Template para planos de ação vinculados a pendências registradas
Exemplo funcional:
1. Analisar pendência
2. Executar tarefas
3. Registrar checklist

## 6. Glossário Sintético
- MCP: Microsoft Copilot
- GHC: GitHub Copilot Agent
- Checklist: Lista de tarefas
- Changelog: Registro de alterações
- Ata: Registro de decisões
- Orquestrador: Agente que aprova fluxos

## 7. Critérios de Atuação Proativa
- Pendência registrada com tarefas não concluídas
- Checklist incompleto
- Changelog ausente
- Ata sem plano de ação vinculado

## 8. Prompt de Ativação
@orquestrador: @mcp: Atue proativamente sobre pendências registradas. Priorize aquelas com checklist incompleto ou changelog ausente.
