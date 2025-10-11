#!/usr/bin/env python3
"""
Scarecrow AutoFlow — Classificador

Script para classificação automática de issues e pull requests em:
- auto-merge: Aprovação automática imediata
- needs-simulation: Requer deliberação simulada entre personas
- manual-review: Requer revisão humana obrigatória

Uso:
    python classificador.py --type issue --number 123
    python classificador.py --type pr --number 456

Critérios detalhados em: ../docs/CRITERIOS_CLASSIFICACAO.md
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, Literal

CategoryType = Literal["auto-merge", "needs-simulation", "manual-review"]


class Classificador:
    """Classificador automático de issues e PRs."""

    def __init__(self, github_token: str = None):
        """
        Inicializa o classificador.

        Args:
            github_token: Token de autenticação do GitHub (opcional)
        """
        self.github_token = github_token or os.environ.get("GITHUB_TOKEN")
        self.version = "1.0"

    def classificar_issue(self, issue_data: Dict) -> Dict:
        """
        Classifica uma issue.

        Args:
            issue_data: Dados da issue (do GitHub API)

        Returns:
            Dict com categoria, score de confiança e justificativa
        """
        # Extrair metadados
        labels = [label["name"] for label in issue_data.get("labels", [])]
        body = issue_data.get("body", "")
        title = issue_data.get("title", "")
        size = len(body)

        # Verificar labels de override
        if "autoflow:auto-merge" in labels:
            return self._create_result("auto-merge", 100, "Override manual via label")
        if "autoflow:needs-simulation" in labels:
            return self._create_result("needs-simulation", 100, "Override manual via label")
        if "autoflow:manual-review" in labels:
            return self._create_result("manual-review", 100, "Override manual via label")
        if "autoflow:skip" in labels:
            return self._create_result("skip", 100, "Skip automação via label")

        # Regra 1: manual-review (prioridade máxima)
        if self._check_manual_review_issue(labels, body, size):
            return self._classify_manual_review_issue(labels, body, size)

        # Regra 2: auto-merge
        if self._check_auto_merge_issue(labels, body, size):
            return self._classify_auto_merge_issue(labels, body, size)

        # Regra 3: needs-simulation (padrão)
        return self._classify_needs_simulation_issue(labels, body, size)

    def classificar_pr(self, pr_data: Dict) -> Dict:
        """
        Classifica um pull request.

        Args:
            pr_data: Dados do PR (do GitHub API)

        Returns:
            Dict com categoria, score de confiança e justificativa
        """
        # Extrair metadados
        labels = [label["name"] for label in pr_data.get("labels", [])]
        files = pr_data.get("files", [])
        additions = pr_data.get("additions", 0)
        deletions = pr_data.get("deletions", 0)
        draft = pr_data.get("draft", False)

        # PRs em draft são skipped
        if draft:
            return self._create_result("skip", 100, "PR está em draft")

        # Verificar labels de override
        if "autoflow:auto-merge" in labels:
            return self._create_result("auto-merge", 100, "Override manual via label")
        if "autoflow:needs-simulation" in labels:
            return self._create_result("needs-simulation", 100, "Override manual via label")
        if "autoflow:manual-review" in labels:
            return self._create_result("manual-review", 100, "Override manual via label")
        if "autoflow:skip" in labels:
            return self._create_result("skip", 100, "Skip automação via label")

        # Regra 1: manual-review (prioridade máxima)
        if self._check_manual_review_pr(labels, files, additions + deletions):
            return self._classify_manual_review_pr(labels, files, additions + deletions)

        # Regra 2: auto-merge
        if self._check_auto_merge_pr(labels, files, additions + deletions):
            return self._classify_auto_merge_pr(labels, files, additions + deletions)

        # Regra 3: needs-simulation (padrão)
        return self._classify_needs_simulation_pr(labels, files, additions + deletions)

    def _check_manual_review_issue(self, labels: list, body: str, size: int) -> bool:
        """Verifica se issue deve ser manual-review."""
        critical_labels = ["breaking-change", "security", "architecture", "manifesto", "critical"]
        if any(label in labels for label in critical_labels):
            return True

        if size > 5000:
            return True

        critical_keywords = [
            "manifesto consolidado",
            "copilot-instructions.md",
            "princípios centrais",
            "mudança estratégica",
        ]
        if any(keyword in body.lower() for keyword in critical_keywords):
            return True

        return False

    def _check_auto_merge_issue(self, labels: list, body: str, size: int) -> bool:
        """Verifica se issue pode ser auto-merge."""
        approved_labels = ["documentation", "typo", "dependencies", "good first issue"]
        if not any(label in labels for label in approved_labels):
            return False

        blocked_labels = ["breaking-change", "security", "architecture", "manifesto"]
        if any(label in labels for label in blocked_labels):
            return False

        if size > 2000:
            return False

        critical_keywords = [
            "manifesto consolidado",
            "copilot-instructions.md",
        ]
        if any(keyword in body.lower() for keyword in critical_keywords):
            return False

        return True

    def _check_manual_review_pr(self, labels: list, files: list, lines: int) -> bool:
        """Verifica se PR deve ser manual-review."""
        critical_labels = ["breaking-change", "security", "architecture", "needs-discussion"]
        if any(label in labels for label in critical_labels):
            return True

        if lines > 500:
            return True

        critical_files = [
            ".github/copilot-instructions.md",
            ".github/copilot-diretrizes/",
            "ManifestoMCP.md",
            ".github/workflows/",
        ]
        for file in files:
            filename = file.get("filename", "")
            if any(critical in filename for critical in critical_files):
                return True

        return False

    def _check_auto_merge_pr(self, labels: list, files: list, lines: int) -> bool:
        """Verifica se PR pode ser auto-merge."""
        approved_labels = ["documentation", "typo", "dependencies"]
        if not any(label in labels for label in approved_labels):
            return False

        blocked_labels = ["breaking-change", "security", "needs-discussion"]
        if any(label in labels for label in blocked_labels):
            return False

        if lines > 100:
            return False

        # Verificar tipos de arquivo
        for file in files:
            filename = file.get("filename", "")
            # Apenas .md em subprojetos ou docs/
            if not (filename.endswith(".md") or "/docs/" in filename or "/debates/" in filename):
                return False

        return True

    def _classify_manual_review_issue(self, labels: list, body: str, size: int) -> Dict:
        """Classifica issue como manual-review."""
        reasons = []
        if any(label in labels for label in ["breaking-change", "security", "architecture", "manifesto", "critical"]):
            reasons.append("Label crítico presente")
        if size > 5000:
            reasons.append("Tamanho > 5000 caracteres (alta complexidade)")
        if "manifesto consolidado" in body.lower() or "copilot-instructions.md" in body.lower():
            reasons.append("Menciona artefato crítico")

        justificativa = "Manual-review necessário: " + ", ".join(reasons)
        return self._create_result("manual-review", 95, justificativa)

    def _classify_auto_merge_issue(self, labels: list, body: str, size: int) -> Dict:
        """Classifica issue como auto-merge."""
        confidence = 90
        if size < 500:
            confidence = 95
        if "documentation" in labels or "typo" in labels:
            confidence = 98

        justificativa = f"Issue simples ({', '.join(labels)}), tamanho {size} chars, sem riscos identificados"
        return self._create_result("auto-merge", confidence, justificativa)

    def _classify_needs_simulation_issue(self, labels: list, body: str, size: int) -> Dict:
        """Classifica issue como needs-simulation."""
        justificativa = "Não se qualifica para auto-merge nem manual-review, requer análise multi-perspectiva"
        return self._create_result("needs-simulation", 80, justificativa)

    def _classify_manual_review_pr(self, labels: list, files: list, lines: int) -> Dict:
        """Classifica PR como manual-review."""
        reasons = []
        if lines > 500:
            reasons.append(f"{lines} linhas modificadas (limite: 500)")
        if any(label in labels for label in ["breaking-change", "security"]):
            reasons.append("Label crítico presente")

        justificativa = "Manual-review necessário: " + ", ".join(reasons)
        return self._create_result("manual-review", 95, justificativa)

    def _classify_auto_merge_pr(self, labels: list, files: list, lines: int) -> Dict:
        """Classifica PR como auto-merge."""
        confidence = 90
        if lines < 50:
            confidence = 95
        if "typo" in labels:
            confidence = 98

        justificativa = f"PR simples ({', '.join(labels)}), {lines} linhas, apenas docs/markdown"
        return self._create_result("auto-merge", confidence, justificativa)

    def _classify_needs_simulation_pr(self, labels: list, files: list, lines: int) -> Dict:
        """Classifica PR como needs-simulation."""
        justificativa = "Não se qualifica para auto-merge nem manual-review, requer análise multi-perspectiva"
        return self._create_result("needs-simulation", 80, justificativa)

    def _create_result(self, category: str, confidence: int, justificativa: str) -> Dict:
        """Cria resultado estruturado da classificação."""
        return {
            "category": category,
            "confidence": confidence,
            "justificativa": justificativa,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": self.version,
        }


def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description="Classificador AutoFlow")
    parser.add_argument("--type", choices=["issue", "pr"], required=True, help="Tipo: issue ou pr")
    parser.add_argument("--number", type=int, required=True, help="Número da issue/PR")
    parser.add_argument("--data", type=str, help="JSON com dados da issue/PR (opcional)")

    args = parser.parse_args()

    classificador = Classificador()

    # Se dados fornecidos via --data, usar diretamente
    if args.data:
        data = json.loads(args.data)
    else:
        # TODO: Buscar dados via GitHub API
        print("Erro: --data é obrigatório no MVP. Integração com GitHub API será implementada.", file=sys.stderr)
        sys.exit(1)

    # Classificar
    if args.type == "issue":
        resultado = classificador.classificar_issue(data)
    else:
        resultado = classificador.classificar_pr(data)

    # Output JSON
    print(json.dumps(resultado, indent=2))


if __name__ == "__main__":
    main()
