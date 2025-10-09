# Arquivo obsoleto

Este arquivo foi mantido apenas para compatibilidade, mas não é mais utilizado no arcabouço do ScarecrowLab. O operador padrão é sempre o GPT-4.1.
[CONTEXT_SOURCES]
- .github/copilot-instructions.md (role: core) sha256:5942FFA462501E4284333727BFDE754AB0C6F0B98B478C23DE8E0768264E68AB
- default_agents.md (role: manifesto) sha256:D10543AFFABA3C78F1F20D18850A4533A36B38B42ACFBED92E5BEDEC6384CE69
- .github/AGENT_RULES.md (role: documentation) sha256:D11EDFE4998D5FD05D0B47190AEB483F007F69905F41E638490912954D1715B2
- .github/copilot-diretrizes/glossario.md (role: annex) sha256:B56120087C79D2766BC237E8268240F939B1280E67EBD9A8FEE6B276B1F46FFD
[/CONTEXT_SOURCES]

Preload guidance for multi-model agents (short):
- Prioritize the `copilot-instructions.md` and `default_agents.md` for operational decisions.
- If using a low-cost model (GPT-5 Mini), prefer summaries only; call higher-capacity models for policy conflicts.
- Validate source hashes against `.github/context_digest.json` before assuming stale content.

User constraints:
- Follow the user's latest explicit constraints (e.g., "do not read files") and respect system policies.

When resuming a session, include a 2–3 line "Prompt de Retomada" summarizing last action and next step.
