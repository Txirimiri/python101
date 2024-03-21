import streamlit as st
import pandas as pd

df2 = pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv")
st.data_editor(df2)




# st.title("Mi primer proyecto. A wee app by Kirstie.")
# st.write("Hola")
# st.markdown("##Hello")
# st.markdown("*Hello*")

# #streamlit run streamilt_app.py
# animales = ("dog", "cat", "bird")
# name = st.text_input('Introducir un animal')
# if name in animales:
#     st.write(f"El animal {name} existe")
# else:
#     if name:
#         st.write(f"El no animal {name} en la lista. ")

# def aplicarEdad(x):
#     return x - 5

# edad = st.number_input('¿Que edad tienes?')
# if st.button("click me"):
#     st.write(f"Tu edad es {aplicarEdad(edad)}")

# #if st.button("Click Me"):
#     #st.write(f"Tu edad es {edad - 5}")

st.markdown("# Calculadora")
num1 = st.number_input("Introducir el primer número",
            min_value=0, max_value=100)
num2 = st.number_input("Introducir el segundo número",
                       min_value=0, max_value=100)

oper = st.radio("Seleccionar una operacion:", ["Sumar", "Restar", "Multiplicar", "Divide"])
def resulta(x, y, op):
    if op =="Sumar":
        return x+y
    elif op == "Restar":
        return x-y
    else : return "No existe este opcion."


                     
#calculate button
if st.button("Calcular"): 
   st.write(f"The result is = {resulta(num1,num2,oper)}")

add_slider = st.sidebar.slider('Select a range of values',
        0.0, 100.0, (25.0, 75.0))

lenguages = ("Java", "C#" , "Python")
opcion = st.sidebar.selectbox("Seleccionar un lenguaje", lenguages)

if opcion:
    st.write(f"Has selecionado :v: {opcion}")
    
# streamlit run streamlit_app.py    