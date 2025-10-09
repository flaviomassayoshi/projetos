# Subprojeto: Automação da Geração do ManifestoMCP.md

## Objetivo
Automatizar a geração do arquivo `ManifestoMCP.md` sempre que o template `.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md` for atualizado, garantindo rastreabilidade, governança e eliminação de erros manuais.

## Justificativa
- Garante que o manifesto consolidado esteja sempre alinhado ao template e ao arcabouço.
- Elimina risco de edição manual e resíduos de versões antigas.
- Facilita governança, rastreabilidade e manutenção do laboratório.

## Escopo
- Workflow automatizado (ex: GitHub Actions) para regeneração do manifesto.
- Script de extração/conversão do template para o manifesto final.
- Documentação do fluxo e exemplos de uso.

## Estrutura Inicial
- `README.md` (este arquivo)
- `workflow_geracao_manifesto.yml` (exemplo de workflow)
- `gerar_manifesto.py` (script de geração)
- `CHECKLIST.md` (checklist de entrega e validação)

## Critérios de sucesso
- Manifesto sempre atualizado automaticamente após alteração do template.
- Processo rastreável, auditável e documentado.
- Facilidade de manutenção e extensão futura.

---

> Consulte o checklist e os exemplos para detalhes do fluxo.
