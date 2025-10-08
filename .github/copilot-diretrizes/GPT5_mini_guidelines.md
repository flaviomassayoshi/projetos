# Diretrizes e Templates — GPT-5 Mini (modelo `0x`)

Objetivo: fornecer orientação prática, checklists e templates otimizados para o uso consistente do GPT-5 Mini no arcabouço ScarecrowLab.

Instruções de uso (IA only)

- O GPT-5 Mini (`0x`) é o modelo preferencial para tarefas rotineiras e de baixa/mediana complexidade.
- Sempre estruture prompts com: 1) contexto resumido (2-4 linhas), 2) tarefa clara, 3) formato de resposta esperado.
- Para documentos longos, aplique chunking + resumos intermediários antes de pedir ações que envolvam o conteúdo completo.

Checklist rápido antes de invocar o Mini

- [ ] Resumo do contexto (2-4 linhas) incluído.
- [ ] Objetivo da tarefa explícito (ex.: "Gerar 3 sugestões", "Validar nomenclatura").
- [ ] Exemplo do formato de saída pedido.
- [ ] Dados sensíveis removidos ou tratados.
- [ ] Gatilho de escalonamento definido (se aplicável).

Templates otimizados

Template: Revisão Rápida de Documento
```
Contexto: {{resumo_2-3_linhas}}
Tarefa: Liste até 5 problemas de consistência (nomenclatura, estilo, links quebrados) e sugira correções curtas.
Formato: bullets numerados, cada item 1-2 linhas.
```

Template: Extração de Ações
```
Contexto: {{resumo_2-4_linhas}}
Tarefa: Extraia ações executáveis e agrupe por prioridade (alta, média, baixa). Limite a 10 ações.
Formato: tabela markdown com colunas: Ação | Prioridade | Responsável sugerido | Esforço estimado (S/M/L).
```

Template: Geração de Trecho de Código (baixa complexidade)
```
Contexto: {{resumo_2-3_linhas}}
Tarefa: Gere um trecho de código em {{linguagem}} que faça {{descrição_curta}}. Incluir comentários e 1-2 casos de teste simples.
Formato: bloco de código com comentários e seção "Casos de teste".
```

Práticas recomendadas de prompting

- Use instruções diretas e curtas.
- Prefira perguntas específicas em vez de "melhorar" sem critério.
- Se precisar de mais precisão, peça validação em 2 passos: geração + verificação/resumo.

Gatilhos de escalonamento (quando subir para 1x)

- Resultado do Mini falha em critérios de qualidade definidos.
- Tarefa classificada como "Crítica" no plano de ação.
- Necessidade de interpretação profunda de contexto com alto risco (jurídico, segurança, finanças).

Registro e telemetria

- Sempre registre: id do job, prompt hash, modelo usado (GPT-5 Mini), duração e tamanho da resposta.
- Se escalonar, registre motivo, quem autorizou e modelo destino.

Exemplos práticos

Exemplo 1 — Revisão de README
```
Contexto: README do subprojeto X (resumo: objetivo do subprojeto, comandos principais, dependências).
Tarefa: Identifique 5 pontos de melhoria para clareza e padronização de estilo. Sugira frases curtas.
Formato: bullets numerados, 1-2 linhas por sugestão.
```

Exemplo 2 — Validar checklist
```
Contexto: CHECKLIST.md do subprojeto Y (resumo: passos para validação automática).
Tarefa: Confirme se a ordem das etapas está consistente e sugira 3 melhorias de teste.
Formato: bullets numerados.
```

---

Arquivo gerado automaticamente para orientar uso do GPT-5 Mini no arcabouço. Ajuste templates conforme necessidade do time.