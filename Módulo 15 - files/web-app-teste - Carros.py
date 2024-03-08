import streamlit as st
import pandas as pd
import altair as alt

# Dados fictícios dos 26 estados do Brasil
dados = {
    'Estado': ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'],
    'Carros Novos': [100, 150, 200, 120, 250, 180, 300, 170, 220, 190, 400, 230, 210, 280, 160, 240, 140, 350, 380, 130, 110, 170, 320, 260, 130, 450, 170],
    'Carros Usados': [80, 120, 150, 100, 200, 160, 250, 140, 180, 170, 320, 190, 160, 230, 120, 210, 100, 280, 300, 90, 80, 140, 270, 220, 90, 350, 130]
}

# Cria um DataFrame a partir dos dados
df = pd.DataFrame(dados)

# Configurações do Streamlit
st.title('Comparativo de Carros Novos e Usados por Estado')
st.write(df)

# Gráfico de barras comparando carros novos e usados
chart = alt.Chart(df).mark_bar().encode(
    x='Estado',
    y=alt.Y('Carros Novos', axis=alt.Axis(title='Quantidade de Carros')),
    color=alt.value('blue')
)

chart += alt.Chart(df).mark_bar().encode(
    x='Estado',
    y=alt.Y('Carros Usados'),
    color=alt.value('orange')
)

chart.properties(
    title='Comparativo de Carros Novos e Usados por Estado'
).configure_axis(
    labelAngle=90
)

# Exibe o gráfico no Streamlit
st.altair_chart(chart, use_container_width=True)
