import streamlit as st
from datetime import datetime, timedelta

def calcular_valor_aluguel(data_inicio, valor_aluguel_mensal):
    # Defina a data de início
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")

    # Calcule a diferença em minutos entre a data de início e a data atual
    minutos_decorridos = (datetime.now() - data_inicio).total_seconds() / 60

    # Calcule o valor gasto considerando o valor por minuto
    valor_gasto = minutos_decorridos * (valor_aluguel_mensal / (30 * 24 * 60))  # Valor mensal convertido para minutos

    return valor_gasto

# Interface do Streamlit
st.title("Impostômetro de Aluguel")

# Input para a data de início
data_inicio = st.text_input("Digite a data de início (formato: dd/mm/yyyy)", "15/07/2023")

# Input para o valor mensal do aluguel
valor_aluguel_mensal = st.number_input("Digite o valor mensal do aluguel", min_value=0.01, value=1750.00)

# Botão para calcular o valor gasto
if st.button("Calcular"):
    valor_gasto = calcular_valor_aluguel(data_inicio, valor_aluguel_mensal)
    st.success(f"Valor gasto com aluguel: R$ {valor_gasto:.2f}")
