# com411
Work from Problem Solving Through Programming (COM411)

## Week 1: 
Revision of various python functions, variables, and operators.

```python
print() #This is a print function, outputs the contents to the user
input() #This is an input function, allows for user input

name = #This is a variable, allows for the storing and if desired editing of data

int() #This is a integer function, converts variables into integers using this function, stores whole numbers
str() #This is a string function, converts variables into strings using this function, stores words / letters
float() #This is a float function, converts variables into floats using this function, can store negatives and positives aswell as decimal places
```
## Week 2: 
Revision of If statements, elif, else, while loops, modulo operators, 

```python
#simple python if and elif statements used
num = input("Enter num: ")

if (num > 5):
    print("wow big num")
elif (num != int):
    print("well well well")
else:
    print("small")

#to find an odd number
if (num % 2 != 0):

#range
#range generates a range of numbers
# - start index (included)
# - end index (Excluded)
# - step difference (difference)
#demonstration of a For loop
for value in range(1, 10, 1):
    print (value)
#for loop
for character in name:
    print (character)
#for loops go through a specific amount of steps or elements

#nesting - putting one code block in another (for loop in an if statement, while inside a for)
print ("please enter your name")
name = input()

if (len(name) < 6):
    for character in name:
        print (character)
else:
    print("you have a long name")
```



## Week 3

```python
#All the built in functions in PYTHON 
abs()	
delattr()	
hash()	
memoryview()	
set()
all()	
dict()	
help()	
min()	
setattr()
any()	
dir()	
input()
print()

#and much much more
```

### Program to Calculate the Area of a triangle (Using/creating functions)

```python

def calculate_tri(base, height):

    area = 0.5 * base * height
    return area

#calling the function
calculate_tri(10, 5)

```

### Multiple User Defined Functions

```python
def display_box(name):
  message = "* Hello {} *".format(name)
  print("*" * (len(message))
  print(message)
  print("*" * (len(message))
  
def greet_user():
  print("Please enter your name")
  name = input()
  display_box(name)
  
greet_user()
```