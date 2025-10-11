# Changelog — Template de Prompt Padrão

## [2025-10-11 02:45] Criação do TEMPLATE_PROMPT_PADRAO.md

**Responsável:** GitHub Copilot Agent (GHC)

**Descrição:**
- Criado novo template `TEMPLATE_PROMPT_PADRAO.md` para estruturação padronizada de prompts no ScarecrowLab
- Incluída instrução funcional `[gerar_guid]` para geração automática de identificadores únicos (GUID/UUID)
- Template alinhado aos princípios constitucionais do laboratório: rastreabilidade, governança e interoperabilidade

**Motivação:**
- Garantir rastreabilidade completa de prompts através de identificadores únicos
- Facilitar integração entre agentes MCP/GHC e persistência documental
- Compatibilizar com templates já consolidados (TEMPLATE_SUBPROJETO, TEMPLATE_PLANO_ACAO, TEMPLATE_ATUALIZACAO_MANIFESTO)

**Artefatos criados/atualizados:**
- `.github/TEMPLATE_PROMPT_PADRAO.md` (novo)
- `.github/copilot-instructions.md` (atualizada árvore de anexos e contextos de uso)
- `.github/copilot-diretrizes/templates_index.md` (adicionada referência ao novo template)
- `.github/changelog/2025-10-11_template_prompt_padrao.md` (este arquivo)

**Estrutura do template:**
- Identificação com instrução `[gerar_guid]`
- Dados do prompt (origem, destino, data/hora)
- Contexto e objetivo
- Lista de tarefas
- Artefatos envolvidos
- Subprojeto relacionado
- Critérios de sucesso
- Justificativa de persistência
- Links de referência
- Observações adicionais

**Integração com arcabouço:**
- Referenciado na árvore de anexos do `copilot-instructions.md`
- Incluído no índice de templates (`templates_index.md`)
- Compatível com protocolo de orquestração e template de conversa IA
- Alinhado aos MVPs de rastreabilidade, governança e autossuficiência

**Status final:** Concluído

**Referências:**
- Issue: "Inclusão de instrução [gerar_guid] no TEMPLATE_PROMPT_PADRAO.md para rastreabilidade"
- Template base: `.github/ia_conversas/TEMPLATE_CONVERSA_IA.md`
- Protocolo: `.github/copilot-diretrizes/protocolo_orquestracao_chat.md`
