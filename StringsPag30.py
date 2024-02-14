#texto = "programazioa gustatzen gustatzen zait."

#print("X + texto.strip() + "X")
#print("X" + textos.rstrip()+ "X")
#print(texto.count( "gustatzen"))
#print(texto[5:]) #shows text from 0-5 character
#print(texto[5:10])# does not include 10th character. showing between 5 and 10 [5:10]
#print(texto [-5:])#counts from end of string

#pagina 40
#s= " 122,Python,es,64,un,777,lenguaje,222,de,55,66,programación "

#s= s.strip("") #para quitar los espacios
#listaString = s.split(",") #para quitar commas
#listaDePalabras =[]
#print(listaString)
#print("a" + s+ "b")
#for i in listaString: #bucle
 #   if i.isnumeric():
    #    print(i)
     #   listaDePalabras.append(i)

#resultado = " ".join(listaDePalabras)
#print(resultado)
#print(listaString)        
""" 
###pagina 40
s= " 122,Python,es,64,un,777,lenguaje,222,de,55,66,programación "
s =s.strip()
listaString = s.split(",")
listaDePalabras =[]
for i in listaString:
    if not i.isnumeric():
        listaDePalabras.append(i)
print(listaDePalabras)
resultado = " ".join(listaDePalabras)
print(resultado) """

#Lo que quieres conseguir es lo siguiente output: Pagina 41
#Python es un lenguaje de programación
#PYTHON ES UN LENGUAJE DE PROGRAMACIÓN
#Python Es Un Lenguaje de Programación

""" s= "122,Python,es,64,un,777,lenguaje,222,de,55,66,programación"
s =s.upper() ###
listaString = s.split(",")
listaDePalabras =[]
for i in listaString:
    if not i.isnumeric():
        listaDePalabras.append(i)
print(listaDePalabras)
resultado = " ".join(listaDePalabras)
print(resultado)



s= "122,Python,es,64,un,777,lenguaje,222,de,55,66,programación"
s = s.title()###
listaString = s.split(",")
listaDePalabras =[]
for i in listaString:
    if not i.isnumeric():
        listaDePalabras.append(i)     
print(listaDePalabras)
resultado = " ".join(listaDePalabras)

print(resultado)
 """

###Pagina 41
long_string "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
s
s= s.replace("Bill Gates", "Guido Van Rossum")
s= s.replace()