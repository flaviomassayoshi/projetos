# Extensões e Comandos Customizados para o ScarecrowLab

## Objetivo
Desenvolver um sistema de @extensions e /commands customizados para ampliar, automatizar e facilitar a interação com os fluxos, artefatos e governança do ScarecrowLab em diferentes interfaces (chat, web, VS Code, bots).

## Motivação
Permitir que usuários e agentes interajam com o laboratório de forma mais ágil, padronizada e automatizada, integrando comandos e extensões a bots, editores e sistemas externos.

## Comandos Documentados

### #lab — Verificação de Contexto Persistente

**Objetivo:** Confirmar que o contexto do repositório e arcabouço está carregado e ativo na sessão atual.

**Sintaxe:** `#lab`

**Comportamento esperado:**
- Reconhecido por agentes/automação como validação rápida de contexto ativo
- Resposta padrão: "Entendido, contexto carregado!"
- Pode incluir informações adicionais como:
  - Confirmação de acesso ao arcabouço (copilot-instructions.md)
  - Status de carregamento dos templates
  - Referência ao painel central de subprojetos
  - Última atualização do manifesto MCP

**Casos de uso:**
- Teste rápido de persistência do contexto em conversas longas
- Validação de que o agente tem acesso às diretrizes do ScarecrowLab
- Checkpoint antes de executar tarefas complexas
- Verificação após reconexão ou início de nova sessão

**Exemplo de resposta:**
```
Entendido, contexto carregado!

✅ Arcabouço ScarecrowLab ativo
✅ Acesso a copilot-instructions.md e anexos
✅ Templates e glossário disponíveis
✅ Painel central de subprojetos acessível
📅 Manifesto MCP: última atualização disponível

Pronto para executar tarefas conforme as diretrizes do laboratório.
```

**Implementação:**
- Agentes automáticos devem reconhecer `#lab` como comando de verificação
- Humanos podem usar `#lab` para confirmar que o contexto está ativo
- IAs devem responder com confirmação padrão e informações complementares relevantes

---

## Escopo Inicial
- Definir sintaxe e arquitetura de comandos (/checklist, /ata, /aprovar, etc.)
- Implementar protótipo de parser e executor de comandos
- Integrar comandos a bots (Telegram, Discord) e/ou extensões VS Code
- Documentar exemplos e fluxos de uso

## Próximos Passos
1. Mapear comandos e extensões prioritários
2. Propor arquitetura e sintaxe
3. Implementar protótipo mínimo
4. Testar integração com artefatos do laboratório
5. Documentar resultados e roadmap

---

> Este subprojeto visa tornar o ScarecrowLab ainda mais interativo, modular e automatizado.
