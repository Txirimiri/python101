# Programa para solicitar edades de trabajadores y proporcionar comentarios sobre la edad.


repetir = "s"  # Inicialización del bucle principal

while repetir != "n": # Bucle principal para solicitar edades
    edad =int(input("Cuál es tu edad? "))
    if edad < 18:
        print("menor de edad")
    elif edad > 65:
        print("edad de jubilación")
    elif edad > 18:
        print("aceptable")
    else:
        print("aceptable")  
# Preguntar si el usuario quiere continuar         
    repetir = input("Quieres continuar? (s, n) ")                 

 




