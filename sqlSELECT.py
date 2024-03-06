import sqlite3

conn =sqlite3.connect('pelis.db')

cur = conn.cursor()

cur.execute("SELECT * FROM Peliculas;")

rows = cur.fetchall()

for row in rows:
    #print(type(rows)) #(2, 'Indiana Jones', 2)
    print(row[COL_DURACION])
conn.close()