
# AVISO IMPORTANTE

O arquivo raiz e central do arcabouço de diretrizes é o `copilot-instructions.md`, localizado em `.github/`. Todo o arcabouço de diretrizes (arquivos e anexos em `.github/copilot-diretrizes/` e correlatos) é a única fonte da verdade do ScarecrowLab.

O manifesto consolidado tem como foco central o agente MCP (Microsoft Copilot), reunindo em um único documento todos os fluxos, templates e comandos essenciais para sua operação no ScarecrowLab. Ao atualizar o manifesto, não basta referenciar arquivos `.md` ou anexos: é obrigatório compreender e incorporar diretamente as diretrizes, regras e exemplos dos anexos ao texto do manifesto, garantindo que o MCP entenda exatamente o funcionamento do laboratório sem depender de consultas externas. Toda consolidação deve ser fiel ao arcabouço vigente e não substitui a consulta ao arcabouço original para decisões estratégicas ou revisões profundas.

# TEMPLATE DE ATUALIZAÇÃO DO MANIFESTO — SCARECROWLAB (MCP)

**Objetivo:** Garantir que toda atualização do manifesto produza um arquivo único, detalhado e autoexplicativo (formato `ManifestoMCP.md`), compatível com o agente MCP (Microsoft Copilot) e adequado para comunicação e operação no contexto do ScarecrowLab.


## Instruções de Uso


## Dados da Atualização

### Subprojetos Impactados (obrigatório)
Liste todos os subprojetos afetados por esta atualização, utilizando nomes exatos conforme o painel central de subprojetos (`.github/painel_subprojetos.md`).
Exemplo:
- agente-integrador
- validacao_ia_multimodelo
- extensoes/xyz

> O MCP/GHC deve validar e consumir informações diretamente do painel central de subprojetos. Caso algum subprojeto citado não esteja presente ou atualizado no painel, sinalizar pendência para revisão.

> O painel central é a fonte única e oficial para status, pendências e checklists de subprojetos. Todos os manifestos e templates devem referenciá-lo para garantir rastreabilidade e atuação proativa.


## Estrutura Recomendada do Manifesto Consolidado

### 1. Objetivo do Manifesto
(Explique o objetivo principal do manifesto e o público-alvo, com clareza para o MCP e para humanos.)

### 2. Visão Geral
(Descreva o propósito do ScarecrowLab, contexto e identidade do laboratório)

### 3. Princípios Centrais
(Listar e explicar os princípios que regem o laboratório: modularização, rastreabilidade, automação, integração entre IAs, etc.)

### 4. Fluxograma Operacional
(Inclua um fluxograma ou diagrama (ASCII/Markdown) ilustrando o ciclo de uma pendência, do plano de ação ao encerramento.)

### 5. Integração MCP — Orientações e Migração
(Explique que o manifesto consolidado é o único documento operacional para o MCP e instrua o MCP a operar diretamente a partir deste arquivo.)

### 6. Como Funciona
(Explique o fluxo de trabalho, organização dos subprojetos, uso de checklists, changelogs, debates, comandos e templates)

### 7. Protocolo de Conversa Orquestrada
(Detalhe o papel do orquestrador, comandos padrão, exemplos simulados e fluxo de comunicação para o MCP. O manifesto deve orientar explicitamente que o MCP utilize o template de conversa IA (`.github/ia_conversas/TEMPLATE_CONVERSA_IA.md`) ao gerar prompts, conforme protocolo do arcabouço.)

### 8. Templates Essenciais (com exemplos reais)
(Inclua todos os templates relevantes para o MCP: checklist, changelog, ata, plano de ação, exemplos práticos.)

### 9. Diretrizes para Versionamento de Arquivos Markdown
(Inclua orientações para nomeação, versionamento e histórico de arquivos colaborativos.)

### 10. Exemplo de Conversa Orquestrada
(Inclua um exemplo prático de interação entre MCP e orquestrador, demonstrando o protocolo de comunicação.)

### 11. Glossário Essencial
(Atualize ou acrescente definições relevantes para o contexto do laboratório, priorizando termos usados no fluxo do MCP.)

### 12. Como o MCP Atua no ScarecrowLab
(Explique o comportamento esperado do MCP, fluxo de execução, registro de ações e rastreabilidade.)

### 13. Resumo
(Consolide a identidade, propósito e diferenciais do ScarecrowLab, com foco no uso pelo MCP.)


---

### 14. Casos Reais e Pendências Simuladas
Inclua exemplos de pendências reais ou fictícias para servir de gatilho à atuação do MCP, permitindo atuação proativa e validação de fluxos.

**Exemplo de Pendência Simulada:**
```markdown
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

---

### 15. Checklist Real com Status
Inclua um checklist preenchido com status reais (✔️, ❌, ⏳) para que o MCP possa sugerir atualizações, sinalizar pendências ou propor encerramentos.

**Exemplo:**
```markdown
Checklist: Atualização do README — agente-integrador
- [x] Revisar ata de 2025-10-12
- [x] Atualizar README com novo fluxo
- [x] Criar changelog com justificativa
- [x] Vincular checklist ao subprojeto
```

---

### 16. Critérios para Atuação Proativa do MCP
Defina quando o MCP pode agir sem comando explícito:
- Quando há pendência registrada com tarefas não concluídas
- Quando há checklist incompleto ou changelog ausente
- Quando há ata com decisões sem plano de ação vinculado

---

### 17. Prompt de Ativação Proativa
Inclua um prompt padrão para liberar o MCP para atuação autônoma:
```markdown
@orquestrador: @mcp: Atue proativamente sobre pendências registradas no manifesto. Priorize aquelas com checklist incompleto ou changelog ausente.
```


> Sempre que atualizar o manifesto, garanta que ele seja autossuficiente, reflita a identidade e os fluxos vigentes do laboratório, e seja compatível com o MCP (Microsoft Copilot).