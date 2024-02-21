
#lenguaje = input("Cual es tu lenguaje de programacion favorito?")

#match lenguaje: 
 #       case "Python":
  #          print("A mi me gusta Python tambien")
   #    case "Java"  "Javascript":
 #       print("Bueno, bastante complicado...")   
    #    case ("Bueno, JS es bastante complicado...") #case "Java" | "Javascript"
     #   case _:
      #      print(f"No tengo conocimento de este {lenguaje}")             

#car test could be for voice control
comando = inut("Enter a command for the car")

match comando:
    case "start":
        print("The car has started")
    case "stop":
        print("The car has stopped")
    case "quit":
        print("Game Over")
