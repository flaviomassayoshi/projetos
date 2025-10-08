# Mapeamento de Conteúdo Detalhado — Modularização das Diretrizes Copilot

**Objetivo:** Listar todos os blocos de conteúdo do arquivo principal que devem ser movidos para anexos, indicando o anexo de destino sugerido.


## Blocos a modularizar (com destino e ação)

1. **Templates, roteiros e checklists detalhados**
	- Destino: `copilot-diretrizes/exemplos_casos_especiais.md` (ou criar novo anexo se o tema for muito específico).
	- Ação: Adicionar seção “Templates e Exemplos de Checklists” com exemplos práticos.

2. **Fluxo detalhado de encerramento de pendências, changelog e templates**
	- Destino: `copilot-diretrizes/exemplos_casos_especiais.md` (seção “Fluxos de Encerramento e Changelog”) ou criar `copilot-diretrizes/template_changelog.md` se o fluxo for extenso.
	- Ação: Incluir passo a passo, exemplos de changelog e template mínimo.

3. **Observações técnicas (execução de scripts, leitura de arquivos, troubleshooting)**
	- Destino: 
	  - Execução de scripts/venv: `copilot-diretrizes/diretrizes_execucao_venv_windows.md`
	  - Troubleshooting e leitura de arquivos: `copilot-diretrizes/diretrizes_tecnicas.md`
	- Ação: Garantir que cada caso especial citado no principal esteja detalhado no anexo correspondente.

4. **Fluxo de rodadas de debate, atas, tabelas de decisão**
	- Destino: `copilot-diretrizes/diretrizes_debate.md`
	- Ação: Consolidar todo o fluxo, exemplos de atas e tabelas de decisão.

5. **Convenções de código, docstrings, organização**
	- Destino: `copilot-diretrizes/convenções_codigo.md`
	- Ação: Garantir que exemplos e padrões estejam claros e completos.

6. **Glossário de termos (MCP, GHB, etc.)**
	- Destino: 
	  - Se breve, incluir em `copilot-diretrizes/exemplos_casos_especiais.md` (seção “Glossário”).
	  - Se extenso, criar `copilot-diretrizes/glossario.md` e referenciar nos demais anexos.
	- Ação: Adicionar/atualizar seção de glossário.

7. **Regras para projetos de terceiros, versionamento, separação de customizações**
	- Destino: `copilot-diretrizes/projetos_terceiros.md`
	- Ação: Garantir que todos os exemplos e fluxos estejam presentes.

> Após validar e complementar os anexos, atualizar o arquivo principal para referenciar apenas o essencial e o índice de anexos.
