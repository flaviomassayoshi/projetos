
# Manifesto Consolidado — ScarecrowLab (MCP)

## 1. Objetivo do Manifesto
Este manifesto consolida todas as diretrizes, fluxos, templates e exemplos necessários para a atuação do agente MCP (Microsoft Copilot) no ScarecrowLab. Serve como referência única e autoexplicativa para operação, automação e rastreabilidade de pendências, subprojetos e integrações entre IAs.

## 2. Visão Geral
O ScarecrowLab é um laboratório de integração, automação e governança de projetos colaborativos, com foco em modularidade, rastreabilidade e atuação proativa de agentes de IA. O manifesto centraliza práticas, exemplos e comandos para garantir padronização e eficiência.
# Manifesto Consolidado — ScarecrowLab (MCP)

## 1. Objetivo do Manifesto
Este manifesto consolida todas as diretrizes, fluxos, templates e exemplos necessários para a atuação do agente MCP (Microsoft Copilot) no ScarecrowLab. Serve como referência única e autoexplicativa para operação, automação e rastreabilidade de pendências, subprojetos e integrações entre IAs.

## 2. Visão Geral
O ScarecrowLab é um laboratório de integração, automação e governança de projetos colaborativos, com foco em modularidade, rastreabilidade e atuação proativa de agentes de IA. O manifesto centraliza práticas, exemplos e comandos para garantir padronização e eficiência.

## 3. Princípios Centrais
- Modularização de subprojetos
- Rastreabilidade de decisões e entregas
- Automação de fluxos e registros
- Integração transparente entre agentes de IA
- Uso de checklists, changelogs e atas

## 4. Fluxograma Operacional
```
Pendência → Plano de Ação → Execução → Checklist → Changelog/Ata → Encerramento
```

## 5. Integração MCP — Orientações e Migração
O MCP deve operar exclusivamente a partir deste manifesto consolidado, sem depender de consultas externas. Toda atuação, registro e automação devem seguir as diretrizes e exemplos aqui descritos.

## 6. Como Funciona
- Subprojetos organizados em pastas dedicadas
- Pendências registradas como temas ou tarefas
- Planos de ação e checklists para cada entrega
- Changelogs e atas para rastreabilidade
- Debates e decisões documentados
- Todos os status, pendências e checklists de subprojetos devem ser consultados no painel central `.github/painel_subprojetos.md`

## 7. Protocolo de Conversa Orquestrada
O orquestrador humano coordena prompts e libera o MCP para atuação. O MCP deve utilizar o template de conversa IA ampliado (`.github/ia_conversas/TEMPLATE_CONVERSA_IA.md`) ao gerar prompts, conforme protocolo do arcabouço.

O formato ampliado do template de conversa IA inclui os seguintes campos obrigatórios:
- Contexto
- Artefatos envolvidos (ex: checklist, changelog, README, ata, etc.)
- Subprojeto relacionado
- Tarefas
- Status atual da pendência
- Justificativa da ação
- Critérios de sucesso
- Links de referência
- Prompt detalhado (espaço para maiores informações, conteúdo de artefatos)

**Exemplo prático de conversa orquestrada (formato ampliado):**
```
@orquestrador:
@mcp: Atualizar checklist de entrega conforme instruções abaixo.

Contexto:
- Nova pendência identificada no subprojeto X.

Artefatos envolvidos:
- Checklist, changelog, README

Subprojeto relacionado:
- agente-integrador

Tarefas:
1. Criar checklist de entrega.
2. Registrar changelog.

Status atual da pendência:
- Checklist não iniciado

Justificativa da ação:
- Nova decisão registrada em ata, exige atualização do fluxo.

Critérios de sucesso:
- Checklist criado e vinculado ao subprojeto.
- Changelog registrado.

Links de referência:
- ata_debate_2025-10-08.md

Prompt detalhado:
- (Espaço para maiores informações, conteúdo de artefatos, instruções adicionais ou contexto expandido)

@mcp:
Checklist criado e changelog registrado conforme solicitado.
```

## 8. Templates Essenciais (com exemplos reais)
### Template de Checklist de Entrega
```
Checklist: Atualização do README — agente-integrador
- [x] Revisar ata de 2025-10-12
- [x] Atualizar README com novo fluxo
- [x] Criar changelog com justificativa
- [x] Vincular checklist ao subprojeto
```

### Template de Changelog
```
- Data/hora: 2025-10-08
- Responsável: GitHub Copilot
- Descrição: Checklist X concluído
- Status final: concluído
- Link para checklist/ata: ./checklist_X.md
```

### Template de Plano de Ação
```
Plano de ação:
1. Analisar pendência
2. Propor etapas
3. Executar cada etapa
4. Converter em checklist
5. Registrar changelog
```

## 9. Diretrizes para Versionamento de Arquivos Markdown
- Nomear arquivos de checklist como `CHECKLIST_<tema>.md`
- Changelogs em `.github/changelog/<tema>.md`
- Atas em `ata_<data>_<tema>.md`
- Manter histórico e rastreabilidade

## 10. Exemplo de Conversa Orquestrada
```
@orquestrador:
@mcp: Validar se o arquivo `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` está bem elaborado para garantir que o manifesto consolidado atenda plenamente aos objetivos do ScarecrowLab.

Contexto:
- O template de atualização de manifesto foi revisado para incorporar o painel central de subprojetos e garantir rastreabilidade, validação automática e atuação proativa do MCP/GHC.

Artefatos envolvidos:
- TEMPLATE_ATUALIZACAO_MANIFESTO.md
- painel_subprojetos.md

Subprojeto relacionado:
- arcabouço oficial

Tarefas:
1. Analisar se o template contempla todos os campos e instruções necessários para rastreabilidade e governança.
2. Verificar se a referência ao painel central de subprojetos está clara e suficiente.
3. Sugerir ajustes, se necessário, para garantir alinhamento com os objetivos do manifesto consolidado.

Status atual da pendência:
- Template revisado, aguardando validação do MCP.

Justificativa da ação:
- Garantir que o fluxo de atualização de manifestos seja robusto, rastreável e compatível com a atuação proativa do MCP/GHC.

Critérios de sucesso:
- Confirmação do MCP de que o template está adequado, ou recebimento de sugestões de melhoria.

Links de referência:
- .github/TEMPLATE_ATUALIZACAO_MANIFESTO.md
- .github/painel_subprojetos.md

Prompt detalhado:
- Caso identifique lacunas, ambiguidade ou oportunidades de melhoria, detalhe as recomendações para que o arcabouço permaneça autossuficiente e alinhado à governança do laboratório.
```

## 11. Glossário Essencial
- Pendência: tarefa ou decisão não concluída
- Checklist: lista de etapas de entrega
- Changelog: registro de alterações
- Ata: registro formal de decisões
- Orquestrador: humano que coordena prompts
- MCP: Microsoft Copilot

## 12. Como o MCP Atua no ScarecrowLab
O MCP executa planos de ação, propõe checklists, registra changelogs e sinaliza pendências automaticamente, sempre que identificar temas abertos, checklists incompletos ou decisões sem rastreabilidade. Toda validação de subprojetos, status e pendências deve ser feita a partir do painel central `.github/painel_subprojetos.md`.

## 13. Resumo
O ScarecrowLab prioriza automação, rastreabilidade e colaboração entre agentes de IA, com o MCP atuando de forma proativa e transparente, sempre guiado por este manifesto consolidado.

---

## 14. Casos Reais e Pendências Simuladas
**Exemplo de Pendência Simulada:**
```
Pendência: Atualizar README do subprojeto "agente-integrador"
Contexto: Novo fluxo de integração foi aprovado na ata de 2025-10-12
Tarefas:
1. Revisar ata
2. Atualizar README
3. Criar changelog
Critérios de sucesso:
- README atualizado com novo fluxo
- Changelog registrado
Referência: ata_debate_2025-10-12.md
```

## 15. Checklist Real com Status
```
Checklist: Atualização do README — agente-integrador
- [x] Revisar ata de 2025-10-12
- [x] Atualizar README com novo fluxo
- [x] Criar changelog com justificativa
- [x] Vincular checklist ao subprojeto
```

## 16. Critérios para Atuação Proativa do MCP
- Quando há pendência registrada com tarefas não concluídas
- Quando há checklist incompleto ou changelog ausente
- Quando há ata com decisões sem plano de ação vinculado

## 17. Prompt de Ativação Proativa
```
@orquestrador: @mcp: Atue proativamente sobre pendências registradas no manifesto. Priorize aquelas com checklist incompleto ou changelog ausente.
```

> Sempre que atualizar o manifesto, garanta que ele seja autossuficiente, reflita a identidade e os fluxos vigentes do laboratório, e seja compatível com o MCP (Microsoft Copilot).
