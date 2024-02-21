###list loop example
#numeros = [1, 5, 6, 2]
#for i in numeros:
#    print(i)

###elif example
#a = 33
#b = 33
#if b > a:
#  print("b is greater than a")
#elif a == b:
#  print("a and b are equal")

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.

### 7 ways to loop in Python 
#1. A Simple for Loop
#2. List Comprehension
#3.A for Loop with range()
#4. A for Loop with enumerate()
#5. A for Loop with lambda
#6. A while Loop
#7. The NumPy Library


###1. simple "for LOOP" fruits = ["Apple", "Mango", "Banana", "Peach"]
#for fruit in fruits:
#  print(fruit)

###2. List Comprehension
#fruits = ["Apple", "Mango", "Banana", "Peach"]
#[print(fruit + " juice") for fruit in fruits]

###3. A for loop with range
#range(start, stop, step)
#fruits = ["Apple", "Mango", "Banana", "Peach"]

#fruits = ["Apple", "Mango", "Banana", "Peach"]
 
# Constructs range object containing elements from 0 to 3
#for i in range(len(fruits)):
#  print("The list at index", i, "contains a", fruits[i])
## result
#The list at index 0 contains a Apple
#The list at index 1 contains a Mango
#The list at index 2 contains a Banana
#The list at index 3 contains a Peach

###A slightly different approach would be to print only some of the fruits based on their index. We’d do this by specifying the starting and ending index for the for loop using the range() function:

#fruits = ["Apple", "Mango", "Banana", "Peach"]
 
# Constructs range object containing only 1 and 2
#for i in range(1, 3):
#  print(fruits[i])
#Here’s the output:
#Mango
#Banana
##As we asked, it’s returned only those fruits at index 1 and 2; remember, 3 is the stopping point, and 0 is the first index in Python.

###4. A for Loop with enumerate()
#fruits = ["Apple", "Mango", "Banana", "Peach"]
 
#for index, element in enumerate(fruits):
#  print(index, ":", element)
##Running the above code returns this list of the elements and their indexes:
#0 : Apple
#1 : Mango
#2 : Banana
#3 : Peach

####5. A for Loop with lambda
##Python’s lambda function is an anonymous function in which a mathematical expression is evaluated and then returned. As a result, lambda can be used as a function object. Let’s see how to use lambda as we loop through a list.
##We’ll make a for loop to iterate over a list of numbers, find each number's square, and save or append it to the list. Finally, we’ll print a list of squares. Here’s the code:
#lst1 = [1, 2, 3, 4, 5]
#lst2 = [] 
# Lambda function to square number
#temp = lambda i:i**2
#for i in lst1:
     # Add to lst2
#    lst2.append(temp(i))
#   print(lst2)
##We use lambda to iterate through the list and find the square of each value. To iterate through lst1, a for loop is used. Each integer is passed in a single iteration; the append() function saves it to lst2.

#We can make this code even more efficient using the map() function:

#lst1 = [1, 2, 3, 4, 5]
   
#lst1 = list(map(lambda v: v ** 2, lst1))
   
#print(lst1)
#After applying the provided function to each item in a specified iterable, map() produces a map object (which is an iterator) of the results.

#Both these codes give the exact same output:

#[1, 4, 9, 16, 25]

###6. A while Loop
##We can also iterate over a Python list using a while loop. This is one of the first loops beginning programmers meet. It's also one of the easiest to grasp. If you consider the name of the loop, you'll soon see that the term "while" has to do with an interval or time period. The term "loop" refers to a piece of code that is executed repeatedly. So, a while loop executes until a certain condition is met.
##In the code below, that condition is the length of the list; the i counter is set to zero, then it adds 1 every time the loop prints one item in the list. When i becomes greater than the number of items in the list, the while loop terminates. Check out the code:

#fruits = ["Apple", "Mango",  "Banana", "Peach"]
 
#i = 0
#while i < len(fruits):
#  print(fruits[i])
#  i = i + 1
##Can you guess what the output will be?
#Apple
#Mango
#Banana
#Peach
##It is important to note the i = i + 1 in the code above can also be shortened as i += 1.
##Our code ensures that the condition i < len(fruits) will be satisfied after a certain number of iterations. Ending while loops properly is critical; you can learn more about HOW TO END LOOPS IN PYTHON HERE.

###7. The NumPy Library
##The methods we’ve discussed so far used a small lists. However, efficiency is essential when you’re working with larger amounts of data. Suppose you have large single-dimensional lists with a single data type. In this case, an external library like NumPy is the best way to loop through big lists.
#NumPy reduces the overhead by making iteration more efficient. This is done by converting the lists into NumPy ARRAYS. As with lists, the for loop can also be used to iterate over these arrays.
##It is important to note that the method we present here can only be used for arrays of single data types.

#import numpy as np
 
#nums = np.array([1, 2, 3, 4, 5])
 
#for num in nums:
#  print(num)
#Running the code above gives the following output:
#1
#2
#3
#4
#5
###Although we’ve used for num in nums: for its simplicity in this example, it’s usually better to use for num in np.nditer(nums): when you’re working with large lists. The np.nditer function returns an iterator that can traverse the NumPy array, which is computationally more efficient than using a simple for loop.


#numbers divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

 # Create an empty list to store numbers that meet the given conditions
nl = []

# Iterate through numbers from 1500 to 2700 (inclusive)
for x in range(1500, 2701):
    # Check if the number is divisible by 7 and 5 without any remainder
    if (x % 7 == 0) and (x % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
        nl.append(str(x))

# Join the numbers in the list with a comma and print the result
print(','.join(nl))       

#2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius
        



        
 #3. Write a Python program to guess a number between 1 and 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.       