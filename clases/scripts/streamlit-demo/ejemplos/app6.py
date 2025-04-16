import streamlit as st

# Título de la aplicación
st.title("Interacciones con botones en Streamlit")

# Estado inicial de la página
if "nota" not in st.session_state:
    st.session_state.nota = 0

if "mensaje" not in st.session_state:
    st.session_state.mensaje = "¡Presiona un botón para comenzar!"

# Funciones para manejar los botones
def incrementar():
    st.session_state.nota += 1
    st.session_state.mensaje = "¡Has incrementado la nota!"

def decrementar():
    st.session_state.nota -= 1
    st.session_state.mensaje = "¡Has decrementado la nota!"

def reiniciar():
    st.session_state.nota = 0
    st.session_state.mensaje = "La nota ha sido reiniciada."



# Mostrar el estado actual
st.write(f"**Nota actual:** {st.session_state.nota}")
st.write(f"**Mensaje:** {st.session_state.mensaje}")

# Botones para interactuar
col1, col2, col3 = st.columns(3)

with col1:
    st.button("Incrementar", on_click=incrementar)

with col2:
    st.button("Decrementar", on_click=decrementar)

with col3:
    st.button("Reiniciar", on_click=reiniciar)


# Mostrar un mensaje adicional basado en el valor del nota
if st.session_state.nota > 10:
    st.warning("¡La nota es mayor que 10!")
elif st.session_state.nota == 10:
    st.image("https://media1.tenor.com/m/f3_kfNdFAb0AAAAC/leonardo-dicaprio-clapping.gif")
elif st.session_state.nota >= 6:
    st.success("¡Aprobado!")
elif st.session_state.nota < 6 and st.session_state.nota > 0:
    st.error("¡Reprobado!")
elif st.session_state.nota < 0:
    st.warning("¡La nota es negativa!")
else:
    st.info("La nota está en el rango correcto.")

# Botón para mostrar un mensaje adicional
if st.button("Mostrar saludo"):
    st.session_state.mensaje = "¡Hola! Qué nota me pongo?."