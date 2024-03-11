# frutas = ["MANZANA", "pera", "NARANJA", "uva", "MELON"] #list comprehension

# #nuevas_frutas = [fruta.lower() for fruta in frutas if fruta.isupper()] 
# nuevas_frutas = [fruta.lower() for fruta in frutas if fruta.isupper()] ##

# nuevas_frutas =[]

# for fruta in frutas:
#     if fruta.isupper():
#         nuevas_frutas.append(fruta)
        
# print(nuevas_frutas)



# print(nuevas_frutas)


numeros = [3, 54, -12, 4, -67, 99,-120]

#todos =["Par" if i%2==0 else "Impar" for i in numeros]
#print(todos)


listaPositivos = [i for i in numeros if i >=0]
print (listaPositivos)

#bucle 1st is bucles, assign new list