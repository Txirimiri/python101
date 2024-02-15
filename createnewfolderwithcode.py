# #import os
# sDirectory ="pruebas"
# print(os.getcwd())

# os.mkdir(sDirectory)#makes folder
# os.chdir(sDirectory)#

# print(os.getcwd())

#programa para crear un directorio 
#import os
#User_directory = input("Como se llama la carpeta")
#print(os.getcwd(User_directory))
 
#os.mkdir(User_directory)
#os.chdir(User_directory)
                                


New_directory= input("Como quieres llamar tu carpeta?")

if os.path.exists:
    print("No esta disponsible. Elige otro nombre.")

else:
    os.mkdir(New_directory)
    os.dir(New_directory)
    print(f"Tu nueva carpeta {New_directory} está lista" )

    with open("a.txt", "w") as f: 
    f.write("hola")
    with open("b.txt", "w") as f: 
    f.write("hola")



    



