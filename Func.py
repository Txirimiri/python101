





print(11%3) #3 r 2
print(10%3) #3, 4 1
print(10%2)

def IsPar(x):
    if x % 2 == 0:
        return 0 #("Par")
    else:
        return 1 #("Impar")
print(IsPar (10)==1)


#con una lista, encuentra el número maximo y mínimo

#lista = [1,4,3,6,9,7]

#def minmax(lista):
    #return min(lista), max(lista) #option 1


#def minmax2(*args):
    #return min(args), max(args) #option 2


#x, y = minmax(lista)
#print(max(lista))
#print(min(lista))
#print(x,y)

#En una línea de texto, encuentra la palabra más larga. Por ejemplo, “Me gustan los garbanzos” devuelve “garbanzos”.

texto = "Me gustan los garbanzos."  #use if
def encontrarPalabra(texto):
    palabras = texto.split()
    max_len =0
    max_palabra = ""

    for palabra in palabras:
        if len(palabra) > max_len:
            max_len = len(palabra)
            max_palabra = palabra

    return max_len, max_palabra

texto = "Me gustan los garbanzos."
print(encontrarPalabra(texto))