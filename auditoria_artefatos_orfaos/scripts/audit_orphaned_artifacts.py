#!/usr/bin/env python3
"""
Script de Auditoria de Artefatos Órfãos — ScarecrowLab

Este script identifica e documenta artefatos órfãos no repositório:
- Branches não mescladas sem PRs associados
- Pull Requests não mesclados (abertos, fechados, inativos)
- Issues abertas sem vínculo com PRs ou merges

Uso:
    python audit_orphaned_artifacts.py [--repo OWNER/REPO] [--output FILE]

Requer:
    - GITHUB_TOKEN: Token de autenticação do GitHub (variável de ambiente)
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import urllib.request
import urllib.error


class GitHubAPIClient:
    """Cliente simplificado para GitHub API v3"""
    
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Faz requisição à API do GitHub"""
        url = f"{self.base_url}{endpoint}"
        if params:
            query = "&".join([f"{k}={v}" for k, v in params.items()])
            url = f"{url}?{query}"
        
        req = urllib.request.Request(url, headers=self.headers)
        
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            print(f"Erro na requisição {endpoint}: {e.code} - {e.reason}", file=sys.stderr)
            if e.code == 401:
                print("Erro de autenticação. Verifique GITHUB_TOKEN.", file=sys.stderr)
            return []
        except Exception as e:
            print(f"Erro inesperado: {e}", file=sys.stderr)
            return []
    
    def get_branches(self, owner: str, repo: str) -> List[Dict]:
        """Lista todas as branches do repositório"""
        return self._make_request(f"/repos/{owner}/{repo}/branches", {"per_page": 100})
    
    def get_branch_commits(self, owner: str, repo: str, branch: str) -> List[Dict]:
        """Lista commits de uma branch"""
        return self._make_request(f"/repos/{owner}/{repo}/commits", 
                                  {"sha": branch, "per_page": 10})
    
    def get_pull_requests(self, owner: str, repo: str, state: str = "all") -> List[Dict]:
        """Lista pull requests do repositório"""
        return self._make_request(f"/repos/{owner}/{repo}/pulls", 
                                  {"state": state, "per_page": 100})
    
    def get_issues(self, owner: str, repo: str, state: str = "open") -> List[Dict]:
        """Lista issues do repositório"""
        return self._make_request(f"/repos/{owner}/{repo}/issues", 
                                  {"state": state, "per_page": 100})
    
    def compare_branches(self, owner: str, repo: str, base: str, head: str) -> Dict:
        """Compara duas branches"""
        return self._make_request(f"/repos/{owner}/{repo}/compare/{base}...{head}")


class ArtifactAuditor:
    """Auditor de artefatos órfãos"""
    
    def __init__(self, client: GitHubAPIClient, owner: str, repo: str):
        self.client = client
        self.owner = owner
        self.repo = repo
        self.default_branch = "master"
    
    def audit_branches(self) -> List[Dict]:
        """Identifica branches órfãs (não mescladas sem PRs)"""
        print("🔍 Auditando branches...")
        branches = self.client.get_branches(self.owner, self.repo)
        pull_requests = self.client.get_pull_requests(self.owner, self.repo, "all")
        
        # Criar mapa de branches com PRs
        branches_with_prs = set()
        for pr in pull_requests:
            if pr.get("head") and pr["head"].get("ref"):
                branches_with_prs.add(pr["head"]["ref"])
        
        orphaned_branches = []
        
        for branch in branches:
            branch_name = branch.get("name", "")
            
            # Pular branch padrão
            if branch_name == self.default_branch:
                continue
            
            # Verificar se tem PR associado
            if branch_name in branches_with_prs:
                continue
            
            # Verificar se está mesclada
            comparison = self.client.compare_branches(
                self.owner, self.repo, self.default_branch, branch_name
            )
            
            if isinstance(comparison, dict) and comparison.get("ahead_by", 0) > 0:
                # Branch tem commits não mesclados
                commits = self.client.get_branch_commits(self.owner, self.repo, branch_name)
                last_commit = commits[0] if commits else {}
                
                orphaned_branches.append({
                    "name": branch_name,
                    "commits_ahead": comparison.get("ahead_by", 0),
                    "last_commit_date": last_commit.get("commit", {}).get("author", {}).get("date", "N/A"),
                    "last_commit_author": last_commit.get("commit", {}).get("author", {}).get("name", "N/A"),
                    "last_commit_sha": last_commit.get("sha", "N/A")[:7]
                })
        
        print(f"✅ Encontradas {len(orphaned_branches)} branches órfãs")
        return orphaned_branches
    
    def audit_pull_requests(self) -> Dict[str, List[Dict]]:
        """Identifica PRs não mesclados"""
        print("🔍 Auditando pull requests...")
        all_prs = self.client.get_pull_requests(self.owner, self.repo, "all")
        
        unmerged_prs = {
            "open": [],
            "closed_not_merged": [],
            "stale": []
        }
        
        now = datetime.utcnow()
        stale_threshold = now - timedelta(days=30)
        
        for pr in all_prs:
            # Pular PRs mesclados
            if pr.get("merged_at"):
                continue
            
            pr_data = {
                "number": pr.get("number"),
                "title": pr.get("title", ""),
                "state": pr.get("state", ""),
                "author": pr.get("user", {}).get("login", "N/A"),
                "created_at": pr.get("created_at", "N/A"),
                "updated_at": pr.get("updated_at", "N/A"),
                "branch": pr.get("head", {}).get("ref", "N/A")
            }
            
            if pr.get("state") == "open":
                # Verificar se está stale
                updated_date = datetime.strptime(pr.get("updated_at", ""), "%Y-%m-%dT%H:%M:%SZ")
                if updated_date < stale_threshold:
                    unmerged_prs["stale"].append(pr_data)
                else:
                    unmerged_prs["open"].append(pr_data)
            else:
                unmerged_prs["closed_not_merged"].append(pr_data)
        
        total = sum(len(v) for v in unmerged_prs.values())
        print(f"✅ Encontrados {total} PRs não mesclados")
        return unmerged_prs
    
    def audit_issues(self) -> Dict[str, List[Dict]]:
        """Identifica issues órfãs (abertas sem vínculo)"""
        print("🔍 Auditando issues...")
        open_issues = self.client.get_issues(self.owner, self.repo, "open")
        all_prs = self.client.get_pull_requests(self.owner, self.repo, "all")
        
        # Criar mapa de issues referenciadas por PRs
        issues_with_prs = set()
        for pr in all_prs:
            body = pr.get("body", "")
            if body:
                # Procurar referências #123
                import re
                refs = re.findall(r'#(\d+)', body)
                issues_with_prs.update(refs)
        
        orphaned_issues = {
            "without_link": [],
            "stale": []
        }
        
        now = datetime.utcnow()
        stale_threshold = now - timedelta(days=60)
        
        for issue in open_issues:
            # Pular pull requests (issues e PRs compartilham numeração)
            if issue.get("pull_request"):
                continue
            
            issue_number = str(issue.get("number"))
            issue_data = {
                "number": issue.get("number"),
                "title": issue.get("title", ""),
                "author": issue.get("user", {}).get("login", "N/A"),
                "created_at": issue.get("created_at", "N/A"),
                "updated_at": issue.get("updated_at", "N/A"),
                "labels": [l.get("name", "") for l in issue.get("labels", [])]
            }
            
            # Verificar se está vinculada a PR
            if issue_number not in issues_with_prs:
                updated_date = datetime.strptime(issue.get("updated_at", ""), "%Y-%m-%dT%H:%M:%SZ")
                if updated_date < stale_threshold:
                    orphaned_issues["stale"].append(issue_data)
                else:
                    orphaned_issues["without_link"].append(issue_data)
        
        total = sum(len(v) for v in orphaned_issues.values())
        print(f"✅ Encontradas {total} issues órfãs")
        return orphaned_issues


class ReportGenerator:
    """Gerador de relatórios em markdown"""
    
    @staticmethod
    def generate(owner: str, repo: str, branches: List[Dict], 
                 prs: Dict[str, List[Dict]], issues: Dict[str, List[Dict]]) -> str:
        """Gera relatório completo em markdown"""
        
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        
        report = f"""# Relatório de Auditoria — Artefatos Órfãos

**Repositório:** {owner}/{repo}  
**Data/Hora:** {timestamp}  
**Gerado por:** audit_orphaned_artifacts.py

---

## Sumário Executivo

| Categoria | Quantidade |
|-----------|------------|
| Branches órfãs | {len(branches)} |
| PRs abertos não mesclados | {len(prs['open'])} |
| PRs fechados não mesclados | {len(prs['closed_not_merged'])} |
| PRs stale (>30 dias sem atividade) | {len(prs['stale'])} |
| Issues sem vínculo | {len(issues['without_link'])} |
| Issues stale (>60 dias sem atividade) | {len(issues['stale'])} |

---

## 1. Branches Órfãs

**Critério:** Branches com commits não mesclados na master e sem PRs associados.

"""
        
        if branches:
            report += "| Branch | Commits à frente | Último commit | Autor | SHA |\n"
            report += "|--------|------------------|---------------|-------|-----|\n"
            for branch in branches:
                report += f"| `{branch['name']}` | {branch['commits_ahead']} | "
                report += f"{branch['last_commit_date']} | {branch['last_commit_author']} | "
                report += f"`{branch['last_commit_sha']}` |\n"
        else:
            report += "✅ Nenhuma branch órfã encontrada.\n"
        
        report += "\n---\n\n## 2. Pull Requests Não Mesclados\n\n"
        
        # PRs abertos
        report += f"### 2.1 PRs Abertos ({len(prs['open'])})\n\n"
        if prs['open']:
            report += "| # | Título | Autor | Branch | Criado | Atualizado |\n"
            report += "|---|--------|-------|--------|--------|------------|\n"
            for pr in prs['open']:
                report += f"| #{pr['number']} | {pr['title'][:50]} | {pr['author']} | "
                report += f"`{pr['branch']}` | {pr['created_at'][:10]} | {pr['updated_at'][:10]} |\n"
        else:
            report += "✅ Nenhum PR aberto não mesclado.\n"
        
        # PRs fechados não mesclados
        report += f"\n### 2.2 PRs Fechados Não Mesclados ({len(prs['closed_not_merged'])})\n\n"
        if prs['closed_not_merged']:
            report += "| # | Título | Autor | Branch | Criado | Atualizado |\n"
            report += "|---|--------|-------|--------|--------|------------|\n"
            for pr in prs['closed_not_merged']:
                report += f"| #{pr['number']} | {pr['title'][:50]} | {pr['author']} | "
                report += f"`{pr['branch']}` | {pr['created_at'][:10]} | {pr['updated_at'][:10]} |\n"
        else:
            report += "✅ Nenhum PR fechado não mesclado.\n"
        
        # PRs stale
        report += f"\n### 2.3 PRs Stale (>30 dias sem atividade) ({len(prs['stale'])})\n\n"
        if prs['stale']:
            report += "| # | Título | Autor | Branch | Criado | Atualizado |\n"
            report += "|---|--------|-------|--------|--------|------------|\n"
            for pr in prs['stale']:
                report += f"| #{pr['number']} | {pr['title'][:50]} | {pr['author']} | "
                report += f"`{pr['branch']}` | {pr['created_at'][:10]} | {pr['updated_at'][:10]} |\n"
        else:
            report += "✅ Nenhum PR stale.\n"
        
        report += "\n---\n\n## 3. Issues Órfãs\n\n"
        
        # Issues sem vínculo
        report += f"### 3.1 Issues Sem Vínculo com PRs ({len(issues['without_link'])})\n\n"
        if issues['without_link']:
            report += "| # | Título | Autor | Labels | Criado | Atualizado |\n"
            report += "|---|--------|-------|--------|--------|------------|\n"
            for issue in issues['without_link']:
                labels = ", ".join(issue['labels']) if issue['labels'] else "-"
                report += f"| #{issue['number']} | {issue['title'][:50]} | {issue['author']} | "
                report += f"{labels} | {issue['created_at'][:10]} | {issue['updated_at'][:10]} |\n"
        else:
            report += "✅ Nenhuma issue sem vínculo.\n"
        
        # Issues stale
        report += f"\n### 3.2 Issues Stale (>60 dias sem atividade) ({len(issues['stale'])})\n\n"
        if issues['stale']:
            report += "| # | Título | Autor | Labels | Criado | Atualizado |\n"
            report += "|---|--------|-------|--------|--------|------------|\n"
            for issue in issues['stale']:
                labels = ", ".join(issue['labels']) if issue['labels'] else "-"
                report += f"| #{issue['number']} | {issue['title'][:50]} | {issue['author']} | "
                report += f"{labels} | {issue['created_at'][:10]} | {issue['updated_at'][:10]} |\n"
        else:
            report += "✅ Nenhuma issue stale.\n"
        
        report += "\n---\n\n## Recomendações\n\n"
        report += "1. **Branches órfãs:** Avaliar se devem ser removidas ou associadas a PRs\n"
        report += "2. **PRs não mesclados:** Revisar se devem ser mesclados, fechados ou atualizados\n"
        report += "3. **Issues órfãs:** Vincular a PRs, milestones ou fechar se não forem mais relevantes\n"
        report += "4. **Artefatos stale:** Considerar arquivamento ou atualização para reativar\n\n"
        report += "---\n\n"
        report += "> Relatório gerado automaticamente. Para mais informações, consulte "
        report += "[Manual de Uso](../docs/MANUAL_USO.md).\n"
        
        return report


def main():
    parser = argparse.ArgumentParser(description="Auditoria de artefatos órfãos no GitHub")
    parser.add_argument("--repo", default="flaviomassayoshi/ScarecrowLab",
                       help="Repositório no formato OWNER/REPO")
    parser.add_argument("--output", default="relatorios/audit_report.md",
                       help="Arquivo de saída do relatório")
    args = parser.parse_args()
    
    # Validar token
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("❌ Erro: GITHUB_TOKEN não configurado.", file=sys.stderr)
        print("   Configure a variável de ambiente: export GITHUB_TOKEN=seu_token", file=sys.stderr)
        sys.exit(1)
    
    # Parse repositório
    try:
        owner, repo = args.repo.split("/")
    except ValueError:
        print(f"❌ Erro: Formato inválido de repositório '{args.repo}'. Use OWNER/REPO", file=sys.stderr)
        sys.exit(1)
    
    print(f"🚀 Iniciando auditoria do repositório {owner}/{repo}...")
    print()
    
    # Inicializar cliente e auditor
    client = GitHubAPIClient(token)
    auditor = ArtifactAuditor(client, owner, repo)
    
    # Executar auditoria
    branches = auditor.audit_branches()
    prs = auditor.audit_pull_requests()
    issues = auditor.audit_issues()
    
    # Gerar relatório
    print()
    print("📝 Gerando relatório...")
    report = ReportGenerator.generate(owner, repo, branches, prs, issues)
    
    # Salvar relatório
    output_path = args.output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"✅ Relatório salvo em: {output_path}")
    print()
    print("📊 Auditoria concluída!")


if __name__ == "__main__":
    main()
