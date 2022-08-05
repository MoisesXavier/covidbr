import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando o nome das colunas da tabela
df = df.rename(columns={'newDeaths':'Novos óbitos',
'newCases':'Novos casos', 'deaths_per_100k_inhabitants':'Óbitos por 100 mil habitantes',
'totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'}) # Continuar

# Seleção do Estado
estados = list(df['state'].unique())
# print(estados)
state = st.sidebar.selectbox('Qual estado?', estados)

# Seleção da coluna
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

# Seleção das linhas que pertecem ao estado
df = df[df['state'] == state]
 
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

# Imprimindo no código python
# print('DADOS COVID - BRASIL')
# print('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para amostragem.')

# Imprimindo na aplicação
st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar no gráfico. Utilize o menu lateral para amostragem.')



# Plot = Para mostrar a figura/gráfico dentro do código python
# fig.show()

# Plot - na aplicação
st.plotly_chart(fig, use_container_width=True)

# Imprimindo no python
# print('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')


# Imprimindo na aplicação
st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
