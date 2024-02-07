""" x = 199
print(id(x))

y = 175
print(id(y)) """
""" 
x = ["hola", 4, 5]
print(type(x))
print(id(x))
x[0]="Agur"
print(id(x)) """
""" 
x = ["hola", 4, 5]
print(type(x))
print(isinstance(x,int)) """

""" x = input("Introducir algo")

if isinstance(x, int):
    print(int(x * 2))
else:
    print("es otra cosa") """

""" 
#para conmfirmar que tipo de data
inflacion = float(3.765)
print(type(inflacion))
print(id(inflacion)) """

""" #imprimr la suma de todos integers
a = 5
b = 4.32
c = 10

suma =0 
if isinstance(a, int):
    suma +=a # suma suma= suma + a
if isinstance(b, int):
    suma +=b        
if isinstance(c, int):
    suma +=c


print(suma)


a = 5
b = 4.32
c= 10
lista = [a,b,c,]
suma= 0 """
""" 
#bucles
i = 0
while i < 10:
    print("hola" + str(1))   
    i = i+1
 """
x= 0
while x < 10:
    x = x + 1
    if x == 5:
        print("x is 5")
        continue
    print(x)
else:
    print("else")                                                   
