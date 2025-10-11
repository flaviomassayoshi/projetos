# Fluxos de Encerramento, Changelog e Prompt de Retomada (IA-only)

Este anexo consolida fluxos de encerramento, exemplos de changelog e modelo de prompt de retomada para agentes de IA.

## Fluxos de Encerramento e Changelog


Para registrar o encerramento de temas/checklists, utilize o [Template de Changelog](./template_changelog.md).

**Atenção:** Alterações no manifesto consolidado devem SEMPRE ser feitas via template `.github/copilot-diretrizes/TEMPLATE_ATUALIZACAO_MANIFESTO.md`. Nunca edite o manifesto diretamente.

Exemplo:

```
- Data/hora: 2025-10-08
- Responsável: GitHub Copilot
- Descrição: Checklist X concluído
- Status final: concluído
- Link para checklist/ata: ./checklist_X.md
```

## Prompt de Retomada

Sempre que encerrar uma etapa ou checklist, gere um prompt de continuidade contendo:
- Contexto resumido
- Status atual
- Próximos passos sugeridos

Exemplo de prompt de retomada:

"Prompt de continuidade:
- Próxima etapa do checklist: validar se todos os fluxos, templates e exemplos estão acessíveis e rastreáveis nos anexos.
- Todos os arquivos de referência e rastreabilidade já estão criados e indexados.
- Ao retomar, continue a partir da etapa de complementação/criação dos anexos, validando se todos os fluxos e exemplos estão acessíveis."
