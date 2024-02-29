class Guitarra: 
    def __init__(self, marca, cuerdas=6): #abstraction (cuerdas=6) makes it default
       self.marca = marca
       self.cuerdas = cuerdas #attribute
       # print("Estoy vivo")
       self._precio = 100 

    def romperCuerdas(self, cuerdasRotas):
        if cuerdasRotas > self.cuerdas:
            self.cuerdas = 0
            print("no se puede romper mas de 6")
        else:
            self.cuerdas =self.cuerdas - cuerdasRotas
            print(f"Me he quedado con {self.cuerdas} cuerdas")

       
       
       
    def tocar(self):
        if self.cuerdas > 0:
            print("Toca una canción! y strum, strumm, strrrummmm") 
        else:
            print("Lo siento. No hay cuerdas. No suena. ")
       
       ###Main
            
guit =Guitarra("Les Paul", 6)
print(guit.cuerdas)
guit.romperCuerdas(4)
print(guit.cuerdas)
guit.tocar()