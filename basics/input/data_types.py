
#turning an input into an integer data type
"""
number = int(input("Enter a whole number: "))
string = str(input("Enter a string: "))
decimal = float(input("Enter a decimal num: "))
"""

#Calculate BMI program starts here ----------
def run():
    print ("Hi human, what can i call you?")
    name = input()

    print ("So you go by {} thats so interesting, well its nice to meet you {}".format(name,name))

    print ("If you don't mind me asking how old are you?(in years)")
    age = int(input())

    print ("Wow you are err... not old ;)... my systems are faulty how tall are you?(in meters)")
    height = float(input())

    print ("Last question i promise, how much do you weigh?(in kilograms)")
    weight = float(input())

    bmi = weight / (height**2)

    print ("well {} it seems your bmi rating at the age of {} is {:.2f}".format(name, age, bmi))

