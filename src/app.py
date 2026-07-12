import json
import pandas as pd
import requests
import streamlit as st

# ============= CONFIGURAÇÃO =============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# =========== CARREGAR DADOS DO ALERTA DE GASTOS ===========
perfil = json.load(open('./data/perfil_usuario.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
limites_categorias = json.load(open('./data/categorias_limites.json'))

# =========== MONTAR CONTEXTO PARA O ALERTA ===========
contexto = f"""
USUÁRIO: {perfil['nome']}, {perfil['idade']} anos
LIMITE MENSAL GLOBAL: R$ {perfil['limite_mensal_total']}
AVISO DE ALERTA ATIVADO EM: {perfil['porcentagem_alerta']}% do limite.

GASTOS E TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

LIMITES POR CATEGORIA DE GASTO:
{json.dumps(limites_categorias, indent=2, ensure_ascii=False)}
"""

#============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o ECO, um assistente virtual especialista em controle orçamentário.

OBJETIVO:
Ajudar o usuário a monitorar suas despesas, alertando imediatamente quando ele estiver próximo de atingir ou
quando já tiver estourado o limite definido para cada categoria de gasto.

REGRAS:
1. Sempre compare o gasto atual do cliente com o limite estabelecido para a categoria antes de responder;
2. Use os dados fornecidos no arquivo de transações para dar respostas exatas e personalizadas;
3. Adote um tom firme, porém amigável, conscientizando o usuário sobre o impacto de estourar o orçamento;
4. Se o usuário perguntar algo fora do histórico ou sem dados suficientes, admita: "Não encontrei esse registro nas suas transações recentes, mas posso te ajudar a revisar os limites atuais...";
5. Sempre termine a interação oferecendo uma dica rápida de economia para a categoria afetada;
6. Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ============= CHAMAR OLLAMA =============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO USUÁRIO:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============= INTERFACE =============
st.title("💸 ECO - Alerta de Gastos")

if pergunta := st.chat_input("Pergunte algo sobre seus gastos ou limites..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
