import streamlit as st
from datetime import date
from datetime import datetime



count = 0
with st.form("My form", clear_on_submit=True):
    st.title("Soporte Tecnico")
    nombre = st.text_input('Nombre')
    problema = st.text_area('Problema')

    if st.form_submit_button("Agregar problema"):
        descripcion = nombre + " - " + problema + "- " + str(datetime.now()) #.strftime()("%d/%m/%Y"))
        with open ("problemas.txt", "a") as f:
         f.write(descripcion + "\n")
         st.write(f"Gracias {nombre}. Tu información ha sido registrada. Un técnico se pondrá en contacto contigo pronto.")

if st.button("Generar informe"):
    with open("problemas.txt", "r") as f: #creates text file
        st.write(f.readlines())

if "counter" not in st.session_state:
   st.session_state.counter=0

if st.button("Contar"):
   st.session_state.counter +=1

st.write(f"{st.session_state.counter} veces que pinchamos")


# s= """
# for i in range(10):
#     st.write(i)""" #in python print(i)

# exec(s) # to inject code

st.write(eval("10+10==20"))
st.write("Instructions :usar st.write() para imprimir :v: ")
codigo = st.text_area('Introducir codigo')

if codigo:
   exec(codigo)