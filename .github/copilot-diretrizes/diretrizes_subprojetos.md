# Diretrizes para Novos Subprojetos e Tratamento de Propostas

Este anexo consolida as regras e procedimentos para criação, organização e evolução de subprojetos no repositório.

- Toda nova proposta, solução ou iniciativa deve ser registrada diretamente como um novo subprojeto, criando uma pasta dedicada no local apropriado (ex: `python_apps/`, `extensoes/`, etc.).
- Recomenda-se utilizar o arquivo `TEMPLATE_SUBPROJETO.md` como base para a estrutura inicial do subprojeto.
- O subprojeto pode começar apenas com README, checklists e documentação mínima, evoluindo conforme a necessidade.
- Debates, atas, roteiros e histórico devem ser centralizados na estrutura do subprojeto desde o início, garantindo rastreabilidade completa.


---

## Template do Painel Central de Subprojetos

> Utilize este template para criar ou atualizar o painel central de subprojetos (`.github/painel_subprojetos.md`).

```markdown
# Painel Central de Subprojetos — ScarecrowLab

> Fonte única e oficial para status, pendências e checklists de todos os subprojetos. Deve ser referenciado por manifestos, templates e pelo MCP/GHC para validação, rastreabilidade e atuação proativa.

| Subprojeto                  | Status Geral   | Pendências Abertas | Itens de Checklist (detalhado)                                                                                                   | Responsável      | Última Atualização |
|----------------------------|----------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------|
| nome_subprojeto            | Em andamento   | 1                  | - Descrever item 1 (✔️)\n- Descrever item 2 (⏳)                                                                                 | responsávelX     | AAAA-MM-DD         |
| outro_subprojeto           | Concluído      | 0                  | - Checklist concluído (✔️)                                                                                                       | responsávelY     | AAAA-MM-DD         |

## Pendências Detalhadas

### nome_subprojeto
- Pendência: Descrever pendência
	- Contexto: Breve explicação
	- Critérios de sucesso: Critério objetivo

## Instruções
- Atualize este painel sempre que houver mudança de status, pendência ou checklist em qualquer subprojeto.
- O MCP/GHC deve consumir este painel para validação automática e geração de relatórios/status.
- Todos os templates e manifestos devem referenciar este painel como fonte única de subprojetos.
- Utilize os campos de links para facilitar navegação e rastreabilidade.
```

> Estrutura e campos podem ser expandidos conforme necessidade do laboratório.
