import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualización de datos en Streamlit")

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear un gráfico con matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('sin(x)')
ax.set_title('Función Seno')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Crear un gráfico de barras con datos del DataFrame
data = {
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valores': [10, 25, 15, 30]
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index('Categoría'))

st.markdown("## Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Columna 1")
    st.write("Contenido de la columna 1")
    st.pyplot(fig)

with col2:
    st.subheader("Columna 2")
    st.write("Contenido de la columna 2")
    st.bar_chart(df.set_index('Categoría'))    