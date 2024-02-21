#Crear una función para comprobar la edad de un usuario antes de que entre en una web para adultos. Si es menor a 18, devolver False.  
def verify_query(age):
   
    if age >=18:
        return "You are of legal age to enter. "
    else: 
        return "Sorry, you will to have to wait until you are 18."



###Main---------
user_age = int(input("Check to see if you can access this site. How old are you? "))
print(verify_query(user_age))