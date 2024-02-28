class Guitarra: 
    def __init__(self, marca, cuerdas): #abstraction (cuerdas=6) makes it default
       self.marca = marca
       self.cuerdas = cuerdas #attribute
       # print("Estoy vivo")
       self._precio = 100 #this code tells other programmers this should remain private
       
    def tocar(self): #other method
        #if...while
        print(f"Soy {self.marca} y strum, stttrrrum, struuuum")
    
    
    def __str__(self):
        return f"Hola Guitarra {self.marca}" #dunder method

#main programa - instancia /usar de la clase

nombre = input("Cual es el nombre de la guitarra?")
guit1 = Guitarra("Les Paul", 6)
print(guit1.marca)
print(guit1.cuerdas)
print(guit1._precio)
bajo = Guitarra("Bajo sencillo",4)
bajo.cuerdas=5 #get and set
print(bajo.cuerdas)
guit1.tocar() #other method
guit1 = Guitarra ("Les Paul")
print(guit1.cuerdas)

bajo= Guitarra("Les Paul", 4)
print(bajo)


