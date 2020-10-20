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

## Week 4

#### Data Types

##### Ordered Data Structures

lists - Collection of data (can contain more than one data value), its a dynamic data structure (grows with the amount of items you put in it), they are also known as ordered data structures (meaning when we put something into it it will maintain the order of that item), A list is also mutable (meaning it can be modified after creation at any time), this all comes at a price in order to get this flexibility you will need to allocate more memory for lists which means it may not be as efficient as other data structures. Data stored in a list is Heterogeneous (homogeneous is the same data type , heterogeneous is different data types.). You cant perform mathematical operations directly on the list(for instance getting the list and deviding it by 3 wouldnt work youd have to do it manually) = lists are used for shorter sequences of data where no mathematical operations need to be applied.

Array - Collection of Data where the items are stored contiguous in memory (which means items will be stored directly next to each other), It is not a built in data structure in python and will need the use of modules (array, numpy). Arrays are homogeneous (homogeneous is the same data type , heterogeneous is different data types.) and has a fixed size (static)(meaning everything in the array will have to  be of the same type and size)...arrays are more memeory efficient than lists and are so used for larger data sequences where you can perform mathematical operations.

Tuple - Is an ordered data structure (like a list but a tuple is immutable) (immutable data structure means we are unable to change it after creation). tuples are also heterogeneous (homogeneous is the same data type , heterogeneous is different data types.). (Because tuples are immutable this means that its more prodictable acausing less errors and you can understand it better, aswell as it being very efficient in memory) (used in things like read only, making sure it cant be modified)

##### Unordered Data Structures

set - Is an unordered collection of data (means when you put something into a set you wont know the index or where it is stored(throw a marble in the bag you dont know where itll go but itll be in the bag)), sets are unique and not indexed, (unique means you can also rid yourself of duplicates because everything is unique.) There are mutable sets (you can change and add items to it) but you also have something called frozen set which means its immutable.

Dictionary - Dictionaries are dynamic (does grow and shrink) but is also unordered (meaning you will have the key but you wont know where the value is. Each key in the dictionary is unique the dictionary will hash it and will figure out how to map it )


### Tuple/List Example

```python
person = ("Ismail", 19) # tuple

person2 = ["Ismail", 19] # List

print(type(person)) #prints out the data type(Tuple)

print (person + (22, 45)) #tuples cant be changed but we have 2 tuples and it will create a brand new tuple and add all the items together.

#repition in a tuple

personlots = person * 4

print(personlots) # You can multiply tuples (repitition)

#Min and Max in a tuple

temp = (12,13,15,23)

print (min(temperatures))
print (max(temperatures))
```