
 #input(int("Please enter two numbers: ")
      
#num1 = 
#num2 = 




n1=int(input("Introducir un numero?"))
n2= int(input("Introducir otro numero"))
op = input("Do you want to add, subtract, multiply or divide?")


def calculate_answer(n1, n2, op):
    if op == "subtract":
        return n1 - n2
    elif op == "add":
        return n1 + n2
    elif op == "multiply":
        return n1 * n2
    elif op == "divide":
        return int(n1 / n2)
    else:
        return "Not a valid operation"
    

#import matbasic


    ###if __name__=="__main__" double under
    
