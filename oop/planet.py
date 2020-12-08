from human import Human
from robot import Robot
import random

class Planet():

    def __init__(self):
        self.inhabitants = []
    
    def add_human(self, num):
        name = "human" + num
        human = Human(name)
        self.inhabitants.append(human)

    def remove_human(self):
        remove = False
        for species in self.inhabitants:
            if isinstance(species,Human) and remove == False:
                self.inhabitants.remove(species)
                remove = True
        if remove == False:
            print ("No Humans to be removed!!")

    def add_robot(self, num):
        name = "robot" + num
        robot = Robot(name)
        self.inhabitants.append(robot)
    
    def remove_robot(self):
        remove = False
        for species in self.inhabitants:
            if isinstance(species,Robot) and remove == False:
                self.inhabitants.remove(species)
                remove = True
        if remove == False:
            print ("No robots to be removed!!")

    def __repr__(self):
        robot = 0
        human = 0
        for species in self.inhabitants:
            if isinstance(species,Human):
                human += 1
            else:
                robot += 1

        return f"There are a total of {human} Humans and a total of {robot} Robots on this planet"

    def __str__(self):
        robots = []
        humans = []
        h, r = 0, 0
        for species in self.inhabitants:
            if isinstance(species,Human):
                humans.append(species) 
                h += 1
            else:
                robots.append(species) 
                r += 1

        return f"Humans are: {humans} in total {h} and Robots are: {robots} in total {r}"


"""
if __name__ == "__main__":
    earth = Planet()
    earth.add_human()
    earth.add_human()
    earth.add_robot()
    print (earth)
    
"""