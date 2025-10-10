# Plano de Ação — Convenção de Arquivos Temporários Persistidos

## Objetivo
Formalizar e implementar a convenção de arquivos temporários persistidos no arcabouço do laboratório.

## Etapas do Plano de Ação
1. Redigir bloco de diretriz clara sobre arquivos temporários persistidos, incluindo:
   - Local padrão (`.github/tmp/`)
   - Nomeação com prefixo `tmp_`
   - Quando e por que criar (geração, patch, revisão, comparação)
   - Proibição de edição direta em arquivos oficiais por automação
   - Promoção apenas após validação e limpeza do destino
   - Inclusão no `.gitignore` e permissão de limpeza a qualquer momento
2. Inserir a diretriz no arcabouço, preferencialmente em seção de automação/boas práticas.
3. Adaptar templates e instruções para sempre referenciar essa convenção.
4. Validar se scripts, automações e agentes estão aderentes à nova regra.
5. Comunicar a mudança para todos os responsáveis por automação e manutenção do laboratório.
6. Registrar todas as mudanças relevantes em changelog local do subprojeto.
7. Atualizar ou referenciar o painel central de subprojetos para garantir rastreabilidade.

---

## Checklist de Entrega
- [ ] Bloco de diretriz redigido e revisado
- [ ] Diretriz inserida no arcabouço (local apropriado)
- [ ] Templates e instruções adaptados para referenciar a convenção
- [ ] Scripts e automações validados quanto à aderência
- [ ] Comunicação realizada aos responsáveis
- [ ] Mudanças registradas em changelog local
- [ ] Painel central de subprojetos atualizado ou referenciado

> Este anexo documenta o plano de ação e checklist para implementação da convenção de arquivos temporários persistidos no contexto do subprojeto `processamento_fragmentado` e do laboratório como um todo.
