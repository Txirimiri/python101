from dataclasses import dataclass, astuple
import sqlite3

@dataclass
class Peliculas:
    id : int
    nombre : str
    duracion : float

conn = sqlite3.connect('pelis.db')
cursor = conn.cursor()

nombre = input("Cual es el titulo? ")
duracion = input("Cuanto dura la peli?")
p = Peliculas(-1, nombre, duracion)

cursor.execute("INSERT INTP PELICULAS(nombre, duracion) VALUES(?,?);", astuple)
conn.commit() #default not auto commit

conn.close()


