import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def display_trig_text(function_type, amplitude, frequency, phase):
    if function_type == "seno":
        trig = "\\sin"
    elif function_type == "coseno":
        trig = "\\cos"
    else:  # tangente
        trig = "\\tan" 

    title = f"{amplitude} \\times {trig}({frequency}x + {phase:.2f})"
    return title

# Empieza la página

st.title("Figuras interactivas con widgets")

# Widgets en la barra lateral para controlar la figura
st.sidebar.header("Controles de la figura")
function_type = st.sidebar.selectbox(
    "Selecciona una función:",
    ["seno", "coseno", "tangente"]
)

amplitude = st.sidebar.slider("Amplitud:", 0.1, 5.0 , 1.0, 0.1)
frequency = st.sidebar.slider("Frecuencia:", 0.1, 5.0, 1.0, 0.1)
phase = st.sidebar.slider("Fase:", 0.0, 2*np.pi, 0.0, 0.1)

# Configuración de visualización
show_grid = st.sidebar.checkbox("Mostrar cuadrícula", True)
line_color = st.sidebar.selectbox(
    "Color de línea:",
    ["blue", "red", "green", "purple", "orange"]
)
line_style = st.sidebar.selectbox(
    "Estilo de línea:",
    ["-", "--", "-.", ":"]
)

# Generar los datos según los parámetros seleccionados
x = np.linspace(0, 2*np.pi, 1000)

if function_type == "seno":
    y = amplitude * np.sin(frequency * x + phase)
elif function_type == "coseno":
    y = amplitude * np.cos(frequency * x + phase)
else:  # tangente
    y = amplitude * np.tan(frequency * x + phase)
    # Limitar los valores extremos para una mejor visualización
    y = np.clip(y, -10, 10)

st.write("Usando `st.latex`")
display_trig = display_trig_text(function_type, amplitude, frequency, phase)
st.latex(f"y = {display_trig}")

st.write("Usando `st.write`")
st.write(f"**Función** {function_type}: ${display_trig}$")

# Crear la figura
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color=line_color, linestyle=line_style, linewidth=2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_ylim(-5, 5)  # Límites fijos para el eje y
if show_grid:
    ax.grid(True)

# Mostrar la figura en Streamlit
st.pyplot(fig)

# Generar datos en forma de tabla
data_points = 10
sample_x = np.linspace(0, 2*np.pi, data_points)

if function_type == "seno":
    sample_y = amplitude * np.sin(frequency * sample_x + phase)
elif function_type == "coseno":
    sample_y = amplitude * np.cos(frequency * sample_x + phase)
else:  # tangente
    sample_y = amplitude * np.tan(frequency * sample_x + phase)
    sample_y = np.clip(sample_y, -10, 10)

# Crear y mostrar tabla de valores
data = {
    'x': sample_x,
    'y': sample_y
}
df = pd.DataFrame(data)
st.subheader("Tabla de valores")
st.dataframe(df.round(3))

# Añadir botón para descargar los datos
csv = df.to_csv(index=False)
st.download_button(
    label="Descargar datos como CSV",
    data=csv,
    file_name="datos_funcion.csv",
    mime="text/csv",
)
