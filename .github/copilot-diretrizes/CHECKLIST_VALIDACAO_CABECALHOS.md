# Checklist de Validação de Cabeçalhos Autossuficientes

**Objetivo:** Validar conformidade de cabeçalhos de prompts, issues e solicitações com a diretriz de autossuficiência do ScarecrowLab.

**Contexto:** Este checklist deve ser usado por agentes e humanos antes de submeter qualquer prompt formal, issue orquestrada ou solicitação que envolva comunicação entre agentes ou alteração de artefatos do laboratório.

**Referência:** [Diretrizes para Cabeçalhos Autossuficientes](./diretrizes_cabecalhos_autossuficientes.md)

---

## Checklist de Validação — Elementos Obrigatórios

- [ ] **1. Identificação Clara**
  - Remetente explicitamente declarado (ex: @orquestrador, @mcp, @ghc, @usuário)
  - Destinatário explicitamente declarado
  - Formato: `De: @<remetente> | Para: @<destinatário>`

- [ ] **2. Objetivo Explícito**
  - Ação ou resultado esperado descrito de forma clara e concisa
  - Sem ambiguidades sobre o que deve ser feito
  - Uma frase ou parágrafo breve, não mais que 2-3 linhas

- [ ] **3. Contexto Mínimo**
  - Motivação ou situação que originou a solicitação está presente
  - Informações essenciais para execução estão incluídas
  - Contexto suficiente para compreensão independente

- [ ] **4. Artefatos/Subprojetos Identificados**
  - Caminho ou nome dos arquivos impactados está listado
  - Subprojeto relacionado está identificado (se aplicável)
  - Links ou caminhos relativos são válidos e acessíveis

- [ ] **5. Critérios de Sucesso**
  - Condições de conclusão estão definidas
  - Critérios são verificáveis e mensuráveis
  - Formato checklist preferencial: `- [ ] Critério X`

- [ ] **6. Referência (Recomendado)**
  - Link para ata, debate, issue ou documento relacionado
  - Facilita rastreabilidade e auditoria
  - Opcional mas fortemente recomendado

---

## Teste de Independência

- [ ] **O cabeçalho pode ser compreendido sem acesso a:**
  - Histórico de conversas anteriores
  - Contexto externo não documentado
  - Conhecimento prévio não explicitado

- [ ] **Qualquer destinatário (novo agente, humano, auditor) consegue:**
  - Entender o que precisa ser feito
  - Identificar os artefatos envolvidos
  - Avaliar quando a tarefa está concluída
  - Rastrear origem e justificativa da solicitação

---

## Validação de Formato

- [ ] **Estrutura padronizada seguida:**
  ```markdown
  **De:** @<remetente>
  **Para:** @<destinatário>
  **Objetivo:** <descrição>
  **Contexto:** <resumo>
  **Artefato(s)/Subprojeto(s):** <lista>
  **Critérios de Sucesso:** <checklist>
  **Referência:** <link>
  ```

- [ ] **Markdown correto e legível**
- [ ] **Links funcionais e caminhos válidos**

---

## Exemplos de Validação

### ✅ Exemplo POSITIVO (Autossuficiente)

```markdown
**De:** @orquestrador
**Para:** @ghc

**Objetivo:** Adicionar campo "Data de última atualização" ao painel_subprojetos.md

**Contexto:**  
Identificada necessidade de rastrear temporalidade das atualizações em subprojetos para facilitar priorização e identificar itens obsoletos.

**Artefato(s)/Subprojeto(s):**  
- .github/painel_subprojetos.md
- Subprojeto: arcabouço_governanca

**Critérios de Sucesso:**  
- [x] Campo "Última Atualização" adicionado à tabela de subprojetos
- [x] Formato de data padronizado (YYYY-MM-DD)
- [x] Exemplo preenchido para ao menos 3 subprojetos
- [x] Changelog registrado

**Referência:** debates/ATA_PAINEL_CENTRAL_2025-10-10.md
```

**Validação:** ✅ Todos os elementos obrigatórios presentes, contexto claro, independente de histórico externo.

---

### ❌ Exemplo NEGATIVO (Não Autossuficiente)

```markdown
**Para:** @ghc

Atualiza o template que a gente discutiu.

Faz isso com urgência.
```

**Problemas identificados:**
- ❌ Remetente não declarado
- ❌ Objetivo vago ("o template que a gente discutiu")
- ❌ Sem contexto ou motivação
- ❌ Artefato não identificado
- ❌ Sem critérios de sucesso
- ❌ Sem referência
- ❌ Depende de histórico externo ("que a gente discutiu")

**Como corrigir:** Usar estrutura padronizada, identificar artefato específico, incluir contexto e critérios claros.

---

## Fluxo de Uso

1. **Antes de criar issue/prompt:**
   - Preencher estrutura de cabeçalho autossuficiente
   - Executar este checklist de validação

2. **Durante revisão:**
   - Verificar cada item do checklist
   - Corrigir lacunas identificadas
   - Validar independência (teste de leitura sem contexto prévio)

3. **Após aprovação:**
   - Submeter issue/prompt com cabeçalho validado
   - Marcar campo "Cabeçalho autossuficiente validado" nos templates

4. **Auditoria/Retrospectiva:**
   - Revisar prompts submetidos
   - Identificar padrões de não conformidade
   - Atualizar diretriz conforme necessário

---

## Integração com Outros Artefatos

Este checklist deve ser referenciado em:
- TEMPLATE_CONVERSA_IA.md
- ISSUE_TEMPLATE/orchestrated-issue.md
- protocolo_orquestracao_chat.md
- TEMPLATE_CHECKLIST.md
- TEMPLATE_PLANO_ACAO.md

---

## Observações

- Para comunicações informais ou iterações rápidas entre agentes conhecidos, pode-se usar versão simplificada mantendo elementos essenciais (objetivo, contexto, critérios)
- Agentes MCP/GHC devem sinalizar automaticamente prompts que falhem em 3+ itens do checklist
- Este checklist é vivo e deve ser atualizado conforme feedback de uso real

---

> **Status:** Ativo  
> **Responsável:** Persona Revisora de Mudanças Textuais  
> **Última atualização:** 2025-10-11  
> **Vínculo:** [Painel Central de Subprojetos](../painel_subprojetos.md) — Seção "Diretrizes Textuais"
