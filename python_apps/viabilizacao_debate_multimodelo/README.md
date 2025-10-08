# Viabilização de Debates Multimodelo com Copilot e Outros Agentes

## Contexto

Atualmente, debates entre modelos de IA (ex: open-source, APIs, Copilot) exigem copiar/colar manualmente o contexto para cada agente, especialmente para o Microsoft Copilot, que não expõe API pública para integração direta. Isso limita a automação e a fluidez dos debates.

## Objetivo

Permitir que múltiplos modelos de IA (incluindo Copilot) participem de rodadas de debate de forma automatizada ou semi-automatizada, reduzindo a necessidade de intervenção manual e tornando o fluxo mais eficiente e auditável.

## Motivação

- Reduzir o trabalho manual de copiar/colar contexto para cada agente.
- Tornar debates entre modelos mais ágeis, auditáveis e rastreáveis.
- Possibilitar integração futura com outros agentes e fluxos automatizados.

## Premissas e Limitações

- O Copilot não permite integração direta via API, mas pode ler e responder a arquivos Markdown no VS Code.
- Modelos open-source e APIs externas podem ser integrados via scripts, CLI ou automações.
- O fluxo deve ser compatível com a governança e templates de debate já definidos.

## Possíveis Abordagens

- Estruturar o README e arquivos de debate para que qualquer agente (incluindo Copilot) possa ler e responder, minimizando o trabalho manual.
- Desenvolver extensão/plugin para VS Code que automatize a coleta de contexto e publicação de respostas, facilitando a participação do Copilot e de outros modelos.
- Usar automações (scripts, bots, GitHub Actions) para atualizar arquivos de debate e notificar agentes externos.
- Explorar a criação de um painel web ou interface centralizada para debates multimodelo.

## Requisitos Iniciais

- Mapear limitações técnicas do Copilot e de outros modelos.
- Definir formato padrão de arquivos de debate e integração.
- Propor MVP para automação mínima do fluxo.
- Garantir rastreabilidade e versionamento das interações.

## Próximos Passos

- Detalhar MVP e fluxos possíveis.
- Levantar requisitos para extensão/plugin VS Code.
- Prototipar integração com pelo menos um modelo open-source e simular participação do Copilot via arquivos Markdown.
- Avaliar viabilidade de automação parcial para o Copilot.

---

> Este subprojeto está aberto para debate e evolução incremental. Use o template de rodadas de debate para propor pontos, ajustes e registrar decisões.
