import streamlit as st
from datetime import datetime
from babel.numbers import format_currency

def calcular_valor_aluguel(data_inicio, valor_aluguel_mensal):
    # Defina a data de início
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")

    # Calcule a diferença em segundos entre a data de início e a data atual
    segundos_decorridos = (datetime.now() - data_inicio).total_seconds()

    # Calcule o valor gasto considerando o valor por segundo
    valor_gasto = segundos_decorridos * (valor_aluguel_mensal / (30 * 24 * 60 * 60))  # Valor mensal convertido para segundos

    return valor_gasto

# Interface do Streamlit
st.title("Impostômetro de Aluguel")

# Data de início fixa
data_inicio_fixa = "15/07/2023"

# Valor mensal do aluguel
valor_aluguel_mensal = 1750.00

# Calcule o valor gasto com aluguel
valor_gasto = calcular_valor_aluguel(data_inicio_fixa, valor_aluguel_mensal)

# Formate o valor como dinheiro
valor_formatado = format_currency(valor_gasto, 'BRL', locale='pt_BR')

# Exiba o valor formatado
st.text(f"Valor gasto com aluguel: {valor_formatado}")
