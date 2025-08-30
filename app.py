import streamlit as st

st.title("Mi primera app 🚀")
st.write("Este es mi primer proyecto hecho con Streamlit.")

import streamlit as st
import pandas as pd
import numpy as np

st.title("Mi primera aplicación 🚀")
st.write("Ahora con más interacción 🎉")

# Input de texto
nombre = st.text_input("Escribe tu nombre:")
if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido a mi app.")

# Slider
numero = st.slider("Elige un número", 1, 100, 50)
st.write("El número seleccionado es:", numero)

# Gráfico simple
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
