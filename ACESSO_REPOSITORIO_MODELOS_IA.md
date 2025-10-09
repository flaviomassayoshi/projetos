# Acesso ao Repositório para Modelos de IA

## Contexto

Este documento esclarece como diferentes modelos de IA podem acessar o repositório `flaviomassayoshi/projetos`, as permissões disponíveis e as limitações técnicas de cada abordagem.

## Modelo de Acesso Atual

### GitHub Copilot (via GitHub Actions)

O GitHub Copilot que responde a issues e pull requests opera através do GitHub Actions com as seguintes capacidades:

**Permissões Concedidas:**
- ✅ Leitura completa do repositório (todos os arquivos e branches)
- ✅ Escrita em branches (criar, modificar arquivos)
- ✅ Criar e atualizar pull requests
- ✅ Adicionar comentários em issues e PRs
- ✅ Executar comandos via bash no ambiente de CI

**Limitações:**
- ❌ Não pode alterar configurações do repositório
- ❌ Não pode gerenciar permissões de usuários
- ❌ Não pode criar webhooks ou GitHub Apps
- ❌ Não tem acesso direto ao GitHub API fora do contexto do workflow
- ❌ Não pode conceder acesso a outros modelos de IA

### Outros Modelos de IA (Mistral, Ollama, etc.)

Modelos rodando localmente ou em servidores externos têm as seguintes opções de acesso:

#### 1. Acesso via Clone Local (Recomendado para Desenvolvimento)

**Como funciona:**
```bash
# Clonar o repositório (requer autenticação do GitHub)
git clone https://github.com/flaviomassayoshi/projetos.git

# Ou com SSH
git clone git@github.com:flaviomassayoshi/projetos.git
```

**Permissões:**
- Dependem das credenciais do usuário GitHub que clona
- Se o repositório é público: leitura livre para qualquer um
- Se o repositório é privado: requer convite/permissão do owner

**Recomendado para:**
- Modelos rodando localmente (ex: Mistral via Ollama)
- Scripts de automação com credenciais próprias
- Desenvolvimento e testes locais

#### 2. Acesso via GitHub API

**Como funciona:**
```python
import requests

# Leitura de arquivo público
response = requests.get(
    "https://api.github.com/repos/flaviomassayoshi/projetos/contents/README.md"
)

# Para operações de escrita, requer token de acesso pessoal (PAT)
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
```

**Permissões:**
- Leitura: livre para repositórios públicos
- Escrita: requer Personal Access Token (PAT) ou OAuth token
- Tokens devem ser criados pelo owner do repositório ou colaboradores autorizados

**Recomendado para:**
- Automações que precisam interagir com o GitHub remotamente
- Bots e serviços externos
- Integração com APIs de validação

#### 3. Acesso via Markdown (Padrão do Projeto)

**Como funciona:**
Conforme documentado em `python_apps/integracao_mcp_markdown/`, o projeto usa arquivos Markdown como canal de comunicação entre modelos:

```
1. Modelo A escreve em arquivo.md (via clone local)
2. Commit e push das mudanças
3. Modelo B lê arquivo.md (via clone local ou GitHub)
4. Modelo B responde no mesmo arquivo
5. Ciclo se repete
```

**Permissões:**
- Mesmo modelo do clone local
- Cada modelo precisa de suas próprias credenciais Git

**Recomendado para:**
- Debates multimodelo conforme metodologia do projeto
- Rastreabilidade completa via Git
- Auditoria e versionamento

## Configurando Acesso para Novos Modelos

### Para o Owner do Repositório

Se você deseja conceder acesso a modelos de IA operados por outras pessoas ou serviços:

#### Opção 1: Adicionar Colaborador (Acesso Direto)
1. Acesse: `https://github.com/flaviomassayoshi/projetos/settings/access`
2. Clique em "Add people"
3. Adicione o usuário GitHub da pessoa que operará o modelo
4. Escolha o nível de permissão: Read, Write, ou Admin

#### Opção 2: Personal Access Token (Acesso Programático)
1. Como owner, você pode criar PATs próprios
2. Acesse: `https://github.com/settings/tokens`
3. Clique em "Generate new token (classic)"
4. Selecione scopes necessários: `repo` para acesso completo
5. **Importante:** Tokens devem ser tratados como senhas e nunca commitados

#### Opção 3: GitHub App (Acesso de Automação)
Para automações mais complexas:
1. Crie um GitHub App em `https://github.com/settings/apps`
2. Configure permissões (Contents: Read/Write, Issues: Read/Write, etc.)
3. Instale o app no repositório
4. Use credenciais do app para autenticar

### Para Usuários/Desenvolvedores

Se você deseja usar seu próprio modelo de IA para interagir com este repositório:

1. **Repositório Público:** Clone livremente para leitura
2. **Repositório Privado:** Solicite acesso ao owner (@flaviomassayoshi)
3. **Para escrita:** Configure suas credenciais Git localmente

```bash
# Configurar Git
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Configurar autenticação (use PAT ou SSH)
# Via HTTPS com PAT:
git clone https://github.com/flaviomassayoshi/projetos.git
# O Git solicitará username e token (use PAT como senha)

# Via SSH (recomendado):
git clone git@github.com:flaviomassayoshi/projetos.git
# Requer chave SSH configurada: https://docs.github.com/en/authentication
```

## Limitações do GitHub Copilot (Este Agente)

Como agente de IA operando via GitHub Actions, **não posso:**

- ❌ Alterar configurações de permissões do repositório
- ❌ Adicionar colaboradores
- ❌ Criar ou revogar tokens de acesso
- ❌ Instalar GitHub Apps
- ❌ Conceder acesso a outros modelos de IA

**Apenas o owner do repositório** (@flaviomassayoshi) pode gerenciar permissões através da interface web do GitHub ou da API com credenciais apropriadas.

## Recomendações

### Para Integração Multimodelo

1. **Clone Local + Credenciais Próprias** (Preferido)
   - Cada modelo opera com clone local do repositório
   - Usa credenciais Git do desenvolvedor/operador
   - Melhor controle e rastreabilidade

2. **Markdown como Canal de Comunicação**
   - Seguir padrão documentado em `python_apps/integracao_mcp_markdown/`
   - Debates estruturados via commits
   - Auditoria completa via histórico Git

3. **Automação com PAT ou GitHub App**
   - Para bots e serviços automatizados
   - Requer configuração pelo owner
   - Tokens devem ser armazenados de forma segura (secrets, env vars)

### Segurança

- ⚠️ **Nunca commite tokens ou senhas** no repositório
- ⚠️ Use `.gitignore` para excluir arquivos de configuração sensíveis
- ⚠️ Revogue tokens imediatamente se houver suspeita de comprometimento
- ⚠️ Use chaves SSH com passphrase para maior segurança

## Próximos Passos

Se você precisa de acesso específico:

1. **Identifique o tipo de acesso necessário:**
   - Leitura apenas? (repositório público é suficiente)
   - Escrita? (precisa de colaborador ou PAT)
   - Automação? (considere GitHub App)

2. **Entre em contato com o owner:**
   - Via issue no repositório
   - Especifique: qual modelo, qual finalidade, qual nível de acesso

3. **Para colaboradores do projeto:**
   - Configure suas credenciais Git localmente
   - Clone o repositório
   - Siga as diretrizes em `.github/copilot-instructions.md`

## Referências

- [Documentação de Permissões do GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
- [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub Apps](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps)
- [SSH Keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

**Última atualização:** 2025-01-27  
**Responsável:** GitHub Copilot (via issue #request-repo-access-ia-models)
