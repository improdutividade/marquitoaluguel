import streamlit as st
from datetime import datetime, timedelta
import time

st.set_page_config(
    page_title="Aluguel Marquito",
    page_icon="💸",
    layout='wide',
    initial_sidebar_state='expanded'
)    

def calcular_valor_aluguel(data_inicio, valor_aluguel_mensal):
    # Defina a data de início
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")

    # Calcule a diferença em milissegundos entre a data de início e a data atual
    milissegundos_decorridos = (datetime.now() - data_inicio).total_seconds() * 1000

    # Calcule o valor gasto considerando o valor por milissegundo
    valor_gasto = milissegundos_decorridos * (valor_aluguel_mensal / (30 * 24 * 60 * 60 * 1000))  # Valor mensal convertido para milissegundos

    return valor_gasto

def itens_comprados(valor_gasto, valor_item):
    quantidade = valor_gasto / valor_item
    return int(quantidade)

# URL direto da imagem no GitHub
background_image = "https://raw.githubusercontent.com/improdutividade/marquitoaluguel/main/quito.jpeg"

st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url('{background_image}');
            background-size: cover;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }}

        h1 {{
            font-size: 2.5em;
            text-align: center;
            margin: 0;
        }}

        h2 {{
            font-size: 1.8em;
            text-align: center;
            margin: 10px 0;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Interface do Streamlit
st.title("Impostômetro de Aluguel")
st.subheader("Acompanhe quantos R$ o André Russo Dias Marquito gastou com aluguel em uma casa que ele ainda não mora.")
st.subheader("Valor gasto com aluguel desde 18/01/2024")

# Data de início fixa
data_inicio_fixa = "18/01/2024"

# Valor mensal do aluguel
valor_aluguel_mensal = 1750.00

# Itens e seus preços
itens = {
    "Tablitos": 29.90,
    "Heineken 330ml": 6.78,
    "Fiat Argo": 83490.00,
    "Kinder Ovo": 8.00,
    "Air Jordan 1 High Chicago (2015)": 2200.00,
    "Iphone 12 64gb": 3299.00,
    "Broto de Bambu Grosso": 25.95,
    "Arroz 5kg": 25.50,
    "Camisa do Cabuloso 2024": 269.90,
}

# Crie espaços reservados para os textos
valor_gasto_placeholder = st.empty()
item_comprado_placeholder = st.empty()

# Tempo atual para controle de reinicialização
tempo_inicial = time.time()

# Botão para reiniciar o aplicativo
if st.button("Reiniciar Aplicativo"):
    st.experimental_rerun()

while True:
    # Calcule o valor gasto com aluguel
    valor_gasto = calcular_valor_aluguel(data_inicio_fixa, valor_aluguel_mensal)

    # Exiba o valor formatado com 6 casas decimais no espaço reservado
    valor_gasto_placeholder.markdown(f"<h1>Valor gasto com aluguel: R$ {valor_gasto:.6f}</h1>", unsafe_allow_html=True)

    # Atualize dinamicamente os itens comprados
    for item, valor_item in itens.items():
        quantidade = itens_comprados(valor_gasto, valor_item)
        item_comprado_placeholder.markdown(f"<h2>Com esse valor poderiam ser comprados {quantidade} {item}.</h2>", unsafe_allow_html=True)
        time.sleep(5)  # Aguarde 5 segundos antes de passar para o próximo item
        item_comprado_placeholder.empty()  # Limpe o espaço reservado

    # Aguarde 0.1 segundo antes de recomeçar a atualização
    time.sleep(0.1)

    # Reinicie o aplicativo após 1 hora (3600 segundos)
    if time.time() - tempo_inicial > 3600:
        st.experimental_rerun()
