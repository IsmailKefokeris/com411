
class robot():
     # A class attribute
    LAWS = "Protect, Obey and Survive"

    # A class method
    def the_laws(self):
        print(robot.LAWS)

    # An initialiser (special instance method)
    def __init__(self):

        # An instance attribute
        self.name = "Robot"
        self.age = 0

    # An instance method
    def display(self):
        print(f"I am {self.name}")
    
    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

class human():

    MAX_ENERGY = 100

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
        self.energy = human.MAX_ENERGY
    
    def display(self):
        print ("I am {} and i am {} years old and weigh {} i have an energy of {}".format(self.name,self.age,self.weight,self.energy))

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'


if (__name__ == "__main__"): #allows the program to only run in the main program file (this one)
    human = human("ismail",19,75)
    human.display()
