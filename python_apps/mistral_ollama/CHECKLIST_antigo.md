# Checklist de Setup — Debate Multimodelo com Mistral 7B via Ollama

## 1. Instalação do Ollama
- [ ] Baixar o instalador do Ollama para Windows: https://ollama.com/download
- [ ] Executar o instalador e concluir a instalação
- [ ] Verificar se o Ollama está acessível no terminal (comando `ollama --version`)

## 2. Instalação do Modelo Mistral 7B
- [ ] No terminal, rodar: `ollama run mistral`
- [ ] (Opcional) Para versão instruída: `ollama run mistral:instruct`
- [ ] Confirmar que o modelo roda com suporte a GPU (CUDA 12.9)

## 3. Ambiente Python
- [ ] Criar ambiente virtual Python 3.10 dedicado ao subprojeto
- [ ] Ativar o ambiente virtual
- [ ] Instalar dependências necessárias (ex: requests, rich, etc.)

## 4. Script de Integração
- [ ] Criar script Python para enviar prompts ao Ollama (API local ou CLI)
- [ ] Permitir leitura de arquivos Markdown de debate e escrita das respostas
- [ ] Testar envio de prompt e recebimento de resposta do modelo

## 5. Integração com Fluxo de Debates
- [ ] Definir pasta de debates e formato dos arquivos Markdown
- [ ] Automatizar registro das respostas do modelo nos arquivos de debate
- [ ] Validar fluxo completo: prompt → resposta → registro no arquivo

## 6. Documentação e Uso
- [ ] Documentar comandos principais e exemplos de uso
- [ ] Registrar eventuais problemas e soluções

---

> Marque cada item conforme for concluindo. Checklist pode ser expandido conforme necessidades do projeto.
