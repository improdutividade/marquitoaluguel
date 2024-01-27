import streamlit as st
from datetime import datetime

def calcular_valor_aluguel(data_inicio, valor_aluguel_mensal):
    # Defina a data de início
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")

    # Calcule a diferença em milissegundos entre a data de início e a data atual
    milissegundos_decorridos = (datetime.now() - data_inicio).total_seconds() * 1000

    # Calcule o valor gasto considerando o valor por milissegundo
    valor_gasto = milissegundos_decorridos * (valor_aluguel_mensal / (30 * 24 * 60 * 60 * 1000))  # Valor mensal convertido para milissegundos

    return valor_gasto

# Interface do Streamlit
st.title("Impostômetro de Aluguel")

# Data de início fixa
data_inicio_fixa = "15/07/2023"

# Valor mensal do aluguel
valor_aluguel_mensal = 1750.00

# Calcule o valor gasto com aluguel
valor_gasto = calcular_valor_aluguel(data_inicio_fixa, valor_aluguel_mensal)

# Exiba o valor formatado com 6 casas decimais
st.text(f"Valor gasto com aluguel: R$ {valor_gasto:.6f}")
