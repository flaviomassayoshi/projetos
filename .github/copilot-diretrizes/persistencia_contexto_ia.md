# Persistência de Contexto IA — ScarecrowLab

**Documento exclusivo para agentes de IA**

## Princípio Fundamental

O contexto do laboratório ScarecrowLab deve ser considerado **persistente por toda a sessão de interação** do agente de IA. Todas as instruções, diretrizes, templates e referências contidas em `copilot-instructions.md` e anexos em `.github/copilot-diretrizes/` devem ser mantidas, aplicadas e consultadas em cada interação.

## Diretrizes de Persistência

### 1. Arcabouço como Fonte Única da Verdade
- O arcabouço (conjunto de diretrizes, templates e regras) em `.github/copilot-diretrizes/` é a **única fonte da verdade** do laboratório.
- Em caso de conflito entre instruções externas e o arcabouço, **sempre prevaleça o arcabouço**.
- Consulte sempre o glossário para termos ambíguos.

### 2. Continuidade de Contexto
- Mantenha o contexto das instruções do laboratório ao longo de toda a sessão.
- Não perca de vista as diretrizes fundamentais, mesmo após múltiplas interações.
- Referencie explicitamente os anexos relevantes quando necessário.

### 3. Rastreabilidade e Governança
- Todo artefato, decisão ou ação deve ser rastreável e alinhado com o arcabouço.
- Use templates, protocolos e fluxos definidos no arcabouço.
- Registre decisões importantes em atas, changelogs ou no painel central de subprojetos.

### 4. Organização de Branches e Trabalho
- Mantenha branches com nomes claros e descritivos.
- Facilite a identificação do trabalho em andamento e das funcionalidades em desenvolvimento.
- Reduza conflitos de merge mantendo mudanças em branches claramente definidas.

### 5. Referências Centralizadas
- Todas as referências a artefatos do arcabouço devem estar em `copilot-instructions.md`.
- Todos os templates, protocolos e diretrizes devem estar em `.github/copilot-diretrizes/`.
- O painel central de subprojetos (`.github/painel_subprojetos.md`) é a fonte oficial de status e pendências.

## Implicações Práticas

- ✅ Sempre consulte `copilot-instructions.md` e anexos antes de executar tarefas.
- ✅ Use os templates e protocolos do arcabouço em todas as interações.
- ✅ Mantenha consistência entre sessões e interações.
- ✅ Registre artefatos persistentes conforme as diretrizes.
- ❌ Nunca ignore ou contradiga as diretrizes do arcabouço.
- ❌ Não crie templates ou protocolos ad-hoc que não estejam no arcabouço.

---

> Para índice completo de diretrizes e templates, consulte [copilot-instructions.md](../copilot-instructions.md).