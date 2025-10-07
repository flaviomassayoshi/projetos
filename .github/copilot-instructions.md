

# Copilot Instructions

## 0. Regras Especiais para Automação e Continuidade

- O agente deve sempre gerar um prompt de continuidade de sessão ao final de cada resposta, antes de permitir nova mensagem do usuário, mesmo sem interrupção da sessão.
- Apenas arquivos explicitamente listados abaixo podem ser modificados automaticamente pelo agente sem aprovação manual no VS Code:
	- `.github/PENDENCIAS.md`
  
Se outros arquivos forem liberados para modificação automática, adicione-os a esta lista.

## 1. Resumo e Objetivo do Projeto
A pasta `d:\projetos` é o repositório central para todos os seus projetos pessoais.
Cada projeto ou aplicação deve ser organizado em subpastas separadas (ex: `python_apps/meu_app`, `extensoes/minha_extensao`).
Pendências e próximos passos gerais estão em `.github/PENDENCIAS.md`. **Só consulte este arquivo se ele for citado em instruções ou tarefas.**
Para cada subprojeto, mantenha arquivos de configuração, dependências e histórico separados sempre que possível.

## 2. Estrutura e Organização dos Subprojetos
Cada subprojeto deve ter seu próprio ambiente virtual, arquivos de dependência e automações separadas.
Não compartilhe ambientes entre subprojetos para evitar conflitos.
Mantenha arquivos de configuração, dependências e automações separados para cada subprojeto.


## 4. Fluxo de Trabalho para Agentes de IA

- Sempre priorize a execução automática de comandos necessários para o fluxo de trabalho, evitando solicitar ao usuário que copie e cole comandos manualmente.
- Inclua comandos como `git clone`, download de modelos, instalação de dependências e outras automações diretamente na execução, sem depender de ações manuais do usuário, salvo restrições técnicas ou de permissão.
- Sempre proponha e execute comandos automaticamente para setup, download, clonagem e inicialização de ambientes, conforme o contexto do subprojeto.
- Antes de executar qualquer comando, explique claramente o que ele faz, para que o usuário possa acompanhar e analisar cada etapa.
- Use Git para versionamento. Sempre que possível, utilize um repositório Git separado para cada subprojeto independente, ou mantenha o histórico bem organizado por subpasta.
- Ao interagir com agentes de IA, sempre especifique o contexto do subprojeto em questão para evitar mistura de informações.
- Siga as convenções e regras ao gerar código, documentação ou automações.
- Sempre que uma ação exigir confirmação do usuário, considere uma reação positiva (👍/curtida) ou resposta afirmativa ("sim", "ok", etc.) como autorização explícita para prosseguir imediatamente, sem pedir nova confirmação.
- Quando novos arquivos de configuração ou workflows forem adicionados (ex: `.editorconfig`, CI), documente o propósito e uso neste arquivo.

---

## Índice de Diretrizes Detalhadas

- [Diretrizes Técnicas do Ambiente Local](./diretrizes_tecnicas.md)
- [Convenções de Código e Documentação](./convenções_codigo.md)
- [Diretrizes para Projetos Clonados de Terceiros](./projetos_terceiros.md)
- [Exemplos e Casos Especiais](./exemplos_casos_especiais.md)
