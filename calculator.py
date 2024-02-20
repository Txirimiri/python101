#caluclator app
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero"
    
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = input("Do you want to add, subtract, multiply, or divide? ")

if op == "add":
    result = add(n1, n2)
elif op == "subtract":
    result = subtract(n1, n2)
elif op == "multiply":
    result = multiply(n1, n2)
elif op == "divide":
    result = divide(n1, n2)
else:
    result = "Not a valid operation"

print("Result:", result)


 

    
