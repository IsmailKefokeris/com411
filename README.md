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

## Week 5

sets, In python a set is equivalent to mathematics..but in terms of programming.. a set is a collection of distinct object (no duplicates..Unique). may be defined by membership rule or by listing its members. Sets are unordered which contains immutable objects(The items in  the set cannot be changed) but the set itself can be mutable (but the set itself can be changed) or immutable ...Frozen sets

Creating an example set:

```python
wedding = {"cake", "old", "new", "blue", "borrowed"} #Creates a set with some pre defined values... 

items = ("Guests", "witnesses") #Creates a set with another data structure..Has to be a tuple because sets must contain immutable objects! (LISTS ARE NOT)
wedding = {items}

```

Function:	                                                            Description:

len(s)	                                              The number of elements in set s (known as cardinality of s).

x in s --------------------------------------------	  Test x is a member of set s.

x not in s	                                          Test x is not a member of set s.

s.add(el) ------------------------------------------- Adds the element el to the set s.

s.discard(el)                                         Removes the element el from the set s if it is contained in the set s. If not, nothing will happen.

s.remove(el) --------------------------------------	  Removes the element el from the set s if it is contained in the set s. If not, a KeyError will occur.

s.issubeset(t)	----------------------------------------- Test whether every element of set s is in set t.
[Equivalent to s <= t]

s.issuperset(t)	----------------------------------------- Test whether every element of set t is in set s.
[Equivalent to s >= t]

s.union(t) -----------------------------------------	Creates a new set with elements from both set s and set t.
[Equivalent to s | t]

s.intersection(t) -----------------------------------------	Creates a new set with elements that are common to both set s and set t.
[Equivalent to s & t]

s.difference(t) -----------------------------------------	Creates a new set with elements that in set s but not in set t.
[Equivalent to s - t]

s.symmetric_difference(t) -----------------------------------------	Creates a new set with elements in either set s or set t but not both.
[Equivalent to s ^ t]

s.copy() -----------------------------------------	Creates a new set with a shallow copy of set s.

del s -----------------------------------------	Deletes the set s.

------------------------------------------------------------------------------------------------------------------------------------------------

### Dictionary

Dictionaries are dynamic, unordered and mutable collections of data. Dictionaries use hashing to determine how an item will be stored... Keys are unique in a dictionary and are used by hashing algorithms which will generate a hash value.

Creating an example Dictionary:

```python

wedding = {} #creates a dictionary (because the curly brackets are empty)

wedding["guests"] = 6  #stores the value 6 under the key guests. (adding an item)

wedding["guestsNames"] = ("john", "Amigoo", "peter")  #stores the guest names. (adding an item)


```


Function:	                                                            Description:

len(d)	                                                    The number of elements in dictionary d.
x in d		                                                Test x is a key of dicitonary d.
d["k"] = v		                                            Adds the value v using key k to the dicitonary d.
d.pop(k)		                                            Removes the value with key k from the dictionary d.
d.popitem()		                                            Removes the last inserted item (or random item in older versions of Python) from the dictionary d.
d.clear()		                                            Removes all key-values stored in the dictionary d.
d.items()		                                            Returns the key-value pairs stored in the dictionary d.
d.values()		                                            Returns all the values stored in the dictionary d.
d.copy()		                                            Creates a new dictionary with a shallow copy of dictionary d.
del d		                                                Deletes the dictionary d.


## Week 6

Data, Computer file is the most  basic unit to store data on a computer.
Multiple computer files can be grouped together into folders or otherwise known as directories.... A computer folder is essentially a container for computer files and may also contain other folders

#### File Paths and the Current Working Folder

The current working folder is the folder were the program is actually running.... There are two ways to access a file, an absolute path which is a location in the file system regardless of current working folder.... or a relative path which starts from the current working efolder which avoids the need for an absolute path.

#### File Formats

There are various different types of information files...for instance .txt, .csv, .json, .png, etc...

##### .txt

unformatted text

sample.txt
--------------------------
This is a text file with some sample data.

##### .csv

csv... stands for comma separated values..indicates how the text is stored in the file and often represents data from spreadsheets or databases...The first row often is the header....

movies.csv
--------------------------
Film,Genre,Year
Tangled,Animation,2010
Gnomeo and Juliet,Animation,2011
WALL-E,Animation,2008

##### .Json

Json...or otherwise known as a javascript object notation.... is an independent text based interchange format....files with this format will use .json extension and are used to exchanged data between web application and a server.

These files may contain simple data structures(dictionaries) that can be processed efficiently and flexibily....

songs.json
--------------------------
[
  {
    "song_id": "1",
    "song_title": "Zombie",
    "artist_id": "14",
    "album_id": 1,
    "duration": 301.123,
    "year": "1994"
  },
  {
    "song_id": "2",
    "song_title": "In The End",
    "artist_id": "35",
    "album_id": 9,
    "duration": 271.405,
    "year": 2002
  }
]



#### Python Modules

Python treats files as one of two categories - either as text files or binary files:

A text file is a file that contains data stored using a text-based format.  Text files can be plain (i.e. contain no formatting) or contain text with formatting.  Some examples of plain text files include files with the extensions .txt, .csv and .json.  Some examples of text files that contain formatting include .docx and .xls. 

A binary file is a file that contains data stored using a format other than a text-based format.  For example, audio, video and image files are binary files and can be processed as such by Python.

#### Programming python TXT Files

The key function in python is "open" which takes two parameters....file name and mode

Modes:

    Read: default mode and we would specify it using "r"

    append: Specified using "a" this will open a file for appending...if the file doesnt exist python will create it.

    write: specified by using "w" this will open a file in write mode...if the file doesnt exist python will create it.

    create: specified by using "x" In this mode, the file is created....If the file already exists then an error will be generated.

Additionally files can be opened as a text file("b"...doesnt need specification because its the default) or a binary file ("b" does need specification)

For example, if we wish to open an existing text file for reading we can use any of the following:
```python

    file = open("data.txt", "rt")

    #or, as text file is the default type of file, we have:

    file = open("data.txt", "r")

    #or, as read is also the default mode, we have:

    file = open("data.txt")

    #Similarly, if we wish to create and write to a new binary file, we can do the following:

    file = open("output.png", "wb")
```
WHENEVER YOU OPEN A FILE YOU MUST CLOSE IT AFTERWARDS


#### Programming python CSV Files

When working with csv in python we import something called csv (a module) which makes it simpler to handle csv files in python.

For example, if we wish to open a CSV file for reading and display the first column of each row then we can do the following:

```python

import csv

with open("data.csv") as csvfile:
    # This is the reader which will read the csv file
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # This gets each row in the csv file 
    for row in csv_reader:
        print(row[0])

```

Best to use with simply because it avoids having to close the same file after you are done and avoid you forgetting.


#### Programming python JSON Files

Again with Json we need to use a module to help process json...we have a module called json which we can use to help.

```python
import json

with open("data.json") as json_file:
  data = json.load(json_file)

print(data)

```

sometimes its useful to generate json...you can use functions such as dump...

```python
import json

# a dictionary...
json_data = {
    "name": "Prins",
    "job": "Lecturer"
}

# opening the file in write mode
json_file = open("output.json", "w")
# calls the dump function to write into the file
json.dump(json_data, json_file, indent = 4)

json_file.close()

```
Alternatively, the methods "loads" and "dumps" can be used when working with strings rather than files.
THEY HAVE AN "S" at the end to identify them

#### Python and Remote Files

We could use the request module allowing me to communicate with a web server..

We can get data (e.g. a JSON file) from a server using the method get:

```python
import requests

response = requests.get("https://somesite.com/data.json")
print(response.json())

```

We can send data (e.g. JSON) to a server using the method post:

```python
import json
import requests

data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_data = json.dumps(data)
requests.post("https://somesite.com/post", json=json_data)

```


## Week 7

Data Visualisation... Data visualisation is used to represent different types of information..It is going to be used for us to help solve real world problems, we want to represent relationsips and correlations between data sets and privdes a mean by which we understand trends. Visualisations is crucial to organisations allowing them to find patterns in user data and make important choices.


### Visulasing data with PYthon

Matplotlib..Library for python to create plots and graphs using python scripts..it can use a wide range of graphics and has dedicated plotting module named pyplot which can simplify the process of creating plots and graphs.

in convention the module pyplot is imported as "plt"  because the name is so long

```python
import matplotlib.pyplot as plt
```

Some commonly used functions are:

    .plot - Takes two parameters.. A list or values representing points on X and Y... itll draw them

        ```python
        import matplotlib.pyplot as plt

        x = [0,2,4,6,8,10]
        y = [0,20,40,60,80,100]

        plt.xlabel("x values")
        plt.ylabel("y values")

        plt.plot(x, y)
        plt.show()
        Pyplot Line
        import matplotlib.pyplot as plt

        x = [0,2,4,6,8,10]
        y = [0,20,40,60,80,100]

        plt.xlabel("x values")
        plt.ylabel("y values")

        plt.plot(x, y, "o")
        plt.show()
        ```

    .step - Similar to plot function but used to create a step plot

        ```python
        import matplotlib.pyplot as plt

        x = [0,2,4,6,8,10]
        y = [0,20,40,60,80,100]

        plt.xlabel("x values")
        plt.ylabel("y values")

        plt.step(x, y)
        plt.show()    

        ```
    
    .bar - Creates a Bar graph

        ```python
        import matplotlib.pyplot as plt

        x = [0,2,4,6,8,10]
        y = [0,20,40,60,80,100]

        plt.xlabel("x values")
        plt.ylabel("y values")

        plt.bar(x, y)
        plt.show()
        ```
    
    .pie - Creates a pie chart

        ```python
        
        import matplotlib.pyplot as plt

        labels = ('A', 'B', 'C', 'D')
        sizes = [15, 30, 45, 10]

        plt.pie(sizes, labels=labels)
        plt.show()

        ```



#### Week 8


###### Subplots with matplotlib...

Looking at data in different ways we can get different insights to the data...for instance data related to time there would be different techniques to visualise that..it also helps to compare things by seeing them next to each other..Using matplotlib we will be able to combine and create a number of charts or plots int o a single graphic (known as a "Figure")...The entire chart or graphic....A figure can consist of 0 or more axis with many subplots represented in a different way depending what we are drawing....

In Matplotlib figures contain:

![Matplotlib Figure Anatomy....Prins Butt](pictures/matplotlib.png)


Figure - A figure is a top level container for all plots and graphics...A figure is able to contain any number of Axes("Plots") and is able to be set to control the space between Axes...To be useful a figure must have atleast one Axes...

Creating a figure we would use the method ".figure()" which is from matplotlib.pyplot.... Once we have the figure it can be populated with plots ("AXES") as needed... we can also use the ".subplots" method to create subplots and with this method we are able to populate a figure with the number of Axes and arrange them into a grid of rows and columns...alternatively we are also able to use the method ".add_subplot" of a figure to add an individual subplot... into a 2 by 2 grid and if the current subplot is the 3rd it would use the values 2,2,3 to add a subplot to the appropriate location....

```python

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)

or

import matplotlib as plt

fig, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2)

or

import matplotlib as plt

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)

```

Axes - Axes represent a "plot" or "subplot" in a specific figure...they contain 2 or 3 Axis (2D or 3D plots)...Axes contains most of the elements taht make up a plot (Axis, Ticks, Lines, Text, etc)

```python

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)
x = range(0, 10, 1)
y = range(0, 20, 2)
axes[0,0].plot(x, y)
axes[1,1].plot(x, y)

```

Axis - The axis controls the limits of a plot and are represented by number line like objects in a plot....axis consist of ticks and tick labels...We can use the axis to control what ticks and labels are shown on screen....When adding ticks and labels it is often useful to call plt.tight_layout() to layout the plots neatly and ensure no overlapping...

```python 

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

x = range(0, 10, 1)
y = range(0, 20, 2)

axes[0,0].plot(x, y)
axes[0,0].set_xlabel('X')
axes[0,0].set_xlim(2, 8)
axes[0,0].set_ylabel('Y')
axes[0,0].set_ylim(4, 16)

plt.tight_layout()

```

Ticks - Ticks are represented on the axis and can either be major or minor (they are the numbers across an axis (XYZ)) A Major as shown in the diagram above is a longer thicker tick compared to its minor counterpart...by default minors are not visible on the axis ...major ticks represent the key points along an axis...Both major and minor ticks are controlled using tick parameters allowing their appearance and formatting to be manipulated....we can also specify the position of the ticks by supplying a list of values or generating these using "multipleLocator"...

```python

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, axs = plt.subplots(2, 2)

x = range(0, 10, 1)
y = range(0, 20, 2)

axs[0,0].plot(x, y)

axs[0,0].set_xlabel('X')
axs[0,0].set_xlim(2, 8)

axs[0,0].set_ylabel('Y')
axs[0,0].set_ylim(4, 16)

axs[0,0].tick_params(which='both', width = 2)
axs[0,0].tick_params(which='major', length = 8)
axs[0,0].tick_params(which='minor', length = 4, color = 'r')

axs[0,0].xaxis.set_minor_locator(MultipleLocator(1))
axs[0,0].yaxis.set_minor_locator(MultipleLocator(2))
axs[0,0].xaxis.set_major_locator(MultipleLocator(2))
axs[0,0].yaxis.set_major_locator(MultipleLocator(4))

plt.tight_layout()
plt.show()
```

#### Week 9 - Animations

Animation: System generated timed event

Events: something system or user initated

Basic Animation Loop.....

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
  ax.cla() # clears axis
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  ax.plot(frame, frame, "ro")

def run():
  simp_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)

  plt.show()

run()
```
Adding Init function and numpy to create a box and other techniques

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
data = None
fig, ax = plt.subplots()

def init():
    global data
    data = {
        "x":np.array[3,3, 4,4,3], 
        "y":np.array[3,4, 4,3,3]
    }

def animate(frame):
    ax.cla() # clears axis
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.plot(frame + data["x"], data["y"], "ro")

def run():
    simp_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000, init_func=init)

    plt.show()

run()
```

