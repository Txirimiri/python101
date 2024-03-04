class Vehiculo:
    def __init__(self, marca, modelo, color, ruedas): 
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas 
    
    def conducir(self):
         print(f"Soy {self.marca} y vroom, vrooom, vrrooom.")

    def chocar(self):
         print(f)


class Camion(Vehiculo):
     def __init__(self, marca, modelo, color, ruedas, cabina):
        super().__init__(marca, modelo, color, ruedas)
        self.cabina = cabina

    def dormir()









