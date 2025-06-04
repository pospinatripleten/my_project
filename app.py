import pandas as pd
import plotly.express as px
import streamlit as st
 
autos= pd.read_csv('C:\\Users\\Paola\\Myprojects\\my_project\\vehicles_us.csv',sep=',') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
hist_button2 = st.checkbox('Grafico de Dispersión') # crear un botón
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(autos, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

 
if hist_button2: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un grafico de dispersión')
         
    # crear un histograma
    figb = px.scatter(autos, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(figb, use_container_width=True)
