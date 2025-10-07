
# Copilot Instructions

## 1. Objetivo e Contexto do Projeto
- O projeto está localizado em `d:\projetos`.
- Fase inicial: sem `README.md` ou código-fonte.
- Todas as pendências e próximos passos estão em `.github/PENDENCIAS.md`. **Só consulte este arquivo se ele for citado em instruções ou tarefas.**
- Tarefas iniciais incluem: conectar ao repositório remoto GitHub, autenticar o GitHub CLI, commit inicial, configurar CI e adicionar arquivos de configuração (veja `.github/PENDENCIAS.md` se citado).

## 2. Fluxo de Trabalho para Agentes de IA
- Use Git para versionamento. O repositório remoto será criado no GitHub conforme pendências.
- Sempre siga as convenções e regras abaixo ao gerar código, documentação ou automações.
- Sempre que uma ação exigir confirmação do usuário, considere uma reação positiva (👍) ou resposta afirmativa ("sim", "ok", etc.) como autorização explícita para prosseguir.
- Quando novos arquivos de configuração ou workflows forem adicionados (ex: `.editorconfig`, CI), documente o propósito e uso neste arquivo.

## 3. Convenções do Projeto
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

## 4. Prompt de Continuidade de Sessão
- Sempre gere um session resume prompt antes de encerrar uma interação e permitir uma nova pergunta do usuário. Este prompt deve resumir o objetivo inicial e todos os detalhes de contexto relevantes discutidos, para que o trabalho possa ser facilmente retomado caso a sessão seja invalidada ou interrompida.

## 5. Exemplos e Casos Especiais
> Se `.github/PENDENCIAS.md` for citado em instruções ou tarefas:
> - Consulte-o para as ações mais recentes.
> - Sempre atualize o arquivo ao concluir, adicionar ou remover pendências, ou quando solicitado explicitamente.
> - Para setup de repositório, autentique o GitHub CLI e execute os comandos necessários.
> - Para configuração de CI, adicione os arquivos necessários e documente aqui.

## 6. Manutenção das Diretrizes
- Atualize este arquivo conforme o projeto evoluir e novas convenções ou workflows forem estabelecidos.
