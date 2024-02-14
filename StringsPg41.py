correos = ["jon.smith@microsoft.com","maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
listadeNombres= []
listadeDominios = []
for c in correos:
    nombre, dominio = c.split("@")
    listadeNombres.append(nombre) 
    listadeDominios.append(dominio)
    print(nombre)
    print(dominio)

sTexto = sTextp
 
 #Informe
sTexto =""
for i in listadeNombres:
    sTexto= sTexto + i + "," 
    print(sTexto)

with open("informe.txt, "w") as f:
    f.write(sTexto)
