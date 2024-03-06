class Vehiculo:
    def __init__(self, marca, modelo, color): 
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.averiado = False
    
    def conducir(self):
         print(f"Soy {self.marca} y vroom, vrooom, vrrooom.")

    def chocar(self, vehiculo=False):

        if self.averiado == True:
        print(f"¡Anda al mecánico!")
        else:
        self.averiado == vehiculo
        print()
        
            


class Camion(Vehiculo):
     def __init__(self, marca, modelo, color,  cabina):
        super().__init__(marca, modelo, color,)
        self.cabina = cabina

    def dormir()









