import sqlite3

print("Programa de BD")

conn= sqlite3.connect("pelis.db") #print("Programa de BD")

#cur = conn.cursor()
# conn.execute("CREATE TABLE Peliculas(id integer PRIMARY KEY AUTOINCREMENT, nombre text, ")

while True:
    
    accion = int(input("Qué quieres hacer? 1. SELECT, 2. INSERT, 3. UPDATE, 4. DELETE "))
    
    if accion == 1:
        #mostrar todas las pelis
        sSQL = "SELECT * FROM Peliculas"
        cur = conn.cursor()
        cur.execute(sSQL)
        filas = cur.fetchall()
        for fila in filas:
            print(fila)
    elif accion == 2:
        nombre = input("Cual es el nombre? ")
        duracion = float(input("Cuánto dura la peli? "))
        cur = conn.cursor()
        sSQL = "INSERT INTO Peliculas (nombre, duracion) VALUES (?,?)"
        cur.execute(sSQL, (nombre, duracion))
        conn.commit()
    elif accion == 3: #UPDATE
        id= (input("Qué película desea eliminar?"))
        duracion = input("Qué duracion tiene?") 
        cur = conn.cursor()
        sSQL = "UPDATE Peliculas SET duracion = ? WHERE id = ?"
        cur.execute("DELETE desde Peliculas Where id =?")
    elif accion == 4:
        break
    elif accion == 5:
        print("cerrando")
        conn.close()
        break
    

