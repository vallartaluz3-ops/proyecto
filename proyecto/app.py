import streamlit as st
import random

st.markdown("""
<style>

.main {
    background-color: #f5f5f5;
}

.pedido {
    animation: mover 2s infinite;
}

@keyframes mover {
    0% {transform: translateX(0);}
    50% {transform: translateX(10px);}
    100% {transform: translateX(0);}
}

</style>
""", unsafe_allow_html=True)
import streamlit as st
import random
import time

from estructuras.cola import Cola
from estructuras.pila import Pila
from simulacion.pedido import Pedido
from simulacion.cocina import Cocina

if "cola" not in st.session_state:
    st.session_state.cola = Cola()

if "pila" not in st.session_state:
    st.session_state.pila = Pila()

if "contador" not in st.session_state:
    st.session_state.contador = 1

if "cocina" not in st.session_state:

    cocina = Cocina(
        st.session_state.cola,
        st.session_state.pila
    )

    cocina.daemon = True
    cocina.start()

    st.session_state.cocina = cocina

st.title("🍔 Fast Food Simulator")

combos = [
    "Hamburguesa",
    "Pizza",
    "Hot Dog",
    "Nuggets",
    "Combo Familiar"
]

if st.button("Generar Pedido"):

    combo = random.choice(combos)

    pedido = Pedido(
        st.session_state.contador,
        combo
    )

    st.session_state.cola.encolar(pedido)

    st.session_state.contador += 1

st.subheader("🧍 Cola de Espera")

for pedido in st.session_state.cola.ver():
    st.info(str(pedido))

st.subheader("👨‍🍳 Preparando")

actual = st.session_state.cocina.pedido_actual

if actual:
    st.warning(str(actual))
else:
    st.success("Esperando pedido")

st.subheader("✅ Pedidos Listos")

for pedido in reversed(st.session_state.pila.ver()):
    st.success(str(pedido))

time.sleep(1)
st.rerun()