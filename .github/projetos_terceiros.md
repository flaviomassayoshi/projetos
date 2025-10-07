# Diretrizes para Projetos Clonados de Terceiros

- Não inicialize ou use Git dentro da pasta do projeto clonado, a menos que vá contribuir diretamente para o repositório original.
- Mantenha suas customizações, scripts e presets em pastas separadas dentro do projeto clonado (ex: `custom_scripts/`, `meus_presets/`) ou fora dele, em um repositório próprio.
- Utilize `.gitignore` para evitar versionar arquivos temporários, outputs ou customizações locais.
- Nunca faça `git add/commit/push` no repositório clonado do projeto original, exceto para contribuir via pull request.
- Para versionar suas customizações, prefira um repositório Git separado apenas para elas, mantendo o projeto clonado limpo e fácil de atualizar.

## Versionamento no repositório principal
- Ao atualizar o repositório principal, só adicione, commite e envie mudanças relacionadas a projetos próprios (pastas e arquivos de sua autoria).
- Não inclua alterações em projetos de terceiros (ex: stable diffusion) no versionamento principal, a menos que sejam customizações suas em pastas separadas.
