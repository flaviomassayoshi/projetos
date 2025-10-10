
# Ativação Remota do GHC via Web

## Sumário Executivo
Este subprojeto visa viabilizar o uso do agente GHC fora da extensão do VSCode, com foco em navegadores mobile, soluções gratuitas e integração flexível com ferramentas de automação baseadas em terminal. A proposta evoluiu para considerar o uso combinado do gh-copilot (CLI Extension) e Copilot CLI, permitindo que bots (ex: Telegram) possam acionar comandos GitHub e sugestões de shell via linguagem natural, ampliando as possibilidades de automação remota e integração com o ecossistema Copilot.

## Proposta Vigente
- Explorar e validar a integração de bots e clientes web/mobile com o agente GHC utilizando gh-copilot e Copilot CLI como camada de automação e interface natural.
- Permitir que comandos e sugestões sejam processados via terminal, scripts ou aliases, simulando um pseudo agente, mesmo sem autonomia total do Copilot Agent.
- Documentar limitações, fluxos e recomendações para uso seguro e rastreável.

## Documento de Apoio
- [DOCUMENTO_APOIO_COPILOT_CLI_AGENT.md](./DOCUMENTO_APOIO_COPILOT_CLI_AGENT.md) — Relatório minificado comparando Copilot CLI, gh-copilot e Copilot Agent, com recomendações para integração e automação.

## Histórico de Debates e Atas
- [ ] Adicione links para arquivos de debate e atas conforme forem criados (ex: `debates/debate_2025-10-08_tema.md`)

## Checklists
- [ ] Adicione ou referencie checklists de setup, automação, entregas, etc.

## Documentação Técnica
- [ ] Detalhe requisitos, dependências, scripts, fluxos e integrações relevantes.

## Plano de ação
1. Definir escopo mínimo do cliente web (HTML/JS ou React)
2. Publicar cliente via GitHub Pages com layout responsivo
3. Criar backend serverless gratuito (Netlify Functions ou Firebase)
4. Configurar GitHub App com agente GHC vinculado
5. Implementar lógica de verificação do modelo ativo (multiplicador 0x)
6. Testar fallback manual via Copilot Web com artefato embutido
7. Validar integração com manifesto, templates e automação via gh-copilot/Copilot CLI
8. Registrar changelog e checklist de entrega

## Checklist de entrega
- [x] Cliente web publicado via GitHub Pages
- [ ] Backend funcional com função de envio de prompt
- [ ] GitHub App configurado com agente GHC ativo
- [ ] Verificação automática do modelo ativo implementada
- [ ] Fallback manual testado com artefato embutido
- [ ] Integração validada com manifesto, templates e automação CLI
- [ ] Changelog inicial registrado
- [ ] Ata de abertura registrada

## Critério de encerramento
O subprojeto será considerado concluído quando o agente GHC puder ser ativado remotamente via navegador mobile ou bot, com fallback funcional, integração validada com os artefatos do ScarecrowLab e automação via gh-copilot/Copilot CLI documentada.
