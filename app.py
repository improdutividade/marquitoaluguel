import streamlit as st
import locale
from datetime import datetime

# Configurar a formatação local para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_valor(valor):
    return locale.currency(valor, grouping=True, symbol=None)

def calcular_valor_aluguel(data_inicio, valor_aluguel_mensal):
    # Função de cálculo aqui

# Título
st.title("Impostômetro de Aluguel")

# Seção para a entrada de data
st.subheader("Período de Cálculo")
data_inicio_fixa = st.date_input("De:", datetime.strptime("15/07/2023", "%d/%m/%Y"))
data_fim = st.date_input("Até:", datetime.now())

# Seção para exibir o contador
valor_gasto_placeholder = st.empty()
valor_aluguel_mensal = 1750.00
valor_gasto = calcular_valor_aluguel(data_inicio_fixa, valor_aluguel_mensal)

# Formate o valor usando a função personalizada
valor_formatado = formatar_valor(valor_gasto)
valor_gasto_placeholder.text(f"**Valor gasto com aluguel:** {valor_formatado}")

# Adicione gráficos, visualizações ou elementos interativos conforme necessário

# Rodapé
st.markdown("<small>© 2024 Seu Nome. Todos os direitos reservados.</small>", unsafe_allow_html=True)
