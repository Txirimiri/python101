# paises = {"Australia": "Canberra", "España": 123}

# print(paises)
# print(type(paises))
# print(dir(paises))

# print(paises.get("Australia"))

# print(paises["Australia"]) #This is similar to .get, but it uses parentheses instead

# paises.update({"España": "Madrid"})
# print(paises)

# paises.update({"Mexico": "Ciudad de Mexico"}) 
#The .update method is used to insert another key/value pair into a dictionary or to change the value associated with an existing key
# paises.pop("España") # .pop es para borrar y escribir el key
# print(paises)
# paises.popitem()  # quita el ultimo
# print(paises)

# for k, v in paises.items():
#     print (k, v)
    
# for k in paises.keys():
#     print (k)

# for v in paises.values():
#     print(v)

# print(paises)

# user1 = {"email": "che@gmail.com", "nombre": "Che"}
# user2 = {"email": "ane@gmail.com", "nombre": "Ane"}

# users = [user1, user2]

# for i in users:
#     print(i)
#     print(i["nombre"])
    # print(type(i))


## Ejercicio 1.a

# coche1 = {"modelo": "Hunday", "color": "blanco"}
# print(coche1)

# coche1.update({"años": 5})
# print(coche1)

# coche1.pop("modelo")
# print(coche1)
    

## Ejercicio 1.b

# coche1 = {"modelo": "Hunday", "color": "blanco"}
# coche2 = {"modelo": "Renoult", "color": "rojo"}

# coches = (coche1, coche2)
# print(coches)

# for i in coches:
    # print(i["modelo"])

## Ejercicio 2

# pedido = {}

# for i in range(3): # because they require three users
#     i = i + 1
#     usuario = input("¿Cuál es tu nombre?")
#     comida = input("Cuál es tu comida favorita?")
#     pedido.update({usuario: comida}) I use the .update method and place it within curly braces {} without using quotes because that's where I want to store the values I receive

# print(pedido)

# for k, v in pedido.items():
#     print(k, v)

pedido = {}

intencion = input("¿quieres hacer un pedido? SI/NO ")

while intencion == "SI": 
    usuario = input("¿Cuál es tu nombre? ")
    comida = input("¿Qué comida quieres pedir? ")
    pedido.update({usuario: comida})
    intencion = input("¿Quieres pedir algo más? SI/NO ")

print(pedido)







s = "Hola, Agur, Hi, Bye, goodbye"
res = s.split(",")
print(res)
if "hola" in s.lower:
    print("Esta")

i = s.find("Hi")


