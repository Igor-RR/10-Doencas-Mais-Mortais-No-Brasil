import streamlit as st
import pandas as pd 
import plotly.express as px

#analisando o arquivo

df = pd.read_csv("GHE_FULL_DD.csv",sep=",")

# Coletando os índices que contém BRA
indice = 1
lista_indice = []

for nacao in df["DIM_COUNTRY_CODE"]:
    if nacao == "BRA":
        lista_indice.append(indice)
    indice += 1

# Recortando da Dataframe original as linhas que contenham apenas o Brasil
df = df.iloc[lista_indice[0]:lista_indice[-1]]

# Ordenando os valores em ordem decrescente
df = df.sort_values(by="VAL_DTHS_RATE100K_NUMERIC",ascending=False)

#Recortando os 10 maiores valores

df = df.head(10)


# Criando o gráfico de pizza

fig = px.pie(df,values="VAL_DTHS_RATE100K_NUMERIC", 
             names="DIM_GHECAUSE_TITLE",
             color="DIM_GHECAUSE_TITLE",
             title="Valores a cada 100.000 habitantes",
             color_discrete_sequence=px.colors.sequential.ice
             )


#Front end
st.set_page_config(page_title="Análises de saúde")
st.title("Causas de morte no Brasil em 2021")
st.plotly_chart(figure_or_data=fig,theme=None)


