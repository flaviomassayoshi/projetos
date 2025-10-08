

# Manifesto de Diretrizes — ScarecrowLab

> Para propor revisões ou atualizações deste manifesto, utilize o template: `TEMPLATE_ATUALIZACAO_MANIFESTO.md`.

---

## Objetivo do Manifesto

Este manifesto tem como objetivo principal permitir e facilitar a colaboração do aplicativo Copilot no ecossistema do ScarecrowLab. Ele define os protocolos, templates e práticas que garantem que agentes de IA — especialmente o Copilot (GHB e MCP) — possam atuar de forma integrada, disciplinada e rastreável dentro dos fluxos operacionais do laboratório.

Toda atualização deste manifesto será feita diretamente nesta página, com o intuito de aprimorar continuamente o entendimento e a eficiência da colaboração entre agentes.

---

## Fluxograma Operacional (Ciclo de uma Pendência)

```markdown
┌──────────────┐
│ Plano de Ação│
└──────┬───────┘
	│
	▼
┌──────────────┐
│ Checklist    │
└──────┬───────┘
	│
	▼
┌──────────────┐
│ Execução     │
└──────┬───────┘
	│
	▼
┌──────────────┐
│ Checklist de │
│ Entrega      │
└──────┬───────┘
	│
	▼
┌──────────────┐
│ Changelog    │
└──────┬───────┘
	│
	▼
┌──────────────┐
│ Encerramento │
└──────────────┘
```

---

O ScarecrowLab é um laboratório de integração, automação e governança de agentes de IA, orientado por modularização, rastreabilidade e transparência. Toda a estrutura, comandos e templates são pensados para que novas IAs entendam rapidamente o contexto, as regras e possam colaborar de forma auditável e evolutiva.

---


## Princípios Centrais

- **Modularização:** Cada nova proposta ou solução é registrada como subprojeto do ScarecrowLab, com pastas, checklists e documentação próprios.
- **Rastreabilidade:** Toda decisão, tarefa ou debate é registrada em atas, changelogs e checklists versionados.
- **Automação e Disciplina:** Checklists, changelogs e templates padronizados garantem que nada fique sem controle ou registro.
- **Integração entre IAs:** Comunicação entre agentes é feita via arquivos Markdown, seguindo protocolo documentado e templates específicos.

---


## Como Funciona

1. **Subprojetos:** Cada iniciativa do ScarecrowLab tem sua própria pasta, README, checklist e changelog. Exemplo: `python_apps/integracao_mcp_markdown/`.
2. **Checklists:** Toda tarefa segue um checklist, que deve ser marcado etapa a etapa. Templates e exemplos estão abaixo.
3. **Changelog:** Encerramento de temas/checklists é sempre registrado, com data, responsável, status e link para o checklist/ata.
4. **Debates e Atas:** Discussões entre IAs seguem fluxo padronizado, com registro em atas e tabelas de decisão.
5. **Comandos e Protocolos:** IAs usam comandos como `@copilot: ler arquivo.md` e `@modeloB: escrever arquivo.md` para interagir via Markdown.
6. **Templates:** Modelos para checklists, changelogs e conversas entre IAs estão incluídos neste manifesto.

---

## Comandos e Protocolos Entre IAs

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

---



## Templates Essenciais
### Template de Ata

```markdown
- Data:
- Participantes:
- Tema:
- Pontos discutidos:
- Decisões tomadas:
- Pendências abertas:
```

---

## Diretrizes para Versionamento de Arquivos Markdown

- Nomeie arquivos com o tema, data (YYYY-MM-DD) e tipo (ex: `ATA_debate_2025-10-08.md`).
- Use nomes sem espaços e com letras minúsculas, separando palavras por underline.
- Para revisões, utilize sufixos incrementais ou datas.
- Mantenha histórico de versões relevantes, evitando sobrescrever atas e changelogs.

---

## Exemplo de Conversa entre IAs

```markdown
@copilot: ler conversa_modeloA_modeloB.md
@modeloB: escrever conversa_modeloA_modeloB.md

// Conversa simulada:

@copilot: modeloB, por favor, revise o checklist do subprojeto X.
@modeloB: Checklist revisado. Sugiro adicionar uma etapa para validação de ambiente.
@copilot: Sugestão aceita. Checklist atualizado.
```

---

### Template de Plano de Ação
Consulte: `TEMPLATE_PLANO_ACAO.md` — Modelo para registro de planos de ação, etapas e critérios de sucesso.

### Template de Checklist de Entrega
Consulte: `TEMPLATE_CHECKLIST_ENTREGA.md` — Modelo para controle e rastreabilidade de entregas vinculadas a planos de ação.

### Template de Checklist

**Objetivo:** (Descreva o objetivo do checklist, contexto e motivação.)

## Instruções de Execução
- (Liste orientações, pré-requisitos, alertas ou boas práticas para execução do checklist por agentes)

## Etapas
- [ ] (Descreva a etapa/tarefa de forma objetiva)
- [ ]
- [ ]

## Links Relacionados
- (Adicione links para atas, debates, documentação técnica, changelog, etc.)

> Use este template para criar novos checklists em subprojetos ou processos do repositório. Separe claramente etapas (ações) das instruções de execução. O status deve ser controlado por etapa.

### Exemplo Prático de Checklist
```
- [ ] Validar ambiente virtual
- [ ] Executar testes automatizados
- [ ] Atualizar changelog
```

### Template de Changelog
- Data/hora:
- Responsável:
- Descrição:
- Status final:
- Link para checklist/ata:

> Utilize este template para cada fechamento de tema/checklist. Adapte conforme a necessidade do subprojeto.

---

## Glossário Essencial

- **Ata**: Registro formal e rastreável de decisões, debates ou reuniões, contendo data, participantes, pontos discutidos e decisões tomadas.
- **Changelog**: Documento que registra o histórico de alterações, encerramentos de pendências e decisões relevantes, com data, responsável e status.
- **Checklist de entrega**: Lista temporária de etapas executadas em uma interação, usada para garantir que todos os itens do plano de ação foram cumpridos antes da resposta final.
- **Checklist temporário**: Lista de etapas ou tarefas criada para controle de uma interação ou entrega pontual, não rastreada como documento formal do projeto.
- **GHB**: GitHub Copilot (Copilot tradicional, integrado ao GitHub e editores de código)
- **Interação**: Todo o fluxo de execução do Copilot para uma resposta, iniciando quando o agente começa a processar a solicitação do usuário e encerrando ao concluir a resposta completa.
- **MCP**: Microsoft Copilot (Copilot integrado ao VS Code, Windows, Microsoft 365, etc.)
- **Pendência**: Tarefa, requisito ou decisão ainda não concluída, podendo ser geral do projeto ou específica de um subprojeto/checklist.
- **Plano de ação**: Sequência estruturada de etapas ou tarefas previstas para atingir um objetivo específico, apresentada antes da execução de uma demanda.
- **Prompt de retomada**: Mensagem gerada ao final de uma etapa ou checklist, contendo contexto resumido, status atual e próximos passos sugeridos para continuidade do fluxo.
- **Tema**: Assunto central de uma pendência, debate, checklist ou subprojeto, utilizado para organização e rastreabilidade.

---



## Como Agentes de IA Atuam no ScarecrowLab

- Sempre iniciam com um plano de ação e checklist de entrega.
- Marcam cada etapa concluída nos checklists.
- Atualizam changelogs e removem pendências encerradas do índice central.
- Seguem rigorosamente os templates e fluxos definidos.
- Toda comunicação, decisão e automação é registrada para garantir rastreabilidade e transparência.
- O MCP (Microsoft Copilot) e o GHB (GitHub Copilot) devem seguir as mesmas diretrizes, garantindo interoperabilidade e rastreabilidade entre plataformas.

---


## Resumo

O ScarecrowLab é um laboratório de integração e governança de IAs, com foco em modularidade, rastreabilidade e automação. Toda colaboração é documentada, auditável e orientada por templates e comandos claros, facilitando a entrada de novas IAs e agentes humanos.

Pronto para ser usado como Copilot Page ou referência para qualquer agente que deseje entender e atuar neste ecossistema.
