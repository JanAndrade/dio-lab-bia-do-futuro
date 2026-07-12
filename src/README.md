# Passo a passo de execução


## Setup do Ollama 

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"

```
## Código completo

Todo o código-fonte está no arquivo `app.py`.

```

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama esta rodando
ollama serve

# 3. Rodar a aplicação
streamlit run src/app.py
```
