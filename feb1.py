""" x = 45.674
y = int(x)
print(y) """
""" 
loggedIn = False
print(int(loggedIn)) """

""" a = {10, 20, 30, 40}
b = { 30,40, 50, 60}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
 """
""" 
#Cambiar el código para preguntar al usuario por los valores para guardar del set pg.19
a = int(input("Dime un numero, por favor"))
b = set()
b.add(a)
print(b) """





""" #pagina 20 Python 101
developers = {'Maria','Pedro'}
empleados = {'Maria','Pedro','Jon', 'Henry'}
gym = {'Jon', 'Maria','Henry'}

print(empleados.difference(developers,gym))
print(gym.intersection(developers))

 """

""" #pagina 21 Python 101
listaRespuestas = [10, 20, "Agur", "Agur", "agur, 10, 50"]
setRespuestas = set(listaRespuestas)
print(setRespuestas) """

""" x = 23.4567
print(f"{x:.2f}") """
""" 
s = "Python es genial!"
print("Python" in s)


s = "Python es mi favorito!"
print("Python" in s) """

""" #lista de compras
compra = ["manzana", "platanos", "kiwis"]
print(compra [0] )
print(len(compra))
compra.append("mango")
compra.remove("manzana")
print(compra)


for i in compra: 
    print("Fruta es" + i)
    if i == "platano": 
        print("Frutas es" + i)
    else:
        print("No es platano")

        print("END")
 """
""" 
compra = ["manzana", "platanos", "kiwis"]
 compra.sort()
print(compra)
compra.reverse()
print(compra) 
compra.pop()
print(compra) """

""" 
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s) """







#pagina 24
compra = ["manzana", "platanos", "kiwis"]
print(compra)
print(len(compra))
print (compra[1])
print (compra [2])
compra.append("zumo")
compra.append("galletas")
print()