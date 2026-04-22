import streamlit as st
import random

st.title("09 - Ejercicios de Streamlit")

st.subheader("Ejercicio 1: Saludo Simple")
nombre = st.text_input("Escribe tu nombre:")
if nombre:
    st.write(f"¡Hola, {nombre}!")
st.divider()

st.subheader("Ejercicio 2: Calculadora de Producto")
num1 = st.number_input("Primer número:", value=0.0, key="num1")
num2 = st.number_input("Segundo número:", value=0.0, key="num2")
st.write(f"Resultado de la multiplicación: **{num1 * num2}**")
if num1 > 100 or num2 > 100:
    st.warning("Números grandes")
st.divider()

st.subheader("Ejercicio 3: Convertidor de Temperatura (Radio Buttons)")
direccion = st.radio(
    "Selecciona la dirección de conversión:",
    ["Celsius a Fahrenheit", "Fahrenheit a Celsius"]
)
temp = st.number_input("Ingresa la temperatura:", value=0.0, key="temp")
if direccion == "Celsius a Fahrenheit":
    resultado = (temp * 9 / 5) + 32
    st.write(f"{temp} °C = **{resultado:.2f} °F**")
else:
    resultado = (temp - 32) * 5 / 9
    st.write(f"{temp} °F = **{resultado:.2f} °C**")
st.divider()

st.subheader("Ejercicio 4: Galería de Mascotas (Tabs)")
tab_gatos, tab_perros, tab_aves = st.tabs(["Gatos", "Perros", "Aves"])

with tab_gatos:
    st.image("https://i.pinimg.com/736x/8b/fc/bc/8bfcbc0ba42c4d27310a7ee297b39de7.jpg", width=300)
    if st.button("Me gusta", key="like_gato"):
        st.toast("Te gusta esta mascota")

with tab_perros:
    st.image("https://i.pinimg.com/736x/c8/76/36/c87636c633fd0a685c8ff015ba214840.jpg", width=300)
    if st.button("Me gusta", key="like_perro"):
        st.toast("Te gusta esta mascota")

with tab_aves:
    st.image("https://i.pinimg.com/736x/49/4d/d0/494dd0c2b6ebdcdce6c69d0a637a7c65.jpg", width=300)
    if st.button("Me gusta", key="like_ave"):
        st.toast("Te gusta esta mascota")
st.divider()

st.subheader("Ejercicio 5: Caja de Comentarios (Formulario)")
with st.form("formulario_comentarios"):
    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")
    enviado = st.form_submit_button("Enviar")

if enviado:
    if mensaje:
        st.json({"asunto": asunto, "mensaje": mensaje})
    else:
        st.warning("El mensaje no puede estar vacío.")
st.divider()

st.subheader("Ejercicio 6: Login Simulado (Session State)")
if "logueado" not in st.session_state:
    st.session_state.logueado = False

if not st.session_state.logueado:
    usuario = st.text_input("Usuario:", key="login_user")
    contrasena = st.text_input("Contraseña:", type="password", key="login_pass")
    if st.button("Ingresar"):
        if usuario == "admin" and contrasena == "1234":
            st.session_state.logueado = True
            st.success("¡Bienvenido, admin! Has iniciado sesión correctamente.")
        else:
            st.error("Usuario o contraseña incorrectos.")
else:
    st.success("Ya estás logueado como admin.")
    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.rerun()
st.divider()

st.subheader("Ejercicio 7: Lista de Compras (Session State)")
if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

producto = st.text_input("Ingresa un producto:", key="producto_input")
col1, col2 = st.columns(2)
with col1:
    if st.button("Agregar"):
        if producto:
            st.session_state.lista_compras.append(producto)
with col2:
    if st.button("Limpiar Lista"):
        st.session_state.lista_compras = []

if st.session_state.lista_compras:
    st.write("**Lista de productos:**")
    for i, item in enumerate(st.session_state.lista_compras, 1):
        st.write(f"{i}. {item}")
else:
    st.info("La lista está vacía.")
st.divider()

st.subheader("Ejercicio 8: Gráfico Interactivo")
n = st.slider("Selecciona N (cantidad de números):", min_value=10, max_value=100, value=20)
datos = [random.uniform(0, 100) for _ in range(n)]
st.line_chart(datos)
if st.button("Regenerar"):
    st.rerun()