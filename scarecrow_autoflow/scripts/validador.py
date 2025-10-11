#!/usr/bin/env python3
"""
Scarecrow AutoFlow — Validador

Script para validação de conformidade de issues e PRs com artefatos constitucionais.

Uso:
    python validador.py --type issue --number 123
    python validador.py --type pr --number 456

Regras detalhadas em: ../docs/REGRAS_VALIDACAO.md
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, List


class Validador:
    """Validador de conformidade com artefatos constitucionais."""

    def __init__(self, repo_path: str = None):
        """
        Inicializa o validador.

        Args:
            repo_path: Caminho do repositório (opcional)
        """
        self.repo_path = repo_path or os.getcwd()
        self.version = "1.0"

    def validar_issue(self, issue_data: Dict) -> Dict:
        """
        Valida uma issue.

        Args:
            issue_data: Dados da issue

        Returns:
            Dict com resultado da validação
        """
        validacoes = []

        # Validação 1: Título
        validacoes.append(self._validar_titulo(issue_data.get("title", "")))

        # Validação 2: Corpo
        validacoes.append(self._validar_corpo(issue_data.get("body", "")))

        # Validação 3: Labels
        validacoes.append(self._validar_labels(issue_data.get("labels", [])))

        # Calcular score
        score = self._calcular_score(validacoes)

        return self._create_result(validacoes, score)

    def validar_pr(self, pr_data: Dict) -> Dict:
        """
        Valida um pull request.

        Args:
            pr_data: Dados do PR

        Returns:
            Dict com resultado da validação
        """
        validacoes = []

        # Validação 1: Título
        validacoes.append(self._validar_titulo(pr_data.get("title", "")))

        # Validação 2: Descrição
        validacoes.append(self._validar_corpo(pr_data.get("body", "")))

        # Validação 3: Arquivos modificados
        validacoes.append(self._validar_arquivos(pr_data.get("files", [])))

        # Validação 4: Estrutura de subprojeto (se aplicável)
        if self._cria_subprojeto(pr_data.get("files", [])):
            validacoes.append(self._validar_estrutura_subprojeto(pr_data.get("files", [])))

        # Calcular score
        score = self._calcular_score(validacoes)

        return self._create_result(validacoes, score)

    def _validar_titulo(self, titulo: str) -> Dict:
        """Valida título."""
        if not titulo or len(titulo) < 10:
            return {
                "nome": "Título",
                "aprovado": False,
                "tipo": "crítica",
                "detalhes": "Título muito curto ou vazio",
            }

        if titulo.lower() in ["update", "fix", "change"]:
            return {
                "nome": "Título",
                "aprovado": False,
                "tipo": "importante",
                "detalhes": "Título muito genérico",
            }

        return {
            "nome": "Título",
            "aprovado": True,
            "tipo": "crítica",
            "detalhes": "Título adequado",
        }

    def _validar_corpo(self, corpo: str) -> Dict:
        """Valida corpo/descrição."""
        if not corpo or corpo.strip() in ["", "TODO"]:
            return {
                "nome": "Corpo",
                "aprovado": False,
                "tipo": "crítica",
                "detalhes": "Corpo vazio ou apenas TODO",
            }

        if len(corpo) < 50:
            return {
                "nome": "Corpo",
                "aprovado": False,
                "tipo": "importante",
                "detalhes": "Corpo muito curto (< 50 caracteres)",
            }

        return {
            "nome": "Corpo",
            "aprovado": True,
            "tipo": "importante",
            "detalhes": "Corpo adequado",
        }

    def _validar_labels(self, labels: List) -> Dict:
        """Valida labels."""
        if not labels:
            return {
                "nome": "Labels",
                "aprovado": False,
                "tipo": "opcional",
                "detalhes": "Nenhum label aplicado (recomendado pelo menos 1)",
            }

        return {
            "nome": "Labels",
            "aprovado": True,
            "tipo": "opcional",
            "detalhes": f"{len(labels)} label(s) aplicado(s)",
        }

    def _validar_arquivos(self, files: List) -> Dict:
        """Valida arquivos modificados."""
        if not files:
            return {
                "nome": "Arquivos",
                "aprovado": False,
                "tipo": "crítica",
                "detalhes": "Nenhum arquivo modificado",
            }

        # Verificar se modifica arquivos críticos
        critical_files = [
            ".github/copilot-instructions.md",
            "ManifestoMCP.md",
        ]
        for file in files:
            filename = file.get("filename", "")
            if any(critical in filename for critical in critical_files):
                return {
                    "nome": "Arquivos",
                    "aprovado": False,
                    "tipo": "crítica",
                    "detalhes": f"Modifica arquivo crítico: {filename}",
                }

        return {
            "nome": "Arquivos",
            "aprovado": True,
            "tipo": "importante",
            "detalhes": f"{len(files)} arquivo(s) modificado(s), nenhum crítico",
        }

    def _cria_subprojeto(self, files: List) -> bool:
        """Verifica se PR cria novo subprojeto."""
        # Simplificado: se cria README.md na raiz de diretório não existente
        for file in files:
            filename = file.get("filename", "")
            if filename.count("/") == 1 and filename.endswith("/README.md"):
                return True
        return False

    def _validar_estrutura_subprojeto(self, files: List) -> Dict:
        """Valida estrutura de novo subprojeto."""
        filenames = [f.get("filename", "") for f in files]

        # Verificar arquivos obrigatórios
        has_readme = any("README.md" in f for f in filenames)
        has_checklist = any("CHECKLIST.md" in f for f in filenames)

        if not has_readme or not has_checklist:
            return {
                "nome": "Estrutura de Subprojeto",
                "aprovado": False,
                "tipo": "crítica",
                "detalhes": "Subprojeto sem README.md ou CHECKLIST.md",
            }

        return {
            "nome": "Estrutura de Subprojeto",
            "aprovado": True,
            "tipo": "importante",
            "detalhes": "Estrutura básica de subprojeto presente",
        }

    def _calcular_score(self, validacoes: List[Dict]) -> int:
        """Calcula score de conformidade."""
        pesos = {
            "crítica": 10,
            "importante": 5,
            "opcional": 2,
        }

        total = 0
        pontos = 0

        for val in validacoes:
            tipo = val["tipo"]
            peso = pesos[tipo]
            total += peso
            if val["aprovado"]:
                pontos += peso

        if total == 0:
            return 100

        return int((pontos / total) * 100)

    def _create_result(self, validacoes: List[Dict], score: int) -> Dict:
        """Cria resultado estruturado da validação."""
        aprovado = score >= 90 and all(v["aprovado"] for v in validacoes if v["tipo"] == "crítica")

        return {
            "aprovado": aprovado,
            "score": score,
            "validacoes": validacoes,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": self.version,
        }


def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description="Validador AutoFlow")
    parser.add_argument("--type", choices=["issue", "pr"], required=True, help="Tipo: issue ou pr")
    parser.add_argument("--number", type=int, required=True, help="Número da issue/PR")
    parser.add_argument("--data", type=str, help="JSON com dados da issue/PR (opcional)")

    args = parser.parse_args()

    validador = Validador()

    # Se dados fornecidos via --data, usar diretamente
    if args.data:
        data = json.loads(args.data)
    else:
        # TODO: Buscar dados via GitHub API
        print("Erro: --data é obrigatório no MVP. Integração com GitHub API será implementada.", file=sys.stderr)
        sys.exit(1)

    # Validar
    if args.type == "issue":
        resultado = validador.validar_issue(data)
    else:
        resultado = validador.validar_pr(data)

    # Output JSON
    print(json.dumps(resultado, indent=2))


if __name__ == "__main__":
    main()
