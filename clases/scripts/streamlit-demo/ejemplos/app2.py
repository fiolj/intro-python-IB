import streamlit as st
import pandas as pd

st.title("Trabajando con tablas en Streamlit")

# Texto con diferentes formatos
st.markdown("## Ejemplo de texto con diferentes formatos")
st.write("Este es un texto normal")
st.markdown("**Este texto está en negrita**")
st.markdown("*Este texto está en cursiva*")
st.markdown("## Este es un encabezado H2")

# Oootra vez con Harry Potter
data = {
    "Titulo": [
        "La piedra filosofal",
        "La cámara secreta",
        "El prisionero de Azkaban",
        "El cáliz de fuego",
        "La orden del Fénix",
        "El misterio del príncipe",
        "Las reliquias de la muerte"
    ],
    "Año de edición": [1997, 1998, 1999, 2000, 2003, 2005, 2007],
    "Páginas": [223, 251, 317, 636, 766, 607, 607],
}

df = pd.DataFrame(data)
# Ojo que lo siguiente funciona como en los notebooks:
#df

df = pd.DataFrame(data)

# Mostrar el DataFrame
st.subheader("Tabla de ejemplo:")
st.dataframe(df)

# Tabla estática
st.subheader("Tabla estática:")
st.table(df)