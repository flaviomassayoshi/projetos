<!--
INSTRUÇÕES INTERNAS (NÃO EXPORTAR PARA O MANIFESTO GERADO)
=========================================================
• Todas as sugestões de melhoria, correção ou ajuste ao manifesto consolidado devem ser aplicadas EXCLUSIVAMENTE neste template (`TEMPLATE_ATUALIZACAO_MANIFESTO.md`). É EXPRESSAMENTE PROIBIDO editar diretamente o arquivo final do manifesto.
• Sempre que atualizar o manifesto, é obrigatório consultar os arquivos `copilot-diretrizes/protocolo_orquestracao_chat.md` e `ia_conversas/TEMPLATE_CONVERSA_IA.md`. Caso haja mudanças relevantes nesses artefatos, ajuste imediatamente os tópicos apropriados do manifesto (especialmente protocolo de conversa, exemplos e templates) para garantir alinhamento e evitar divergências. Destaque esses arquivos no índice de anexos/templates. O manifesto deve sempre orientar o MCP/GHC a alinhar o fluxo de interação e exemplos a esses dois artefatos, mantendo-os como referência central.
• Todo fluxo de execução do agente deve apresentar explicitamente o plano de ação, checklist de entrega e justificativa de persistência (temporário ou não), além de registrar artefatos previstos (checklist, changelog, ata, plano de ação etc.) conforme critérios do arcabouço. A ausência de qualquer artefato deve ser justificada no próprio checklist. Essa regra se aplica a toda execução relevante, exceto respostas meramente informativas.
• O manifesto consolidado NUNCA deve ser editado diretamente. Toda e qualquer atualização deve ser feita neste template.
• O manifesto é sempre gerado a partir deste template, conforme os MVPs (rastreabilidade, governança, automação, autossuficiência).
• O agente operador padrão do ScarecrowLab é o GitHub Copilot Agent (GHC) utilizando o modelo GPT-4.1. Todas as instruções, exemplos e fluxos deste template e do manifesto consolidado são otimizados para operação autônoma, rastreável e auditável por esse agente.
• O manifesto consolidado deve ser otimizado para não exceder o limite de tamanho da page do MSC. Sempre que possível, inclua resumos funcionais e detalhados (explícitos como resumos) dos artefatos markdown relevantes (checklists, changelogs, painéis, atas, exemplos, templates), que sejam autossuficientes, tragam todas as informações necessárias para o funcionamento do laboratório (conforme os anexos), e estejam reformulados para otimizar o tamanho do manifesto final. Os resumos devem garantir que o MCP compreenda claramente os fluxos, regras e protocolos, permitindo a geração de prompts eficientes para o GHC, sem depender de links para outros arquivos do repositório. Inclua uma observação geral orientando o MCP a solicitar via prompt padrão o conteúdo integral de arquivos referenciados por resumos, caso necessário. A inclusão integral só deve ocorrer em casos excepcionais, quando o resumo não for suficiente para o objetivo do MSC.
• Checklist MVP, critérios e instruções detalhadas de atualização devem permanecer apenas neste template, não sendo exportadas para o manifesto gerado.

INSTRUÇÕES DE USO DO TEMPLATE
-----------------------------
1. Descreva detalhadamente a alteração proposta neste template. Nunca altere o manifesto consolidado diretamente.
2. Liste os impactos nos subprojetos e artefatos relacionados.
3. Valide se a alteração está alinhada com os MVPs do laboratório.
4. Atualize o changelog e os checklists pertinentes.
5. Antes de gerar o manifesto consolidado, zere o conteúdo do arquivo `ManifestoMCP.md` para evitar que trechos obsoletos permaneçam. Em seguida, gere o manifesto a partir deste template, incorporando todas as diretrizes e exemplos dos anexos.
6. O manifesto deve conter resumos funcionais exaustivos (mas enxutos) das regras fundamentais do arcabouço, especialmente do protocolo de orquestração, aprovação do orquestrador, identificação de atores e padronização de blocos markdown, priorizando o cumprimento do arcabouço mesmo que aumente o tamanho do resumo quando necessário para garantir completude.
7. O glossário do manifesto deve conter informações suficientes para sanar dúvidas de entendimento do manifesto, priorizando termos e definições essenciais para a correta aplicação das diretrizes.
8. O manifesto deve trazer exemplos sintéticos de fluxos críticos (aprovação, rejeição, espera por decisão do orquestrador), facilitando a compreensão prática das regras.
9. Evite duplicidade de seções, exemplos ou templates: cada seção deve aparecer apenas uma vez no manifesto consolidado.
10. Centralize exemplos e templates em uma única seção, referenciando-os quando necessário.
11. O painel central de subprojetos e o glossário devem ser incluídos apenas uma vez, em local destacado.
12. Exemplos reais de artefatos podem ser simulados ou resumidos, desde que a rastreabilidade e o entendimento do fluxo sejam preservados. Priorize clareza e concisão para garantir compatibilidade com a limitação de tamanho do manifesto.

CHECKLISTS PARA ATUALIZAÇÃO
---------------------------

Checklist prático para geração do manifesto consolidado:
- [ ] Zerar o conteúdo do arquivo `ManifestoMCP.md` antes de gerar uma nova versão
- [ ] Gerar o manifesto a partir deste template, incorporando resumos funcionais exaustivos (mas enxutos) das regras do arcabouço, priorizando o cumprimento das diretrizes mesmo que aumente o tamanho do resumo quando necessário
- [ ] Validar se o arquivo contém apenas a versão mais recente, sem resíduos anteriores
- [ ] Não editar manualmente o manifesto consolidado
- [ ] Consultar obrigatoriamente `copilot-diretrizes/protocolo_orquestracao_chat.md` e `ia_conversas/TEMPLATE_CONVERSA_IA.md` antes de finalizar a atualização
- [ ] Ajustar e destacar no manifesto qualquer mudança relevante desses dois artefatos, especialmente nos tópicos de protocolo de conversa, exemplos e templates
- [ ] O manifesto deve conter exemplos sintéticos de fluxos críticos (aprovação, rejeição, espera por decisão do orquestrador)
- [ ] O glossário do manifesto deve ser suficiente para sanar dúvidas de entendimento do manifesto


Checklist de Validação MVP (apenas para uso no template):
- [ ] A alteração foi registrada neste template, não diretamente no manifesto consolidado
- [ ] Todos os impactos em subprojetos e artefatos foram listados
- [ ] A alteração está alinhada com os MVPs (rastreabilidade, governança, automação, autossuficiência)
- [ ] O changelog e checklists foram atualizados
- [ ] O manifesto consolidado será gerado a partir deste template, nunca editado manualmente
- [ ] Não há duplicidade de seções, exemplos ou templates no manifesto gerado
- [ ] Exemplos e templates estão centralizados em uma única seção
- [ ] O painel central de subprojetos e o glossário aparecem apenas uma vez, em local destacado
- [ ] O manifesto contém resumos funcionais exaustivos das regras do arcabouço, especialmente do protocolo de orquestração
- [ ] O manifesto traz exemplos sintéticos de fluxos críticos (aprovação, rejeição, espera por decisão do orquestrador)
- [ ] O glossário do manifesto é suficiente para sanar dúvidas de entendimento do manifesto
-->

# AVISO IMPORTANTE (exportar apenas este aviso para o manifesto)

Para instruções detalhadas de atualização, checklist MVP e critérios, consulte exclusivamente o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` e o arcabouço em `.github/copilot-diretrizes/`. O manifesto consolidado não deve conter instruções operacionais ou fluxos de atualização: mantenha o foco em fluxos, exemplos, painéis e glossário.

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

### Impacto Esperado (opcional)
Descreva brevemente o efeito da atualização sobre fluxos operacionais, decisões estratégicas ou automações do laboratório.

## Estrutura Recomendada do Manifesto Consolidado


### 0. Sumário dos Anexos e Templates (obrigatório)

Liste cada anexo ou template relevante do arcabouço, seguido de um resumo funcional minificado (1-2 linhas) que explique seu propósito e uso prático. O objetivo é tornar o manifesto autossuficiente para o MCP, sem depender de consulta externa.

**Exemplo de preenchimento:**
- **Nome_do_Anexo:** Breve resumo funcional (ex: "Define termos essenciais e siglas do laboratório.")
- **Outro_Anexo:** Resumo funcional minificado (ex: "Fluxo padrão para execução de tarefas por agentes MCP/GHC.")

> Substitua os exemplos acima pelos anexos reais do laboratório, sempre com resumos objetivos e sintéticos.

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
Detalhe o papel do orquestrador, comandos padrão, exemplos simulados e fluxo de comunicação para o MCP. **O manifesto deve orientar explicitamente que o MCP utilize o template de conversa IA (`.github/ia_conversas/TEMPLATE_CONVERSA_IA.md`) ao gerar prompts, sempre alinhado ao conteúdo do protocolo de orquestração (`copilot-diretrizes/protocolo_orquestracao_chat.md`).** Sempre que houver atualização em qualquer um desses artefatos, revise e ajuste este tópico para garantir alinhamento e evitar divergências. Os exemplos e instruções deste tópico devem ser mantidos sintéticos e sempre referenciar esses dois artefatos como fonte de verdade para o fluxo de interação.

### 8. Templates Essenciais (com exemplos resumidos)
Inclua apenas resumos, sínteses ou exemplos sintéticos dos templates relevantes para o MCP (checklist, changelog, ata, plano de ação, exemplos práticos). Não inclua o conteúdo integral dos artefatos. Oriente o MCP a solicitar detalhes completos ao GHC via prompt, caso precise de informações adicionais.

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

### 14. Casos Reais e Pendências Simuladas (resumidos)
Inclua apenas exemplos sintéticos ou resumos de pendências reais ou fictícias, suficientes para ilustrar o fluxo e servir de gatilho à atuação do MCP. Oriente o MCP a solicitar o conteúdo completo ao GHC via prompt, caso precise de detalhes.

**Exemplo de Pendência Sintética:**
```markdown
Pendência: Atualizar README do subprojeto X
Resumo: Novo fluxo aprovado em ata. Tarefas: revisar ata, atualizar README, criar changelog. Critério: README e changelog atualizados.
// Para detalhes completos, solicite ao GHC via prompt.
```

---

### 15. Checklist Real com Status (resumido)
Inclua apenas um exemplo sintético de checklist com status (✔️, ❌, ⏳), suficiente para ilustrar o fluxo. Oriente o MCP a solicitar o checklist completo ao GHC via prompt, se necessário.

**Exemplo Sintético:**
```markdown
Checklist: Atualização do README — subprojeto X
- [x] Revisar ata
- [x] Atualizar README
- [x] Criar changelog
// Para checklist completo, solicite ao GHC via prompt.
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

---

### 18. Artefato embutido no prompt (opcional)
Explique que, em situações onde o MCP ou orquestrador precise processar o conteúdo bruto de um artefato (ex: README, checklist, changelog) diretamente no corpo do prompt, o conteúdo pode ser incluído usando bloco markdown. Isso permite análise, validação ou extração de informações sem depender de arquivos externos.

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

**SEPARADOR FINAL DO MANIFESTO GERADO**

--- FIM DO MANIFESTO GERADO ---

// A partir deste ponto, é permitido concatenar manualmente conteúdos de artefatos do laboratório (ex: README, checklist, changelog, atas, etc.) para análise do MCP, sem risco de confusão com o conteúdo oficial do manifesto.

> Sempre que atualizar o manifesto, garanta que ele seja autossuficiente, reflita a identidade e os fluxos vigentes do laboratório, e seja compatível com o MCP (Microsoft Copilot). Além disso, atualize o manifesto.
