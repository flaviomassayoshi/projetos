#!/usr/bin/env python3
"""
Scarecrow AutoFlow — Simulador

Script para simulação de decisões por personas especializadas.

Uso:
    python simulador.py --type issue --number 123
    python simulador.py --type pr --number 456

Processo detalhado em: ../docs/PROCESSO_SIMULACAO.md
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Literal

VotoType = Literal["aprovar", "aprovar_com_ajustes", "rejeitar"]


class Simulador:
    """Simulador de decisões por personas."""

    def __init__(self):
        """Inicializa o simulador."""
        self.version = "1.0"
        self.personas = ["Engenheiro de Prompt", "Guardião do Manifesto", "DevOps Modular"]

    def simular(self, item_data: Dict, classificacao: Dict, validacao: Dict) -> Dict:
        """
        Simula decisão por personas.

        Args:
            item_data: Dados da issue/PR
            classificacao: Resultado da classificação
            validacao: Resultado da validação

        Returns:
            Dict com resultado da simulação
        """
        # Análise por cada persona
        analises = []
        analises.append(self._analise_engenheiro_prompt(item_data, validacao))
        analises.append(self._analise_guardiao_manifesto(item_data, validacao))
        analises.append(self._analise_devops_modular(item_data, validacao))

        # Deliberação
        resultado = self._deliberar(analises, item_data)

        return resultado

    def _analise_engenheiro_prompt(self, item_data: Dict, validacao: Dict) -> Dict:
        """Análise pela persona Engenheiro de Prompt."""
        titulo = item_data.get("title", "")
        corpo = item_data.get("body", "")

        # Critérios: clareza, completude, ausência de ambiguidades
        pontos_positivos = []
        pontos_atencao = []
        voto = "aprovar"
        confianca = 80

        # Avaliar clareza do título
        if len(titulo) > 30:
            pontos_positivos.append("Título descritivo e claro")
            confianca += 5
        else:
            pontos_atencao.append("Título poderia ser mais descritivo")
            confianca -= 5

        # Avaliar completude do corpo
        if len(corpo) > 200:
            pontos_positivos.append("Descrição completa com contexto adequado")
            confianca += 5
        else:
            pontos_atencao.append("Descrição poderia ser mais detalhada")
            voto = "aprovar_com_ajustes"
            confianca -= 5

        # Avaliar exemplos práticos
        if "exemplo" in corpo.lower() or "```" in corpo:
            pontos_positivos.append("Inclui exemplos práticos")
            confianca += 10
        else:
            pontos_atencao.append("Adicionar exemplos práticos melhoraria clareza")
            if voto == "aprovar":
                voto = "aprovar_com_ajustes"

        analise = f"Análise focada em clareza e efetividade. Título {'adequado' if len(titulo) > 30 else 'aceitável'}. Descrição {'completa' if len(corpo) > 200 else 'poderia ser expandida'}."

        return {
            "persona": "Engenheiro de Prompt",
            "voto": voto,
            "confianca": max(0, min(100, confianca)),
            "analise": analise,
            "pontos_positivos": pontos_positivos,
            "pontos_atencao": pontos_atencao,
        }

    def _analise_guardiao_manifesto(self, item_data: Dict, validacao: Dict) -> Dict:
        """Análise pela persona Guardião do Manifesto."""
        corpo = item_data.get("body", "")
        score_validacao = validacao.get("score", 0)

        # Critérios: conformidade, rastreabilidade, consistência terminológica
        pontos_positivos = []
        pontos_atencao = []
        voto = "aprovar"
        confianca = 85

        # Avaliar conformidade
        if score_validacao >= 90:
            pontos_positivos.append("Alta conformidade com artefatos constitucionais")
            confianca += 10
        elif score_validacao >= 75:
            pontos_positivos.append("Conformidade aceitável")
            voto = "aprovar_com_ajustes"
            pontos_atencao.append("Melhorar conformidade em validações não-aprovadas")
        else:
            voto = "rejeitar"
            pontos_atencao.append("Conformidade insuficiente, requer revisão")
            confianca = 60

        # Avaliar rastreabilidade
        if any(keyword in corpo.lower() for keyword in ["subprojeto", "checklist", "changelog", "ata"]):
            pontos_positivos.append("Demonstra rastreabilidade com artefatos relacionados")
            confianca += 5
        else:
            pontos_atencao.append("Adicionar referências a artefatos relacionados")

        # Avaliar glossário
        if any(termo in corpo.lower() for termo in ["arcabouço", "manifesto", "artefato persistente"]):
            pontos_positivos.append("Usa terminologia do glossário")
            confianca += 5

        analise = f"Análise focada em conformidade institucional. Score de validação: {score_validacao}/100. Conformidade {'excelente' if score_validacao >= 90 else 'aceitável' if score_validacao >= 75 else 'insuficiente'}."

        return {
            "persona": "Guardião do Manifesto",
            "voto": voto,
            "confianca": max(0, min(100, confianca)),
            "analise": analise,
            "pontos_positivos": pontos_positivos,
            "pontos_atencao": pontos_atencao,
        }

    def _analise_devops_modular(self, item_data: Dict, validacao: Dict) -> Dict:
        """Análise pela persona DevOps Modular."""
        files = item_data.get("files", [])
        labels = [label.get("name", "") for label in item_data.get("labels", [])]

        # Critérios: modularidade, automação, integrações
        pontos_positivos = []
        pontos_atencao = []
        voto = "aprovar"
        confianca = 80

        # Avaliar modularidade
        if len(files) > 0:
            # Verificar se arquivos estão em subprojeto isolado
            dirs = set([f.get("filename", "").split("/")[0] for f in files if "/" in f.get("filename", "")])
            if len(dirs) == 1:
                pontos_positivos.append("Mudanças isoladas em um subprojeto (alta modularidade)")
                confianca += 10
            elif len(dirs) <= 3:
                pontos_positivos.append("Mudanças em poucos subprojetos (modularidade aceitável)")
                confianca += 5
            else:
                pontos_atencao.append("Mudanças em muitos subprojetos (baixa modularidade)")
                voto = "aprovar_com_ajustes"
                confianca -= 10

        # Avaliar automação
        if any(label in labels for label in ["automation", "ci/cd"]):
            pontos_positivos.append("Relacionado a automação (alinhado com princípios)")
            confianca += 10

        # Avaliar integrações
        if "integração" in item_data.get("body", "").lower():
            pontos_positivos.append("Documenta integrações com outros componentes")
            confianca += 5

        analise = f"Análise focada em modularidade e automação. Modularidade {'alta' if len(files) == 0 or len(set([f.get('filename', '').split('/')[0] for f in files])) == 1 else 'aceitável'}."

        return {
            "persona": "DevOps Modular",
            "voto": voto,
            "confianca": max(0, min(100, confianca)),
            "analise": analise,
            "pontos_positivos": pontos_positivos,
            "pontos_atencao": pontos_atencao,
        }

    def _deliberar(self, analises: List[Dict], item_data: Dict) -> Dict:
        """Delibera baseado nas análises das personas."""
        # Contar votos
        votos = {"aprovar": 0, "aprovar_com_ajustes": 0, "rejeitar": 0}
        for analise in analises:
            voto = analise["voto"]
            votos[voto] += 1

        # Determinar tipo de consenso
        total_personas = len(analises)
        if votos["aprovar"] + votos["aprovar_com_ajustes"] == total_personas:
            tipo_consenso = "Consenso total (aprovação)"
            decisao = "aprovado" if votos["aprovar"] == total_personas else "aprovado_com_ajustes"
        elif votos["rejeitar"] == total_personas:
            tipo_consenso = "Consenso total (rejeição)"
            decisao = "rejeitado"
        elif votos["aprovar"] + votos["aprovar_com_ajustes"] >= total_personas / 2:
            tipo_consenso = "Consenso parcial (aprovação)"
            decisao = "aprovado_com_ajustes"
        elif votos["rejeitar"] >= total_personas / 2:
            tipo_consenso = "Consenso parcial (rejeição)"
            decisao = "rejeitado"
        else:
            tipo_consenso = "Dissenso"
            decisao = "manual-review"

        # Gerar justificativa
        justificativa = self._gerar_justificativa(analises, votos, tipo_consenso)

        # Gerar recomendações
        recomendacoes = self._gerar_recomendacoes(analises)

        return {
            "decisao": decisao,
            "tipo_consenso": tipo_consenso,
            "votos": votos,
            "analises": analises,
            "justificativa": justificativa,
            "recomendacoes": recomendacoes,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": self.version,
        }

    def _gerar_justificativa(self, analises: List[Dict], votos: Dict, tipo_consenso: str) -> str:
        """Gera justificativa da decisão."""
        if tipo_consenso == "Consenso total (aprovação)":
            return "Todas as personas aprovaram. Item atende critérios de clareza, conformidade e modularidade."
        elif tipo_consenso == "Consenso total (rejeição)":
            return "Todas as personas rejeitaram. Item não atende critérios mínimos em múltiplas perspectivas."
        elif tipo_consenso == "Consenso parcial (aprovação)":
            return f"Maioria das personas aprovou ({votos['aprovar'] + votos['aprovar_com_ajustes']}/{len(analises)}). Pontos de atenção da minoria devem ser considerados."
        elif tipo_consenso == "Consenso parcial (rejeição)":
            return f"Maioria das personas rejeitou ({votos['rejeitar']}/{len(analises)}). Item requer revisão significativa."
        else:
            return "Dissenso entre personas. Recomenda-se revisão humana para desempate."

    def _gerar_recomendacoes(self, analises: List[Dict]) -> List[str]:
        """Gera recomendações consolidadas."""
        recomendacoes = []
        for analise in analises:
            for ponto in analise["pontos_atencao"]:
                rec = f"{ponto} ({analise['persona']})"
                if rec not in recomendacoes:
                    recomendacoes.append(rec)
        return recomendacoes


def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description="Simulador AutoFlow")
    parser.add_argument("--type", choices=["issue", "pr"], required=True, help="Tipo: issue ou pr")
    parser.add_argument("--number", type=int, required=True, help="Número da issue/PR")
    parser.add_argument("--data", type=str, required=True, help="JSON com dados da issue/PR")
    parser.add_argument("--classificacao", type=str, required=True, help="JSON com resultado da classificação")
    parser.add_argument("--validacao", type=str, required=True, help="JSON com resultado da validação")

    args = parser.parse_args()

    simulador = Simulador()

    # Parse inputs
    data = json.loads(args.data)
    classificacao = json.loads(args.classificacao)
    validacao = json.loads(args.validacao)

    # Simular
    resultado = simulador.simular(data, classificacao, validacao)

    # Output JSON
    print(json.dumps(resultado, indent=2))


if __name__ == "__main__":
    main()
