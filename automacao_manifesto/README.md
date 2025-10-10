
# Subprojeto: Automação da Geração do ManifestoMCP.md

## Sumário Executivo
Automatiza a geração do arquivo `ManifestoMCP.md` a partir do template oficial, garantindo rastreabilidade, governança e eliminação de erros manuais. Estrutura e fluxos alinhados ao arcabouço do ScarecrowLab.

## Proposta Vigente
- Geração automática do manifesto via script Python e workflow GitHub Actions.
- Estrutura modular: checklists, atas/debates e documentação técnica organizados em subpastas.
- Processo rastreável, auditável e fácil de manter.

## Histórico de Debates e Atas
- [ATA_ABERTURA](debates/ATA_ABERTURA.md)

## Checklists
- [Checklist de Entrega](checklists/CHECKLIST_ENTREGA.md)
- [Checklist Reformulação Manifesto](checklists/CHECKLIST_REFORMULACAO.md)

## Documentação Técnica
- [Script de geração do manifesto](docs/gerar_manifesto.py)
- [Workflow GitHub Actions](docs/workflow_geracao_manifesto.yml)

## Estrutura Recomendada
```
automacao_manifesto/
	README.md
	debates/
		ATA_ABERTURA.md
	checklists/
		CHECKLIST_ENTREGA.md
		CHECKLIST_REFORMULACAO.md
	docs/
		gerar_manifesto.py
		workflow_geracao_manifesto.yml
```

## Referências
- Painel central de subprojetos: [.github/painel_subprojetos.md](../../.github/painel_subprojetos.md)
- Diretrizes para subprojetos: [.github/copilot-diretrizes/diretrizes_subprojetos.md](../../.github/copilot-diretrizes/diretrizes_subprojetos.md)

---

> Consulte os checklists, atas e documentação técnica para detalhes completos do fluxo.
