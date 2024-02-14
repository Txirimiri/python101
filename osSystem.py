import os

# print(os.getcwd())

# print(os.listdir())

# os.chdir("..") #("Python")

# print(os.getcwd())
 

os.mkdir("hola") #makes new folder
os.chdir("hola")#enters the new folder into directory
with open("filetest.txt", "w") as f: #creates new text file writing "hola" 
    f.write("hola")

