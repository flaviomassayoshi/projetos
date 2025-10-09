# Changelog — Manifest update (multi-model context)

- Data/hora: 2025-10-08T23:33:31Z
- Responsável: flaviomassayoshi (registro realizado via agente automatizado)
- Descrição:
  - Registrei e apliquei alterações de suporte a fluxo multi-modelo no manifesto consolidado `default_agents.md`.
  - Inclusão da seção "Índice de contexto para uso multi-modelo" em `default_agents.md`, documentando o uso de `.github/context_digest.json` e `.github/preload_prompt.md` para preload seletivo em modelos de baixa capacidade (ex.: GPT-5 Mini) e escalonamento para modelos maiores.
  - Criação dos artefatos auxiliares:
    - `.github/context_digest.json` (índice machine-readable com hashes das fontes canônicas)
    - `.github/preload_prompt.md` (bloco de preload sugerido para injeção em prompts)
    - `.github/tools/regenerate_context_digest.py` (script para regenerar o digest)
  - Substituição de `.github/AGENT_RULES.md` por um stub de compatibilidade apontando para o manifesto e o digest (redução do risco de drift).
  - Regeneração do digest e atualização do arquivo `.github/context_digest.json` com os hashes atuais.

- Arquivos impactados / criados:
  - modified: `default_agents.md` (adicionada seção Índice de contexto para uso multi-modelo)
  - added: `.github/context_digest.json`
  - added: `.github/preload_prompt.md`
  - added: `.github/tools/regenerate_context_digest.py`
  - added/modified: `.github/AGENT_RULES.md` (convertido em stub)

- Observações:
  - A comparação foi feita contra a versão do manifesto gerada pelo GPT‑4.1 (cópia temporária em `.git/tmp_default_agents_gpt4_1.md`). A diferença principal é a adição da seção do digest e instruções de workflow multi‑modelo; não houve remoção de conteúdo pré‑existente.
  - Embora o arcabouço oriente que atualizações do manifesto não exigem changelog formal, este registro foi criado por solicitação explícita para garantir rastreabilidade adicional e auditoria humana.

- Status final: concluído
- Link para checklist/ata: (não aplicável) — nenhum checklist específico foi salvo para esta alteração; recomenda-se abrir um checklist via `TEMPLATE_ATUALIZACAO_MANIFESTO.md` se persistência for desejada.
