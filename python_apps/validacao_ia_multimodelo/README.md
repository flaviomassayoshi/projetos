---

# Proposta Vigente

## Contexto

Deseja-se garantir que alterações feitas automaticamente pelo GitHub Copilot sejam revisadas/validadas por outros modelos de IA gratuitos ou open-source, aumentando a confiabilidade e reduzindo vieses ou erros automatizados.

## Objetivo

Permitir que toda alteração feita pelo Copilot seja submetida à validação por um ou mais modelos de IA gratuitos ou open-source, antes de ser considerada "aceita" no fluxo do projeto.

## Motivação

- Reduzir riscos de erros ou vieses de um único agente.
- Aumentar a transparência e confiança no fluxo automatizado.
- Possibilitar auditoria e aprendizado contínuo do processo de automação.

## Premissa Básica

A validação das alterações deve ocorrer dentro da própria IDE, sem depender de integrações externas como CI/CD. Essa é uma premissa fundamental deste projeto.

## Requisitos Iniciais

- Identificar modelos gratuitos e open-source disponíveis, avaliando limitações de uso e viabilidade de automação.
- Definir formato de submissão (ex: diff, patch, arquivo inteiro).
- Automatizar integração (scripts, GitHub Actions, etc.).
- Garantir rastreabilidade das validações.

## Possíveis Abordagens

- Integrar APIs de modelos open-source (ex: Llama.cpp, StarCoder, HuggingFace Inference API, etc.) e, opcionalmente, serviços gratuitos (ex: OpenAI GPT-3.5-turbo free tier, Google Gemini), sempre considerando limitações de uso e viabilidade para automação.
- Implementar extensão/plugin para IDE ou integração via CI/CD (ex: GitHub Actions) que detecte alterações do Copilot e submeta o diff para análise de outros modelos, exibindo o feedback ao usuário.
- Permitir múltiplos validadores (ex: consenso entre modelos, aprovação por maioria simples, ou outro critério explícito definido no projeto).
- Registrar logs de validação e decisões em formato flexível (changelog, JSON, banco leve, etc.), conforme necessidade do projeto.

## Limitações/Restrições

Integração via CI/CD (ex: GitHub Actions) está vetada e não será considerada nesta proposta.

## Acesso ao Repositório para Modelos de IA

Para informações sobre como diferentes modelos de IA podem acessar este repositório, incluindo permissões, limitações e recomendações de segurança, consulte:

📖 **[ACESSO_REPOSITORIO_MODELOS_IA.md](../../ACESSO_REPOSITORIO_MODELOS_IA.md)**

Este guia aborda:
- Como o GitHub Copilot acessa o repositório
- Opções de acesso para modelos locais (Mistral, Ollama, etc.)
- Configuração de permissões e credenciais
- Melhores práticas de segurança
