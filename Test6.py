""" import random 

cartas = ["a", "b", "c", "d"]
opcion = random.choice(cartas)
print(opcion)


x= random.shuffle(cartas)
print(cartas)  """

""" 
from datetime import datetime

hoy = datetime.now()
print(hoy.day)
print(hoy.month)
print(hoy.year)
print(hoy.hour)
print(hoy.second) """
""" 
import datetime 

s= datetime.datetime.strptime("2012/01/17", "%Y/%m/%d")
print(s.month)
print(s)
#d = datetime.datetime(2021, 12, 1) """

import webbrowser
webbrowser.open("http://www.google.com")

import subprocess
completed = subprocess.run(["ls"],capture_output=True, text= True)
print(completed)