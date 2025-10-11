

# Protocolo de Orquestração via Chat (MCP <-> GHC)

**REGRA FUNDAMENTAL:** Nenhuma recomendação, alteração ou ação sugerida pelo MCP deve ser implementada sem aprovação explícita do orquestrador humano. O agente destinatário (ex: GHC) deve, ao receber recomendações do MCP, solicitar aprovação do orquestrador antes de aplicar qualquer recomendação, mesmo após análise crítica.


**Objetivo:** Consolidar as regras, papéis e templates para orquestração entre MCP e GHC exclusivamente via prompts de chat humano, conforme diretrizes do ScarecrowLab.

**REFERÊNCIA OBRIGATÓRIA:** Todo registro de conversa orquestrada entre agentes (MCP, GHC, orquestrador) deve obrigatoriamente utilizar o template operacional `ia_conversas/TEMPLATE_CONVERSA_IA.md`. Sempre alinhe o fluxo e o conteúdo das interações a este protocolo e ao template. Em caso de atualização em qualquer um desses artefatos, revise ambos para garantir alinhamento e evitar divergências.

## Papéis e responsabilidades
- **Orquestrador (humano):** Coordena o ciclo, aprova prompts e confirma as atualizações finais.
- **MCP:** Opera com base no conteúdo visível da page; prepara prompts consolidados, sumários e exemplos práticos para o GHC; valida mudanças propostas em sandbox antes da solicitação formal ao GHC.
- **GHC:** Recebe prompts do MCP (via chat), aplica as alterações propostas no manifesto e no arcabouço, cria/atualiza templates e gera registros de changelog/ata conforme instruções.

## Fluxo resumido
1. MCP gera um prompt consolidado (com contexto mínimo e instruções claras) e envia ao GHC via chat.
2. GHC implementa as alterações propostas, registra rascunho de changelog e solicita revisão do orquestrador.
3. Orquestrador valida, solicita ajustes se necessário; após aprovação, GHC finaliza commit/PR e atualiza os registros de rastreabilidade.
4. O ciclo reinicia a cada atualização relevante.

## Regras operacionais (obrigatórias)
- Sempre usar `TEMPLATE_ATUALIZACAO_MANIFESTO.md` para alterações no manifesto principal.
- Exemplos reais dos templates devem estar no corpo das seções relevantes do manifesto (evitar links não-autocontidos sempre que possível).
- Para alterações que não sejam do manifesto, registrar changelog em `.github/changelog/<tema>.md` usando o template de changelog.
- Não confiar apenas no histórico Git como única fonte de pendências; manter checklists e atas nas pastas de subprojetos.
- Nenhuma recomendação, alteração ou ação sugerida pelo MCP deve ser implementada sem aprovação explícita do orquestrador humano. O agente destinatário deve sempre solicitar aprovação do orquestrador antes de aplicar qualquer recomendação do MCP.

## Protocolo de Prompt entre Modelos (via chat)


**Toda comunicação entre modelos (MCP, GHC, outros) deve ser mediada por chat humano/orquestrador. Não utilizar comandos de arquivo como `@copilot: ler arquivo.md` em produção.**

**Padronização de blocos markdown:**
Sempre que for necessário incluir artefatos (README, checklist, changelog, exemplos de prompt, etc.) em prompts, utilize blocos markdown simples (três crases: ```), nunca aninhados. Evite blocos markdown dentro de outros blocos markdown para garantir que o conteúdo seja facilmente copiável e selecionável. Priorize sempre resumos funcionais e exemplos sintéticos, facilitando a cópia integral do prompt.

### Template de Prompt para Orquestração Chat

**IMPORTANTE:** Todo prompt deve seguir a [Diretriz de Cabeçalhos Autossuficientes](./diretrizes_cabecalhos_autossuficientes.md). Use o [Checklist de Validação](./CHECKLIST_VALIDACAO_CABECALHOS.md) antes de submeter.

**Estrutura Padronizada:**

```markdown
**De:** @<remetente>  
**Para:** @<destinatário>

**Objetivo:** <Ação ou instrução clara>

**Contexto:**  
<Resumo do objetivo, motivação e situação>

**Artefato(s)/Subprojeto(s):**
- <Arquivos ou temas envolvidos>
- <Subprojeto relacionado>

**Tarefas:**
1. <Descrever cada etapa de forma objetiva>
2. ...

**Critérios de Sucesso:**
- [ ] <Critério 1>
- [ ] <Critério 2>

**Referência:** <Link para conversa, ata ou arquivo relevante>
```


### Exemplo prático
> Para exemplos detalhados de conversa orquestrada, utilize sempre o template operacional `ia_conversas/TEMPLATE_CONVERSA_IA.md`.


### Observações
- O fluxo real de orquestração é sempre mediado por chat humano, nunca por comandos de arquivo.
- Exemplos e templates devem refletir esse fluxo, evitando ambiguidades.

### Referências
- `ia_conversas/TEMPLATE_CONVERSA_IA.md` — Template operacional obrigatório para registro de conversas entre agentes.
- `TEMPLATE_ATUALIZACAO_MANIFESTO.md` — Template de atualização do manifesto consolidado.
