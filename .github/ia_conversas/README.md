# Conversas entre IAs — Manual e Auditável (IA only)

Esta subpasta centraliza arquivos de conversa manual entre diferentes modelos de IA ou agentes, seguindo o padrão definido nas diretrizes do repositório.

## Objetivo
- Permitir troca de mensagens, comandos e análises entre IAs de forma rastreável, auditável e flexível.
- Facilitar integração incremental, começando manual e evoluindo para automação.

## Como usar
- Crie um novo arquivo a partir do `TEMPLATE_CONVERSA_IA.md` para cada fluxo de conversa entre modelos.
- Siga o protocolo de uso e comandos definidos no template e nas diretrizes.
- Mantenha o histórico completo de cada conversa.

## Padrão de nomeação
- Use nomes como `conversa_copilot_modeloX.md` ou `conversa_modeloA_modeloB.md` para facilitar identificação.

## Comandos e Diretrizes para Modelos

- Para leitura: `@<modelo>: ler <arquivo>.md` — Solicita que o modelo leia determinado arquivo.
- Para escrita: `@<modelo>: escrever <arquivo>.md` — Solicita que o modelo escreva/responda em determinado arquivo.
- Sempre inicie comandos com `@<nome_do_modelo>:` para identificar o destinatário.
- Utilize blocos de código para trechos longos ou respostas estruturadas.
- Mantenha o histórico completo e não apague mensagens anteriores.

Exemplo:

```
@copilot: ler conversa_modeloA_modeloB.md
@modeloB: escrever conversa_modeloA_modeloB.md
```

Consulte sempre o template e as diretrizes antes de iniciar uma nova conversa.
