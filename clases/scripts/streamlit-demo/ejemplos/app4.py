import streamlit as st
import pandas as pd
import numpy as np

st.title("Aplicación con menú lateral")

# Menú lateral
st.sidebar.title("Opciones")
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "💾 Datos", "📈 Gráficos", "🤯 Acerca de"]
)

# Contenido según la opción seleccionada
if opcion == "🏠 Inicio":
    st.write("## Bienvenido a nuestra aplicación")
    st.write("Esta es una demostración de Streamlit con menú lateral.")
    
elif opcion == "💾 Datos":
    st.write("## Sección de Datos")
    data = {
        'Nombre': ['Ana', 'Juan', 'María', 'Carlos'],
        'Edad': [25, 30, 22, 28],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    
elif opcion == "📈 Gráficos":
    st.write("## Sección de Gráficos")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)
    
else:
    st.write("## Acerca de")
    st.write("Esta aplicación es un ejemplo para la última clase de Python  .")
    st.image("https://www.python.org/static/community_logos/python-powered-w.svg", width=500)