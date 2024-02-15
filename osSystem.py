#import os

# print(os.getcwd())

# print(os.listdir())

# os.chdir("..") #("Python")

# print(os.getcwd())
 
 #os.rmdir()
####repaso 
import os

os.getcwd() # where you are currently working: get working directory
d1 = "dir1"
d2 = "dir2"
d3 = "dir3"
f= "abc.txt"

s= os.path.join(d1,d2,d3,f)
print(s)
os.mkdir(s)
#dir1\dir2\dir3\abc.txt


os.chdir("dir1") #change path directory, store it in a different place:change directory


#with open ("file.txt", "r") as f:
 #   f.write(sTexto)
#os.mkdir("hola") #makes new folder
#os.chdir("hola")#enters the new folder into directory
#with open("filetest.txt", "w") as f: #creates new text file writing "hola" 
 #   f.write("hola")

os.path.exist() #to see if path already exists


    for f in os.listdir():
        print(os.path.splitext(f)) #('test5', ',py)
        x,y =os.path.splitext