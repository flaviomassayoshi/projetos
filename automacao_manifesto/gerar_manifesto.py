"""
Script para gerar ManifestoMCP.md a partir do TEMPLATE_ATUALIZACAO_MANIFESTO.md
Remove instruções internas (comentários HTML) e exporta apenas o conteúdo relevante.
"""
import re

TEMPLATE_PATH = '.github/TEMPLATE_ATUALIZACAO_MANIFESTO.md'
MANIFESTO_PATH = 'ManifestoMCP.md'

with open(TEMPLATE_PATH, encoding='utf-8') as f:
    template = f.read()

# Remove blocos de instruções internas (entre <!-- ... -->)
conteudo = re.sub(r'<!--.*?-->', '', template, flags=re.DOTALL)

# Remove linhas de instrução específicas do template (opcional, pode ser ajustado)
conteudo = re.sub(r'^## Instruções.*?\n(\d+\..*?\n)+', '', conteudo, flags=re.MULTILINE)

# Remove checklist de validação MVP (opcional)
conteudo = re.sub(r'### Checklist de Validação MVP.*?\n( - \[.*?\n)+', '', conteudo, flags=re.MULTILINE)

# Remove instruções "apenas para edição deste template"
conteudo = re.sub(r'## Instruções \(apenas para edição deste template\).*?\n(.*?\n)+?# AVISO IMPORTANTE', '# AVISO IMPORTANTE', conteudo, flags=re.DOTALL)

# Remove linhas em branco duplicadas
conteudo = re.sub(r'\n{3,}', '\n\n', conteudo)

# Salva o manifesto gerado
with open(MANIFESTO_PATH, 'w', encoding='utf-8') as f:
    f.write(conteudo.strip() + '\n')

print('ManifestoMCP.md gerado com sucesso.')
