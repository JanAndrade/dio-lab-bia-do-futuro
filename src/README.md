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

## Evidência de execução

<img width="1532" height="687" alt="Screenshot 2026-07-12 192625" src="https://github.com/user-attachments/assets/4a0b9079-1c49-445b-b86a-8e825de2678d" />


