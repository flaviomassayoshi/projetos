# ManifestoMCP.md — ScarecrowLab

# AVISO IMPORTANTE

Este manifesto é autossuficiente e incorpora diretamente as diretrizes essenciais do ScarecrowLab, sem depender de referências externas a arquivos `.md`. Todo o arcabouço de diretrizes (arquivos e anexos em `.github/copilot-diretrizes/` e correlatos) é a única fonte da verdade do laboratório. Ao atualizar este manifesto, utilize sempre o template oficial (`.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md`) e incorpore as regras, exemplos e fluxos dos anexos, garantindo que o MCP compreenda integralmente o funcionamento do laboratório.

## 1. Objetivo do Manifesto
Consolidar, em um único documento, as diretrizes, fluxos e templates necessários para o MCP atuar de forma rastreável, padronizada e alinhada à identidade do ScarecrowLab. Público-alvo: operadores do MCP e humanos responsáveis pela governança do laboratório.

## 2. Visão Geral
O ScarecrowLab é um laboratório dedicado à integração, automação e governança de agentes de IA, com foco em modularização, rastreabilidade e colaboração estruturada.

## 3. Princípios Centrais
- Modularização e separação de responsabilidades: cada subprojeto, integração ou automação deve ser isolado e documentado.
- Rastreabilidade: todas as decisões, fluxos, pendências e entregas devem ser registradas em changelogs, atas e checklists.
- Automação incremental: priorizar automações que possam ser evoluídas gradualmente, sempre com rastreabilidade.
- Comunicação padronizada: uso obrigatório de checklists, prompts de continuidade, sinalização de status e templates para garantir clareza e rastreabilidade.
- Compatibilidade e clareza para o MCP: todo fluxo, comando e template deve ser compreensível e operacional para o MCP.

## 4. Fluxograma Operacional
```
1. Apresentar plano de ação com etapas previstas
2. Executar cada etapa sinalizando início, andamento e conclusão
3. Converter o plano de ação em checklist de entrega ao final, marcando cada item como concluído
4. Justificar se o checklist/plano será temporário ou persistente, conforme critérios do arcabouço
5. Registrar e referenciar artefatos persistentes em changelog e/ou índice de pendências
```

## 5. Integração MCP — Orientações e Migração
O manifesto consolidado substitui o processo antigo de arquivo-resumo. O MCP deve operar diretamente a partir deste arquivo, consultando sempre os anexos para detalhes e exemplos completos.

## 6. Como Funciona
O fluxo padrão envolve: apresentação de plano de ação, execução sinalizada, checklist de entrega, justificativa de persistência, registro de artefatos e consulta aos anexos para templates e exemplos. Subprojetos são organizados em pastas dedicadas, com README, checklists e atas.

## 7. Protocolo de Conversa Orquestrada
Toda comunicação entre agentes deve ser mediada pelo orquestrador humano. O MCP deve gerar prompts e interações seguindo o padrão do template de conversa IA, com comandos padronizados, contexto, tarefas, critérios de sucesso e referência. O histórico deve ser completo e rastreável.

Exemplo de prompt (conforme template de conversa IA):
```
@orquestrador: @mcp: Atualizar checklist de entrega conforme instruções abaixo.

Contexto:
- Nova pendência identificada no subprojeto X.

Tarefas:
1. Criar checklist de entrega.
2. Registrar changelog.

Critérios de sucesso:
- Checklist criado e vinculado ao subprojeto.
- Changelog registrado.

Referência: ata_debate_2025-10-08.md
```

## 8. Templates Essenciais (exemplos reais)
- Checklist de entrega:
  - [ ] Sinalizar início de cada etapa
  - [ ] Comunicar andamento/status intermediário
  - [ ] Sinalizar encerramento de cada etapa
  - [ ] Utilizar prompts de continuidade quando necessário
- Changelog:
  - Data/hora: 2025-10-08
  - Responsável: MCP
  - Descrição: Checklist X concluído
  - Status final: concluído
  - Link: ./checklist_X.md
- Plano de ação:
  - 1. Mapear contexto
  - 2. Executar etapas
  - 3. Registrar justificativa
- Ata:
  - Data: 2025-10-08
  - Participantes: MCP, Orquestrador
  - Decisões: ...

## 9. Diretrizes para Versionamento de Arquivos Markdown
- Nomear arquivos por tema/data (ex: checklist_X.md, ata_debate_2025-10-08.md)
- Manter histórico incremental, nunca sobrescrever decisões
- Usar changelog para registrar encerramentos
- Toda entrega, debate ou decisão deve ser registrada em arquivos próprios, seguindo convenções do laboratório.

## 10. Exemplo de Conversa Orquestrada
```
@orquestrador: @mcp: Atualizar checklist de entrega conforme instruções abaixo.

Contexto:
- Nova pendência identificada no subprojeto X.

Tarefas:
1. Criar checklist de entrega.
2. Registrar changelog.

Critérios de sucesso:
- Checklist criado e vinculado ao subprojeto.
- Changelog registrado.

Referência: ata_debate_2025-10-08.md
```

## 11. Glossário Essencial
- Artefato persistente: documento salvo para rastreabilidade
- Checklist de entrega: lista de etapas executadas, sinalizadas e justificadas
- MCP: Microsoft Copilot
- Orquestrador: humano que media prompts, revisões e validações
- Plano de ação: sequência de etapas para um objetivo, sempre sinalizada e registrada

## 12. Como o MCP Atua no ScarecrowLab
O MCP deve apresentar plano de ação, sinalizar início, andamento e conclusão de cada etapa, justificar persistência, registrar ações em changelogs, atas e checklists, e utilizar sempre os templates e exemplos deste manifesto. Toda entrega deve ser rastreável, auditável e compreensível sem necessidade de consulta a outros arquivos.

## 13. Resumo
O ScarecrowLab é referência em integração, rastreabilidade e governança de agentes de IA, promovendo automação, clareza e colaboração estruturada, com foco total na operação do MCP. Este manifesto deve ser sempre atualizado utilizando o template oficial, incorporando as diretrizes dos anexos e garantindo autossuficiência para o MCP.

> Sempre que atualizar o manifesto, garanta que ele seja autossuficiente, reflita a identidade e os fluxos vigentes do laboratório, e seja compatível com o MCP (Microsoft Copilot).
