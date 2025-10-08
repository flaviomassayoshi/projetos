
# Copilot Instructions

## 1. Objetivo e Organização Geral

- A pasta `d:\projetos` é o repositório central para todos os seus projetos pessoais.
- Cada projeto ou aplicação deve ser organizado em subpastas separadas (ex: `python_apps/meu_app`, `extensoes/minha_extensao`).
- Para cada subprojeto, mantenha arquivos de configuração, dependências e histórico separados sempre que possível.
- Pendências e próximos passos gerais estão em `.github/PENDENCIAS.md`. **Só consulte este arquivo se ele for citado em instruções ou tarefas.**

## 2. Estrutura dos Subprojetos e Ambientes

- Cada subprojeto deve ter seu próprio ambiente virtual, arquivos de dependência e automações separadas.
- Não compartilhe ambientes entre subprojetos para evitar conflitos.
- Mantenha arquivos de configuração, dependências e automações separados para cada subprojeto.

## 3. Automação, Controle de Pendências e Changelog

- O agente deve sempre gerar um prompt de continuidade de sessão ao final de cada resposta, antes de permitir nova mensagem do usuário, mesmo sem interrupção da sessão.
- Apenas arquivos explicitamente listados abaixo podem ser modificados automaticamente pelo agente sem aprovação manual no VS Code:
  - `.github/PENDENCIAS.md`
  
  Se outros arquivos forem liberados para modificação automática, adicione-os a esta lista.
- Sempre que uma nova atividade, tópico ou ajuste for solicitado pelo usuário, registre automaticamente a pendência em `.github/PENDENCIAS.md` para controle e histórico.
- Isso garante que nenhum item importante será esquecido, mesmo que o usuário não acompanhe manualmente.
- Sempre que um roteiro ou procedimento for registrado em `.github/PENDENCIAS.md` ou outro arquivo de controle, utilize o formato de checklist para garantir rastreabilidade, acompanhamento e conclusão clara de cada etapa.
- Checklist de entrega obrigatório:
  - Verificar se o prompt de retomada foi gerado e apresentado corretamente.
  - Atualizar o arquivo de pendências (`.github/PENDENCIAS.md`) com todas as novas atividades e tópicos relevantes, atualizando o status de cada item (pendente, em progresso, concluído).
  - Garantir que nenhuma alteração em projetos de terceiros (ex: stable diffusion) seja incluída no versionamento principal, exceto customizações próprias em pastas separadas.
  - Registrar automaticamente no changelog/histórico do projeto (em `.github/changelog/`, com data e hora) decisões importantes, aprendizados ou evoluções relevantes, sem aguardar confirmação manual do usuário. O registro deve ser feito em arquivos temáticos (ex: `stable_diffusion.md`, `infraestrutura.md`) conforme instruções detalhadas em `.github/changelog/README.md`, incluindo data, hora, descrição clara e organização por tema ou subprojeto.

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
