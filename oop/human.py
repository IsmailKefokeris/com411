
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
        self.energy = 100

    # An instance method
    def display(self):
        print(f"I am {self.name}")
    
    def grow(self):
        self.age += 1
    
    def eat(self,eat):
        
        if (self.energy + eat) > 100:
            print("Unable to eat too much energy")
        else:
            self.energy = self.energy + eat

    def move(self, distance):
        if self.energy > distance:
            self.energy = self.energy - distance
        else:
            print ("Not enough Energy...eat something")
    
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
    
    def grow(self):
        self.age += 1
    
    def eat(self,eat):
        
        if (self.energy + eat) > 100:
            print("Unable to eat too much energy")
        else:
            self.energy = self.energy + eat

    def move(self, distance):
        if self.energy > distance:
            self.energy = self.energy - distance
        else:
            print ("Not enough Energy...eat something")
        




if (__name__ == "__main__"): #allows the program to only run in the main program file (this one)
    human = human("ismail",19,75)
    human.display()
    human.move(5)
    human.eat(10)
    human.eat(5)
    human.move(15)
    human.display()
