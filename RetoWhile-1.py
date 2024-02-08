# Programa para solicitar edades de trabajadores y proporcionar comentarios sobre la edad.


repetir = "s"  # Inicialización del bucle principal
while repetir != "n":
    edad =int(input("Cuál es tu edad? "))
    if edad < 18:
        print("menor de edad")
    elif edad > 65:
        print("edad de jubilación")
    elif edad > 18:
        print("aceptable")
    else:
        print("aceptable")    
    repetir = input("Quieres continuar? (s, n) ")






