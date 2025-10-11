# AVISO IMPORTANTE

Para instruções detalhadas de atualização, checklist MVP e critérios, consulte exclusivamente o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` e o arcabouço em `.github/copilot-diretrizes/` e `ia_conversas/`.

# MANIFESTO CONSOLIDADO — SCARECROWLAB (MCP)

## 0. Sumário dos Anexos e Templates — ScarecrowLab

- **Glossário:** Define termos essenciais e siglas do laboratório.
- **Fluxos Gerais para Agentes:** Passo a passo padrão para execução de tarefas por agentes MCP/GHC.
- **Checklist de Comunicação:** Critérios mínimos para comunicação clara e rastreável entre agentes.
- **Fluxos de Encerramento e Changelog:** Como registrar encerramentos, gerar changelogs e prompts de continuidade.
- **Diretrizes para Subprojetos:** Regras para criação, organização e rastreabilidade de subprojetos.
- **Protocolo de Orquestração via Chat:** Regras e exemplos para prompts, aprovação e fluxo MCP <-> GHC <-> orquestrador.
- **Templates Essenciais:** Modelos padronizados de checklist, changelog, ata, plano de ação e conversa IA.
- **Painel Central de Subprojetos:** Fonte única para status, pendências e checklists de todos os subprojetos.
- **Diretrizes Técnicas:** Recomendações para ambiente local, integração de agentes e automação.
- **Convenções de Código:** Padrões de nomenclatura, organização e comentários para código do laboratório.
- **Projetos de Terceiros:** Regras para integração e customização de projetos externos.
- **Execução de venv no Windows:** Orientações para ambientes virtuais Python no Windows.
- **Instruções de Setup e CI:** Setup de ambiente, integração contínua e automações.
- **Diretrizes de Debate:** Regras para rodadas de debate: checkpoints, atas incrementais, registro de decisões e prompts padronizados.
- **Fluxo de Revisão de Diretrizes:** Processo padronizado de revisão e atualização das diretrizes.
- **Checklists Práticos:** Exemplos sintéticos de checklists para uso imediato.
- **Exemplos de Artefatos:** Modelos resumidos de README, checklist, changelog e ata de subprojetos.

---

## 1. Objetivo do Manifesto

Consolidar regras, fluxos e exemplos essenciais para operação do ScarecrowLab, servindo como referência única para o MCP. Garantir rastreabilidade, governança e automação dos processos do laboratório, fornecendo diretrizes para humanos e para o agente MCP.

## 2. Visão Geral

O ScarecrowLab é um laboratório de integração, automação e governança de projetos de IA, com foco em modularização, rastreabilidade e atuação proativa de agentes. O manifesto define o arcabouço operacional, os fluxos principais e critérios de automação do laboratório.

## 3. Princípios Centrais

- Modularização de subprojetos
- Rastreabilidade de decisões e artefatos
- Automação de fluxos e validações
- Integração entre agentes de IA (MCP, GHC, etc.)
- Transparência e governança

## 4. Fluxograma Operacional

```
[Pendência aberta] → [Plano de ação] → [Checklist de entrega] → [Execução] → [Changelog/ata] → [Prompt de continuidade] → [Encerramento]
```

## 5. Integração MCP — Orientações e Migração

O manifesto consolidado é o único documento operacional para o MCP. O MCP deve operar exclusivamente a partir deste arquivo, sem consultar anexos externos. Toda recomendação do MCP só pode ser implementada se estiver alinhada com as diretrizes do manifesto consolidado.

## 6. Como Funciona

- Cada subprojeto possui pasta própria, README, checklists e changelogs.
- O painel central de subprojetos é a fonte única para status, pendências e checklists.
- Toda execução relevante deve apresentar plano de ação, checklist de entrega e justificativa de persistência.
- Artefatos só são válidos se seguirem os modelos e critérios deste manifesto.

## 7. Protocolo de Conversa Orquestrada

- Toda comunicação entre MCP, GHC e orquestrador segue o protocolo de orquestração e o template de conversa IA.
- O MCP deve gerar prompts alinhados a esses artefatos, sempre usando blocos markdown simples e identificando claramente artefatos embutidos.
- Exemplo sintético de prompt:
    ```
    @ghc: Execute o checklist abaixo e registre o changelog.
    ```

## 8. Templates Essenciais (exemplos sintéticos)

### Checklist de Entrega
- [ ] Etapa 1 (✔️/⏳/❌)
- [ ] Etapa 2 (✔️/⏳/❌)

### Changelog
- Data: AAAA-MM-DD
- Responsável: Nome
- Descrição: Resumo da alteração
- Status final: concluído/pendente
- Link para checklist/ata: ./caminho.md

### Plano de Ação
1. Listar etapas previstas
2. Definir critérios de sucesso
3. Justificar persistência (se aplicável)

### Prompt de Retomada
"Próxima etapa: ... | Status: ... | Próximos passos: ..."

## 9. Diretrizes para Versionamento de Arquivos Markdown

- Use nomes claros e padronizados.
- Mantenha histórico de alterações em changelog.
- Atualize o painel central de subprojetos a cada mudança relevante.

## 10. Exemplo de Conversa Orquestrada

```
@orquestrador: @mcp: Analise a pendência abaixo e proponha plano de ação.
Pendência: Atualizar README do subprojeto X.
```

## 11. Glossário Essencial

- **Arcabouço:** conjunto de diretrizes, templates e regras do laboratório.
- **Artefato persistente:** documento obrigatório para rastreabilidade (ex: checklist, changelog, ata).
- **Checklist de entrega:** lista de etapas executadas em uma interação.
- **Changelog:** registro de alterações, decisões e status final.
- **Plano de ação:** sequência de etapas para atingir um objetivo.
- **Prompt de retomada:** mensagem de continuidade após uma etapa.
- **Subprojeto:** iniciativa registrada com pasta própria.
- **Painel central de subprojetos:** fonte única para status, pendências e checklists.

## 12. Como o MCP Atua no ScarecrowLab

- MCP deve sempre apresentar plano de ação, checklist e justificativa de persistência.
- MCP registra artefatos previstos (checklist, changelog, ata, plano de ação).
- MCP só executa recomendações aprovadas pelo orquestrador.

## 13. Resumo

O manifesto consolida a identidade, propósito e fluxos do ScarecrowLab, garantindo rastreabilidade, governança e automação, com foco em operação autônoma e auditável pelo MCP.

---

## 14. Casos Reais e Pendências Simuladas (resumidos)

```markdown
Pendência: Atualizar README do subprojeto X
Resumo: Novo fluxo aprovado em ata. Tarefas: revisar ata, atualizar README, criar changelog. Critério: README e changelog atualizados.
// Para detalhes completos, solicite ao GHC via prompt.
```

---

## 15. Checklist Real com Status (resumido)

```markdown
Checklist: Atualização do README — subprojeto X
- [x] Revisar ata
- [x] Atualizar README
- [x] Criar changelog
// Para checklist completo, solicite ao GHC via prompt.
```

---

## 16. Critérios para Atuação Proativa do MCP

- Quando há pendência registrada com tarefas não concluídas
- Quando há checklist incompleto ou changelog ausente
- Quando há ata com decisões sem plano de ação vinculado

---

## 17. Prompt de Ativação Proativa

```markdown
@orquestrador: @mcp: Atue proativamente sobre pendências registradas no manifesto. Priorize aquelas com checklist incompleto ou changelog ausente.
```

---

## 18. Artefato embutido no prompt (opcional)

Em situações onde o MCP ou orquestrador precise processar o conteúdo bruto de um artefato (ex: README, checklist, changelog) diretamente no corpo do prompt, o conteúdo pode ser incluído usando blocos markdown aninhados.

**Exemplo funcional:**
```markdown
@ghc: Analise o seguinte README e gere um checklist de pendências:

```markdown
# README — Subprojeto X
Fluxo: ...
Pendências:
- [ ] Ajustar integração
- [ ] Revisar documentação
```
```

Oriente sempre a identificar claramente o início e fim do artefato embutido, usando blocos markdown aninhados se necessário.

-----

--- FIM DO MANIFESTO GERADO ---
