class Bebida:
    def __init__(self, tipo:str, volumen:int, cantidad:float):
            self.tipo = tipo
            self.volumen = volumen
            self.cantidad = cantidad

    def beber(self, ):
        print(f"Quiero ordenar {self.tipo} y en {self.cantidad}")

    

##### Main program

#Crear lista para almacenar las bebidas
listaBebidas =[]


#preguntar a 3 usuarios

for i in range(3):
    tipo = input("Qué quieres tomar? ")
    cantidad= input("Cuanto vas a beber ahora (0 a 100)? ")
    
    bebida = Bebida(tipo) #---agregar la bebida a la lista 
    listaBebidas.append(bebida)
    print(listaBebidas)


#imprimir todas las bebidas

    