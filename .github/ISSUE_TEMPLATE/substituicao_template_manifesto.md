> ⚠️ **Atenção:**
> Esta issue é um artefato de controle interno do laboratório (issue do lab). Não confunda com uma issue do GitHub, que é pública e registrada no repositório. Use este template para rastreabilidade, debates e fluxo interno. Quando migrar para o GitHub, registre o link e status correspondente abaixo.

---

## 🗂️ Rastreabilidade e Status

- **Status no lab:**
	- [ ] Aberto
	- [ ] Em andamento
	- [ ] Aguardando resposta
	- [ ] Concluído
	- [ ] Migrado para GitHub
- **Data de abertura:** <!-- preencha -->
- **Data de atualização:** <!-- preencha -->
- **Data de encerramento:** <!-- preencha -->
- **Responsável:** <!-- preencha -->
- **Referência cruzada (issue GitHub, se houver):** <!-- cole o link aqui -->

---
---
name: Solicitação de Substituição de Template do Manifesto
about: Solicite a substituição do TEMPLATE_ATUALIZACAO_MANIFESTO.md conforme padrão ScarecrowLab, prevendo integração com debates, personas e automação.
labels: manifesto, template, melhoria, debate, integração
---


## 📢 Solicitação de Substituição de Template – Atualização do Manifesto

### 👤 Personas Envolvidas
- [ ] MCP (Microsoft Copilot)
- [ ] GHC (GitHub Copilot)
- [ ] Orquestrador humano
- [ ] Outro (especifique):

### 🧾 Motivo da substituição
- O template atual está funcional, mas não segue integralmente o estilo, estrutura e rastreabilidade exigidos pela constituição.
- O novo modelo permite que o MCP opere com autossuficiência, seguindo fluxos encadeados e critérios de persistência.
- Compatível com geração automatizada via GitHub e agentes internos.

### 📂 Arquivo original
[.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md](https://github.com/flaviomassayoshi/ScarecrowLab/blob/master/.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md)

### 📌 Referência constitucional
Baseado nas diretrizes consolidadas em `.github/copilot-instructions.md` e nos artefatos de `.github/copilot-diretrizes/`.

### 🗣️ Histórico de Debates e Decisões
- (Registre aqui as interações, prompts, respostas e decisões relevantes para esta solicitação. Use blocos markdown para comandos, respostas de agentes e atas de debate.)

### ✅ Ação esperada
Substituir o template atual pelo modelo abaixo e registrar a alteração no changelog oficial.

# ---
````markdown name=TEMPLATE_ATUALIZACAO_MANIFESTO_PADRONIZADO.md
# 📜 TEMPLATE DE ATUALIZAÇÃO DO MANIFESTO — SCARECROWLAB

> Este template deve ser usado para gerar o arquivo `ManifestoMCP.md`, autossuficiente e compatível com o agente MCP.  
> O manifesto consolidado **não deve conter instruções operacionais**: foque em fluxos, exemplos, painéis e glossário.  
> Consulte também o arcabouço em `.github/copilot-diretrizes/`.

---

## 🧩 Dados da Atualização

### 🔗 Subprojetos Impactados *(obrigatório)*
Liste os subprojetos afetados, com nomes exatos conforme o painel central (`.github/painel_subprojetos.md`):

- subprojeto-1
- subprojeto-2
- extensoes/xyz

> O MCP/GHC deve validar diretamente no painel. Se algum subprojeto estiver ausente ou desatualizado, sinalizar pendência.

### 📈 Impacto Esperado *(opcional)*
Descreva brevemente os efeitos da atualização sobre fluxos, decisões ou automações.

---

## 🧱 Estrutura do Manifesto Consolidado

### 0. 📂 Sumário de Artefatos e Templates *(obrigatório)*
Liste os artefatos relevantes com resumo funcional minificado:

- `glossario.md`: Define termos e siglas essenciais.
- `protocolo_orquestracao_chat.md`: Fluxo de comunicação MCP ↔ GHC ↔ humano.
- `template_changelog.md`: Registro de encerramento de pendências.

### 1. 🎯 Objetivo do Manifesto
Explique o propósito do manifesto e seu público-alvo (MCP e humanos).

### 2. 🧠 Visão Geral do Lab
Descreva o propósito, identidade e contexto do ScarecrowLab.

### 3. 🧭 Princípios Centrais
Liste os pilares: modularização, rastreabilidade, automação, integração entre IAs.

### 4. 🔄 Fluxograma Operacional
Inclua diagrama (ASCII/Markdown) do ciclo de uma pendência: plano → execução → encerramento.

### 5. 🤖 Integração MCP
Explique que o manifesto é a fonte única para o MCP. Instruções claras para operação direta.

### 6. 🛠️ Como Funciona
Explique o uso de subprojetos, checklists, changelogs, comandos e templates.

### 7. 🗣️ Protocolo de Conversa Orquestrada
Referencie:
- `TEMPLATE_CONVERSA_IA.md`
- `protocolo_orquestracao_chat.md`

Oriente o MCP a usar esses artefatos como fonte de verdade.

### 8. 📋 Templates Essenciais (resumos)
Inclua apenas resumos sintéticos dos templates: checklist, changelog, ata, plano de ação.

### 9. 🗂️ Diretrizes de Versionamento
Oriente sobre nomeação, histórico e versionamento de arquivos Markdown.

### 10. 💬 Exemplo de Conversa Orquestrada
Simule uma interação MCP ↔ orquestrador humano.

### 11. 📚 Glossário Essencial
Defina termos usados nos fluxos do MCP.

### 12. 🧑‍💻 Atuação do MCP
Explique o comportamento esperado, registro de ações e rastreabilidade.

### 13. 🧾 Resumo Final
Consolide identidade, propósito e diferenciais do ScarecrowLab.

### 14. 🧪 Casos Reais ou Simulados
Inclua exemplos sintéticos de pendências reais ou fictícias.

### 15. ✅ Checklist com Status (resumido)
Exemplo sintético com status:
- [x] Revisar ata
- [x] Atualizar README
- [ ] Criar changelog

### 16. 🚀 Critérios para Ação Proativa do MCP
Defina quando o MCP pode agir sem comando explícito:
- Checklist incompleto
- Changelog ausente
- Ata sem plano vinculado

### 17. 🔓 Prompt de Ativação Proativa
```
@orquestrador:  
@mcp: Atue proativamente sobre pendências registradas no manifesto. Priorize aquelas com checklist incompleto ou changelog ausente.
```

### 18. 📦 Artefato Embutido no Prompt (opcional)
Explique como incluir conteúdo bruto (README, changelog, etc.) dentro de blocos markdown para análise direta pelo MCP.

---

🔚 **SEPARADOR FINAL DO MANIFESTO GERADO**  
--- FIM DO MANIFESTO GERADO ---

> Após este ponto, é permitido concatenar artefatos brutos para análise do MCP, sem confusão com o conteúdo oficial do manifesto.

---

### 🤖 Observações para integração futura
- Este template foi estruturado para ser compatível com a criação de issues no GitHub e automação por code agents.
- Campos de personas, histórico de debate e comandos facilitam a rastreabilidade e a participação de agentes em fluxos orquestrados.
