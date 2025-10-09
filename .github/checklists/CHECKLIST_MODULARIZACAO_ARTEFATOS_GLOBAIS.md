# Checklist — Modularização e Separação de Artefatos Globais (.github)

**Tema:** Modularização de templates, checklists, planos, changelogs e atas globais do laboratório
**Status:** Pendente de execução
**Data de criação:** 2025-10-09

## Itens do Checklist

- [ ] Levantar todos os artefatos globais existentes em `.github/` (templates, checklists, planos, changelogs, atas, etc.)
- [ ] Criar estrutura modularizada em `.github/`, com subpastas por tipo de artefato:
    - `.github/templates/`
    - `.github/checklists/`
    - `.github/planos/`
    - `.github/changelogs/`
    - `.github/atas/`
- [ ] Em cada subpasta, separar cada artefato em dois arquivos:
    - `*_markup.md`: apenas o formato exportável
    - `*_instrucoes.md`: apenas instruções, exemplos, critérios e contexto de uso
- [ ] Migrar conteúdos, garantindo que arquivos de markup não contenham instruções internas
- [ ] Atualizar referências, anexos e documentação para os novos caminhos
- [ ] Atualizar `.github/painel_subprojetos.md` com a nova estrutura
- [ ] Validar via script/agente que arquivos `*_markup.md` não contenham instruções, exemplos ou contexto textual
- [ ] Verificar impacto em fluxos existentes (CI, prompts, scripts)
- [ ] Registrar a mudança em changelog e painel central

- [ ] Atualizar o arcabouço (diretrizes, anexos, manifesto) com informações e exemplos sobre a nova estrutura modularizada dos artefatos globais

## Critérios de sucesso
- Estrutura modular criada e artefatos migrados corretamente
- Nenhum arquivo de markup contém instruções internas
- Referências e anexos atualizados
- Validação automatizada de markup puro implementada
- Atualização do painel central
- Verificação de impacto em fluxos existentes
- Mudança registrada para rastreabilidade

---

> Checklist persistente. Executar, revisar e marcar cada item conforme avanço do fluxo.
