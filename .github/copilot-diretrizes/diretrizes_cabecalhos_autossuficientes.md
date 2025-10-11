# Diretrizes para Cabeçalhos de Prompt Autossuficientes

## Objetivo
Estabelecer padrão formal para cabeçalhos de prompts autossuficientes, garantindo que qualquer destinatário (persona, agente ou humano) compreenda a solicitação sem depender de histórico ou contexto externo, promovendo independência, auditabilidade e clareza nos fluxos documentais do ScarecrowLab.

## Motivação
A governança textual e rastreabilidade no laboratório dependem de comunicação clara e independente. Cabeçalhos autossuficientes eliminam ambiguidades, facilitam auditoria e permitem que agentes operem com contexto completo em cada interação, reduzindo erros e retrabalho.

## Definição de Cabeçalho Autossuficiente
Um cabeçalho de prompt é considerado **autossuficiente** quando contém:

1. **Identificação clara do remetente e destinatário**
   - Exemplo: `De: @orquestrador | Para: @ghc`

2. **Objetivo explícito da solicitação**
   - Resumo conciso da ação ou resultado esperado
   - Exemplo: "Atualizar template X com campo Y"

3. **Contexto mínimo necessário**
   - Motivação ou situação que originou a solicitação
   - Informações essenciais para execução
   - Exemplo: "Nova pendência identificada no subprojeto Z"

4. **Artefato(s) e/ou subprojeto(s) envolvido(s)**
   - Caminho ou identificação clara dos arquivos/componentes impactados
   - Exemplo: "Artefato: .github/TEMPLATE_CHECKLIST.md"

5. **Critérios de sucesso ou aceitação**
   - Condições claras para considerar a tarefa concluída
   - Exemplo: "Template atualizado, campo validado, changelog registrado"

6. **Referência opcional mas recomendada**
   - Link para ata, debate, issue ou documento relacionado
   - Exemplo: "Referência: debates/ATA_2025-10-11.md"

## Estrutura Padronizada

```markdown
### Cabeçalho do Prompt

**De:** @<remetente>  
**Para:** @<destinatário>  

**Objetivo:** <Descrição clara da ação esperada>

**Contexto:**  
<Resumo da situação, motivação ou dependências relevantes>

**Artefato(s)/Subprojeto(s):**  
- <Caminho ou nome do artefato>
- <Nome do subprojeto, se aplicável>

**Critérios de Sucesso:**  
- [ ] <Critério 1>
- [ ] <Critério 2>
- [ ] <Critério N>

**Referência:** <Link opcional para ata, issue, debate ou documento>
```

## Exemplos Práticos

### Exemplo 1: Atualização de Template
```markdown
### Cabeçalho do Prompt

**De:** @orquestrador  
**Para:** @ghc  

**Objetivo:** Adicionar campo "Cabeçalho autossuficiente validado" ao TEMPLATE_CHECKLIST.md

**Contexto:**  
Nova diretriz de governança textual exige que todos os prompts e checklists incluam validação de autossuficiência do cabeçalho para garantir rastreabilidade e clareza.

**Artefato(s)/Subprojeto(s):**  
- .github/TEMPLATE_CHECKLIST.md
- Arcabouço de governança textual

**Critérios de Sucesso:**  
- [x] Campo adicionado ao template
- [x] Exemplo de uso incluído
- [x] Changelog registrado

**Referência:** Issue #123 — Governança Textual
```

### Exemplo 2: Criação de Novo Artefato
```markdown
### Cabeçalho do Prompt

**De:** @mcp  
**Para:** @orquestrador  

**Objetivo:** Criar checklist de validação para cabeçalhos autossuficientes

**Contexto:**  
Para suportar a nova diretriz de cabeçalhos autossuficientes, é necessário um checklist que agentes possam usar para validar conformidade antes da submissão de prompts.

**Artefato(s)/Subprojeto(s):**  
- .github/copilot-diretrizes/CHECKLIST_VALIDACAO_CABECALHOS.md (novo)
- Subprojeto: arcabouço_governanca

**Critérios de Sucesso:**  
- [ ] Checklist criado com itens de validação
- [ ] Exemplos positivos e negativos incluídos
- [ ] Integrado ao painel central
- [ ] Referenciado em templates relevantes

**Referência:** debates/ATA_GOVERNANCA_TEXTUAL_2025-10-11.md
```

## Checklist de Validação de Cabeçalhos Autossuficientes

Use este checklist antes de submeter qualquer prompt, issue ou solicitação no ScarecrowLab:

- [ ] **Identificação clara:** Remetente e destinatário explicitamente declarados
- [ ] **Objetivo explícito:** Ação ou resultado esperado está claro e conciso
- [ ] **Contexto mínimo:** Motivação e situação estão descritas de forma suficiente
- [ ] **Artefatos identificados:** Arquivos, templates ou subprojetos impactados estão listados
- [ ] **Critérios de sucesso:** Condições de conclusão estão definidas e verificáveis
- [ ] **Referência presente:** Link para documento de origem ou contexto adicional (recomendado)
- [ ] **Independência validada:** Prompt pode ser compreendido sem acesso a histórico ou contexto externo

## Integração com Templates Existentes

Esta diretriz deve ser aplicada e referenciada nos seguintes templates e documentos:

1. **TEMPLATE_CONVERSA_IA.md**
   - Adicionar seção de validação de cabeçalho autossuficiente
   - Incluir checklist de validação

2. **ISSUE_TEMPLATE/orchestrated-issue.md**
   - Adicionar campo "Cabeçalho autossuficiente validado"
   - Referenciar esta diretriz

3. **protocolo_orquestracao_chat.md**
   - Referenciar diretriz de cabeçalhos autossuficientes
   - Atualizar template de prompt padrão

4. **TEMPLATE_CHECKLIST.md e TEMPLATE_CHECKLIST_ENTREGA.md**
   - Adicionar item de validação de cabeçalho

5. **TEMPLATE_PLANO_ACAO.md**
   - Incluir seção de cabeçalho autossuficiente

## Governança e Manutenção

**Responsável pela diretriz:** Persona Revisora de Mudanças Textuais (definida no arcabouço)

**Critérios de atualização:**
- Feedback de uso em cenários reais
- Identificação de lacunas ou ambiguidades
- Evolução do arcabouço de governança textual

**Processo de revisão:**
- Seguir fluxo definido em `fluxo_revisao_diretrizes.md`
- Registrar mudanças em changelog dedicado
- Validar com múltiplos agentes e cenários

## Observações Adicionais

- Esta diretriz é obrigatória para todos os prompts formais no ScarecrowLab
- Para comunicações informais ou iterações rápidas, pode-se usar versão simplificada mantendo elementos essenciais
- Agentes MCP/GHC devem sinalizar automaticamente prompts que não atendam aos critérios mínimos
- Validação automatizada pode ser implementada via scripts no futuro

## Referências
- [Protocolo de Orquestração via Chat](./protocolo_orquestracao_chat.md)
- [Template de Conversa IA](../ia_conversas/TEMPLATE_CONVERSA_IA.md)
- [Checklist de Comunicação](./checklist_comunicacao.md)
- [Manual de Redação MCP](./manual_redacao_mcp.md)
- [Painel Central de Subprojetos](../painel_subprojetos.md)

---

> Esta diretriz é parte integral do arcabouço de governança textual do ScarecrowLab. Consulte o painel central e o glossário para termos e definições complementares.
