# class Madre:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad =edad
#         #print("Me gusta hacer deportes")
#     #def cocinar(self):
#      #   print("La madre le gusta cocinar")

# class Padre:
#     def __init__(self, nombre, edad):
#         self.ojos = ojos
#         #print("El padre le gusta cocinar")

# class Hijo(Padre, Madre):  #importante el orden MRO (method resolution)
#     def __init__(self, nombre, edad, ojos, estudios):
#         Madre.__init__(self, nombre, edad)
#         Padre.__init__(self, ojos)
#         self.estudios = estudios
#         #super().__init__(nombre, edad)
#         #estudiar(self):
#         #print("estudio")

# jon = Hijo( "Jon", 32, "azules", "Programacion")
# jon.cocinar()
# print(jon.nombre)
# print(jon.edad)
# print(jon.ojos)
# print(jon.estudios)


######

class Direccion:
  def __init__(self, calle, ciudad):
      self.calle = calle
      self.ciudad = ciudad

  def mostrar(self):
      print(self.calle)
      print(self.ciudad)

class Persona:
  def __init__(self, nombre, email):
      self.nombre = nombre
      self.email= email

  def mostrar(self):
      print(self.nombre + ' ' + self.email)

# Agregar funcionalidad para usar la herencia múltiple
class Contacto(Direccion, Persona):
    def __init__(self, calle, ciudad,nombre, email, activo):
        Direccion.__init__(self, calle, ciudad)
        Persona.__init__(self,nombre, email)
        self.activo = activo
        
    def mostrar(self):
        Direccion.mostrar(self)
        Persona.mostrar(self)
        print(self.activo)


# Instanciar un contacto que es activo (True)
jon = Contacto('Jon', 'tugrp@example.com', 'Calle 1', 'Ciudad 1', True)  
jon.mostrar()


