

# Copilot Instructions

## 1. Resumo e Objetivo do Projeto
- A pasta `d:\projetos` é o repositório central para todos os seus projetos pessoais.
- Cada projeto ou aplicação deve ser organizado em subpastas separadas (ex: `python_apps/meu_app`, `extensoes/minha_extensao`).
- Pendências e próximos passos gerais estão em `.github/PENDENCIAS.md`. **Só consulte este arquivo se ele for citado em instruções ou tarefas.**
- Para cada subprojeto, mantenha arquivos de configuração, dependências e histórico separados sempre que possível.

## 2. Estrutura e Organização dos Subprojetos
- Cada subprojeto deve ter seu próprio ambiente virtual, arquivos de dependência e automações separadas.
- Não compartilhe ambientes entre subprojetos para evitar conflitos.
- Mantenha arquivos de configuração, dependências e automações separados para cada subprojeto.

## 3. Fluxo de Trabalho para Agentes de IA
- Sempre priorize a execução automática de comandos necessários para o fluxo de trabalho, evitando solicitar ao usuário que copie e cole comandos manualmente.
- Inclua comandos como `git clone`, download de modelos, instalação de dependências e outras automações diretamente na execução, sem depender de ações manuais do usuário, salvo restrições técnicas ou de permissão.
- Sempre proponha e execute comandos automaticamente para setup, download, clonagem e inicialização de ambientes, conforme o contexto do subprojeto.
- Antes de executar qualquer comando, explique claramente o que ele faz, para que o usuário possa acompanhar e analisar cada etapa.
- Use Git para versionamento. Sempre que possível, utilize um repositório Git separado para cada subprojeto independente, ou mantenha o histórico bem organizado por subpasta.
- Ao interagir com agentes de IA, sempre especifique o contexto do subprojeto em questão para evitar mistura de informações.
- Siga as convenções e regras abaixo ao gerar código, documentação ou automações.
- Sempre que uma ação exigir confirmação do usuário, considere uma reação positiva (👍/curtida) ou resposta afirmativa ("sim", "ok", etc.) como autorização explícita para prosseguir imediatamente, sem pedir nova confirmação.
- Quando novos arquivos de configuração ou workflows forem adicionados (ex: `.editorconfig`, CI), documente o propósito e uso neste arquivo.

## 4. Convenções de Código e Documentação
- **Nomeação:**
  - Use `snake_case` para variáveis e funções
  - Use `PascalCase` para classes
- **Commits:**
  - Siga o padrão Conventional Commits para todas as mensagens de commit
- **Documentação:**
  - Todas as funções públicas devem ter docstrings ou comentários claros
- **Código:**
  - Escreva código claro, conciso e organizado
  - Adicione comentários quando necessário

## 5. Diretrizes para Projetos Clonados de Terceiros
Ao clonar projetos de terceiros (ex: interfaces gráficas, frameworks, exemplos):
- Não inicialize ou use Git dentro da pasta do projeto clonado, a menos que vá contribuir diretamente para o repositório original.
- Mantenha suas customizações, scripts e presets em pastas separadas dentro do projeto clonado (ex: `custom_scripts/`, `meus_presets/`) ou fora dele, em um repositório próprio.
- Utilize `.gitignore` para evitar versionar arquivos temporários, outputs ou customizações locais.
- Nunca faça `git add/commit/push` no repositório clonado do projeto original, exceto para contribuir via pull request.
- Para versionar suas customizações, prefira um repositório Git separado apenas para elas, mantendo o projeto clonado limpo e fácil de atualizar.

## 6. Prompt de Continuidade de Sessão
- Sempre gere um session resume prompt antes de encerrar uma interação e permitir uma nova pergunta do usuário. Este prompt deve resumir o objetivo inicial e todos os detalhes de contexto relevantes discutidos, para que o trabalho possa ser facilmente retomado caso a sessão seja invalidada ou interrompida.

## 7. Exemplos e Casos Especiais
> Se `.github/PENDENCIAS.md` for citado em instruções ou tarefas:
> - Consulte-o para as ações mais recentes.
> - Sempre atualize o arquivo ao concluir, adicionar ou remover pendências, ou quando solicitado explicitamente.
> - Para setup de repositório, autentique o GitHub CLI e execute os comandos necessários.
> - Para configuração de CI, adicione os arquivos necessários e documente aqui.
> Para cada subprojeto:
> - Especifique sempre o contexto do subprojeto ao interagir com agentes de IA ou configurar workflows.

## 8. Manutenção das Diretrizes
- Atualize este arquivo conforme o projeto evoluir e novas convenções ou workflows forem estabelecidos.
