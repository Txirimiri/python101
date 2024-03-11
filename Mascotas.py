class Animal:
    def __init__(self, nombre, pelo, cola, patas,caracter):
        self.nombre = nombre
        self.pelo = pelo
        self.cola = cola
        self.patas = patas
        self.caracter = caracter
        

class Gato(Animal):
    def __init__(self, nombre, pelo, cola, caracter, patas, bigotes):
        super().__init__(nombre, pelo, cola, caracter, patas)
        self.bigotes = bigotes

        def hablar(self):
            print
class Perro(Animal):
    def __init__(self, nombre, pelo cola, caracter, patas, dog_breath)
        super().__init__(nombre, pelo, cola caracter, patas)
        self.dog_breath = dog_breath
if __name__=="__main__":
    listaAnimals = [Gato("felix"), Perro("Sam", "salchicha")]

    for animal in listaAnimals:
        animal.hablar()