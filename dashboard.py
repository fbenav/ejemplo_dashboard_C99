import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Analisis de ventas para vehiculos usados")

df = pd.read_csv('dataset/vehicles_us.csv')

st.write("Vista de las 5 primeras filas del dataset:")
st.table(df.head())

st.subheader("Histograma para el kilometraje:")
fig = px.histogram(df, x="odometer") # crear un histograma
st.plotly_chart(fig, use_container_width=True)

build_lineplot = st.checkbox('Construir evolución de precio')

if build_lineplot:
    st.subheader('Evolución de precio promedio segun condicion vehiculo')

    df_2 = df.groupby(['date_posted','condition'])['price'].mean().reset_index()
    fig_2 = px.line(df_2, x="date_posted", y="price", color = 'condition',
                title='precio promedio vehiculos según dia de publicación')
    st.plotly_chart(fig_2, use_container_width=True)
