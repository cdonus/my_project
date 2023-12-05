import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Vehiculos')
        
car_data = pd.read_csv('/Users/user/my_project/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir Histograma') # crear un botón

        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Construir Grafico Dispersion') # crear un botón
if hist_button_2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
