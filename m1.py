productos = ["raqueta", "balon" , "guantes", "pelota"]

#captext = lambda x:x.capitalize()
#print(captext("raqueta"))

#1. crear una funcion para convertir la primera letra mayúscula
def convertir_may(s):
    return s.capitalize()

map(convertir_may,productos)

print(list(map(convertir_may, productos)))
print(list(map(lambda x:x.capitalize(), productos)))

#2. aplicarla a todos los elementos de la lista

for p in productos:
    print(convertir_may(p))

productos = ["raqueta", "balon" , "guantes", "pelota"]
nuevap = [convertir_may(p)] 


#productos = ["Raqueta", "Balon", "Guantes", "Pelota"] RESULT

#ejercicio 1: sumar 2 a cada elemento de la lista [4, 5, 6] = [6, 7 , 8]



import math
number_list = [4, 5, 6]
print(list(map(lambda x: x+2, number_list)))

def calc(x):
    return x + 2

print(list(map(calc, number_list)))

#ejercicio 2: import math para aprovechar de la función math.sqrt
import math

x = tuple(map(math.sqrt, number_list))
print(x)

#ejercicio 3: teniendo 3 listas de números, multiplicar cada numero

x = [4, 5, 6]
y = [6, 7 , 8]
z=  [8, 1, 2]

lambda x,y,z:x*y*z

print(tuple(map(lambda a, b, c: a*b*c, x, y, z)))