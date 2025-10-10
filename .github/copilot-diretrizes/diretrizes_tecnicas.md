# Diretriz: Execução de Comandos Shell — Contexto e Caminhos

Para garantir execução correta e evitar erros de contexto em automações, scripts e comandos shell:
- Sempre utilize caminhos absolutos ao referenciar arquivos e pastas em comandos shell.
- Sempre que possível, prefixe comandos shell com `cd <diretório>` para garantir o contexto correto de execução, especialmente em planos com múltiplas etapas ou diretórios distintos.
- Em fluxos automatizados, explicite o contexto de cada etapa e valide o diretório antes de executar comandos sensíveis.

Essas práticas reduzem riscos de conflitos, garantem rastreabilidade e evitam erros de execução fora do diretório esperado.

> Esta diretriz complementa as recomendações de automação e scripts do arcabouço, evitando redundância e otimizando a governança operacional.
# Diretrizes Técnicas do Ambiente Local

- GPU: NVIDIA RTX 4070, driver 576.52, CUDA 12.9 (usar builds PyTorch/xFormers para CUDA 12.1+)
- Python 3.10.11
- Ambiente virtual dedicado por subprojeto
- Instalar PyTorch CUDA 12.1: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
- xFormers: build compatível CUDA 12.x, Python 3.10
- Não misturar builds CPU-only e CUDA
- Só usar `--use-cpu all` se não houver GPU
- Se erro "Torch not compiled with CUDA enabled", revisar instalação
- Para troubleshooting: `nvidia-smi` para checar driver/GPU

## Arquitetura e Modularidade

- Recomenda-se fortemente o uso de arquitetura hexagonal (Ports and Adapters) ou, no mínimo, modularidade e separação clara entre núcleo de domínio e integrações externas.
- Cada subprojeto deve isolar regras de negócio do domínio central, mantendo interfaces/adapters para bancos, APIs, UI, automações, etc.
- Novas integrações devem ser implementadas como adapters, sem acoplamento direto ao núcleo.
- Essa abordagem facilita testes, manutenção, automação e evolução incremental, além de favorecer rastreabilidade e governança.

## Escolha de Modelos de IA

Objetivo: orientar a seleção de modelos de IA (ex.: GPT-5 Mini, GPT-5, GPT-4o, etc.) com base em custo, desempenho e adequação às tarefas do arcabouço.

Critérios práticos
- Custo e multiplicadores: valores como `0x`, `1x`, `3.33x` representam multiplicadores de custo/consumo de requisições. Priorize modelos `0x` para uso contínuo e reserve `1x` ou superiores para tarefas críticas.
- Complexidade da tarefa:
	- Simples / Rotina: documentação, validação de arquivos, automações básicas — use `0x` (ex.: GPT-5 Mini).
	- Moderada: geração de trechos de código, análises de impacto, revisões estruturais — `0x` normalmente suficiente; avaliar caso a caso.
	- Crítica / Complexa: geração de código avançado, análise profunda de arquitetura, decisões automatizadas com impacto — considere `1x` (GPT-5 completo) ou modelo premium.
- Latência e disponibilidade: prefira modelos menores quando a latência é sensível e reserve modelos maiores para jobs batch ou interações assíncronas.
- Privacidade e dados sensíveis: verifique políticas do provedor antes de enviar dados sensíveis; prefira processamento local/adapters isolados quando necessário.

Estratégia operacional
- Default: configurar agentes para usar um modelo `0x` por padrão (economia, disponibilidade).
- Escalonamento: permitir override manual/por política para `1x`/`3.33x` em tarefas explicitadas no plano de ação.
- Gatekeeping: exigir aprovação do orquestrador (Flavio ou responsável) para alterar modelo padrão em pipelines automatizados que consomem créditos.

Monitoramento e rastreabilidade
- Registrar no changelog ou no checklist de entrega quando uma tarefa usar modelos `1x`+; incluir data, responsável, justificativa e custo estimado.
- Instrumentar telemetria (logs de uso por job/agente) para auditar consumo e detectar uso indevido de modelos premium.

Transferência de contexto entre agentes
- Ao alternar agentes (ex.: MCP -> GHC), incluir resumo (2–5 linhas) com estado atual e próximo passo para preservar contexto. Não assumir que o novo agente herdará automaticamente o histórico.

Exemplo de regra simples
- "Usar GPT-5 Mini (`0x`) para todas as tarefas de rotina. Para tarefas classificadas como 'Crítica', solicitar aprovação do orquestrador e registrar uso do GPT-5 (`1x`) no changelog." 

Observação: adaptar as recomendações acima conforme as políticas do provedor e o plano de assinatura (Pro, Enterprise, etc.).
