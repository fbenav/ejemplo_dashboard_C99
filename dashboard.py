import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Analisis de ventas para vehiculos usados")
st.write("TO-DO: dashboard en progreso...")

df = pd.read_csv('dataset/vehicles_us.csv')

st.write("Vista de las 5 primeras filas del dataset:")
st.table(df.head())

st.subheader("Histograma para el kilometraje:")
fig = px.histogram(df, x="odometer") # crear un histograma
st.plotly_chart(fig, use_container_width=True)