# Protocolo de Orquestração via Chat (MCP <-> GHC)

**Objetivo:** Consolidar as regras, papéis e templates para orquestração entre MCP e GHC exclusivamente via prompts de chat humano, conforme diretrizes do ScarecrowLab.

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

## Protocolo de Prompt entre Modelos (via chat)

**Toda comunicação entre modelos (MCP, GHC, outros) deve ser mediada por chat humano/orquestrador. Não utilizar comandos de arquivo como `@copilot: ler arquivo.md` em produção.**

### Template de Prompt para Orquestração Chat
```
@<destinatário>: <ação ou instrução clara>

Contexto:
- (Resumo do objetivo, arquivos ou temas envolvidos)

Tarefas:
1. (Descrever cada etapa de forma objetiva)
2. ...

Critérios de sucesso:
- (Critérios claros para considerar a tarefa concluída)

Referência: (opcional, cite conversa, ata ou arquivo relevante)
```

### Exemplo prático
```
@ghc: Atualizar o manifesto do ScarecrowLab conforme instruções abaixo:

Contexto:
- Revisão do protocolo de orquestração para garantir alinhamento com fluxo real de chat.

Tarefas:
1. Criar seção “Protocolo de Orquestração via Chat” explicando o papel do orquestrador entre MCP e GHC.
2. Incluir instruções sobre como o MCP opera com base no conteúdo da page, enquanto o GHC atualiza o manifesto via prompts recebidos por chat.
3. Adicionar templates auxiliares ao arcabouço:
   - Template de prompt para GHC
   - Template de conversa simulada entre agentes (otimizada para chat)
   - Template de plano de ação para atualizações do manifesto
4. Registrar changelog da implementação com data, responsável e link para os templates.

Critérios de sucesso:
- Seção criada e visível no manifesto
- Templates disponíveis para uso
- Changelog registrado

Referência: conversa entre MCP e Orquestrador em <data>.
```

### Observações
- O fluxo real de orquestração é sempre mediado por chat humano, nunca por comandos de arquivo.
- Exemplos e templates devem refletir esse fluxo, evitando ambiguidades.
