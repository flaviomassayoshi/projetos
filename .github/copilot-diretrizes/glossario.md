# Glossário de Termos — Copilot

**Objetivo:** Consolidar definições e siglas relevantes para agentes de IA no contexto do Copilot/ScarecrowLab.

- **#lab**: Comando de verificação rápida de contexto persistente. Usado por humanos e agentes para confirmar que o contexto do repositório e arcabouço ScarecrowLab está carregado e ativo na sessão atual. Resposta padrão: "Entendido, contexto carregado!" (ver detalhes em `extensoes_comandos_scarecrowlab/README.md`).
# Arcabouço: Conjunto estruturado de diretrizes, templates, anexos e regras que compõem a base normativa e operacional do ScarecrowLab. Inclui o arquivo central `copilot-instructions.md`, todos os anexos em `.github/copilot-diretrizes/` e documentos correlatos. É a única fonte da verdade para decisões, fluxos e padronizações do laboratório.

- **Artefato persistente**: Qualquer plano, checklist, changelog, README ou documento que deve ser salvo e referenciado para rastreabilidade futura, conforme critérios definidos nas diretrizes.
- **Artefato temporário**: Plano, checklist ou documento criado apenas para controle pontual, não arquivado formalmente.
- **Ata**: Registro formal e rastreável de decisões, debates ou reuniões, contendo data, participantes, pontos discutidos e decisões tomadas.
- **Changelog**: Documento que registra o histórico de alterações, encerramentos de pendências e decisões relevantes, com data, responsável e status. Não inclui atualizações do manifesto do projeto.
- **Checklist de entrega**: Lista de etapas executadas em uma interação, usada para garantir que todos os itens do plano de ação foram cumpridos antes da resposta final. No contexto do operador principal, o checklist de entrega é o protocolo operacional obrigatório: serve como lembrete e validação do fluxo correto a cada interação, devendo ser apresentado e preenchido ao final de toda execução relevante. Pode ser temporária (controle pontual) ou persistente (rastreabilidade futura).
- **Checklist de entrega persistente**: Checklist de entrega que, por decisão do agente, é salvo e referenciado para rastreabilidade futura.
- **Checklist de revisão modular**: Checklist específico para avaliar modularização, rastreabilidade e alinhamento estrutural do laboratório.
- **Checklist temporário**: Lista de etapas ou tarefas criada para controle de uma interação ou entrega pontual, não rastreada como documento formal do projeto.
- **Copilot Page**: Página de referência para agentes Copilot, consolidando diretrizes e contexto do laboratório.
- **Critérios de persistência**: Fatores (complexidade, múltiplos agentes, impacto, etc.) que orientam a decisão de tornar um artefato persistente.
- **Execução híbrida**: Modalidade de execução de demandas que combina automação (agentes de IA, bots, workflows) com intervenção humana, garantindo flexibilidade e governança. Comum em tarefas que requerem validação manual, decisões estratégicas ou expertise especializada ao longo do processo automatizado.
- **GHB**: GitHub Copilot (Copilot tradicional, integrado ao GitHub e editores de código)
- **Identidade ScarecrowLab**: Conjunto de elementos, padrões e práticas que caracterizam e diferenciam o laboratório, orientando padronização e documentação.
- **Interação**: Todo o fluxo de execução do Copilot para uma resposta, iniciando quando o agente começa a processar a solicitação do usuário e encerrando ao concluir a resposta completa, liberando o usuário para um novo prompt.
- **Manifesto de Diretrizes**: Documento consolidado que reúne, em formato único e autoexplicativo, todos os fluxos, templates, comandos, exemplos e instruções essenciais do laboratório. Serve como referência operacional para agentes (MCP, GHC, GPT, etc.), facilitando o consumo das diretrizes sem análise profunda de múltiplos arquivos. Não substitui o arcabouço original, que permanece como única fonte da verdade para decisões estratégicas e revisões profundas.
- **Artefato embutido no prompt**: Prática de incluir o conteúdo bruto de um artefato (README, checklist, changelog, etc.) diretamente no corpo do prompt, usando bloco markdown simples (três crases: ```), nunca aninhado. Essa padronização garante que o conteúdo seja facilmente copiável e selecionável, facilitando análise, extração e reutilização sem depender de arquivos externos. Sempre evitar blocos markdown dentro de outros blocos markdown.
- **MCP**: Microsoft Copilot (Copilot integrado ao VS Code, Windows, Microsoft 365, etc.)
- **Padronização de fluxos**: Adoção de templates, checklists e changelogs para garantir uniformidade e rastreabilidade.
- **Pendência**: Tarefa, requisito ou decisão ainda não concluída, podendo ser geral do projeto ou específica de um subprojeto/checklist.
- **Plano de ação**: Sequência estruturada de etapas ou tarefas previstas para atingir um objetivo específico, apresentada antes da execução de uma demanda. Pode ser temporário ou persistente.
- **Plano de ação persistente**: Plano de ação que, por decisão do agente, é salvo e referenciado para rastreabilidade futura.
- **Prompt de continuidade**: Mensagem gerada ao final de uma etapa, contendo contexto resumido, status e próximos passos sugeridos.
- **Prompt de retomada**: Mensagem gerada ao final de uma etapa ou checklist, contendo contexto resumido, status atual e próximos passos sugeridos para continuidade do fluxo.
- **Referenciamento de templates**: Prática de citar explicitamente os arquivos de template nos documentos e instruções do laboratório.
- **Template de checklist de entrega**: Modelo padronizado para controle e rastreabilidade de entregas vinculadas a planos de ação.
- **Template de plano de ação**: Modelo padronizado para registro de planos de ação, etapas e critérios de sucesso.
- **Tema**: Assunto central de uma pendência, debate, checklist ou subprojeto, utilizado para organização e rastreabilidade.

> Sempre que for editar este glossário, mantenha os termos em ordem alfabética e evite redundâncias, unificando definições semelhantes e garantindo clareza para todos os agentes.
