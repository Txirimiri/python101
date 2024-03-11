import sqlite3

conn = sqlite3.connect('movies.db')

conn.execute("CREATE TABLE Movies (id integer, titulo, año)")

#conn.close()



cur = conn.cursor()