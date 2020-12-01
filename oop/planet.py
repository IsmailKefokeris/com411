import human as human_bot
import random

class Planet():

    def __init__(self):
        self.species = {
            "humans": [],
            "robots": []
        } 
    
    def add_human(self, num):
        name = "human" + num
        self.species["humans"].append(name)

    def remove_human(self):
        if len(self.species["humans"]) > 0:
            name = str(input("Name: "))
            self.species["humans"].remove(name)
        else:
            print("no Humans available to remove")

    def add_robot(self, num):
        robot = "robot" + num
        self.species["robots"].append(robot)
    
    def remove_robot(self):
        if len(self.species["robots"]) > 0:
            robot = str(input("Name: "))
            self.species["robots"].remove(robot)
        else:
            print("no robots available to remove")
        
    def __repr__(self):
        return "humans {} and Robots {}".format(self.species["humans"], self.species["robots"])

    def __str__(self):
        return "Humans are: {} in total {} and Robots are: {} in total {} ".format(self.species["humans"], len(self.species["humans"]),self.species["robots"], len(self.species["robots"]))


class Universe():
    
    def __init__(self):
        self.planets = []
    
    def generate(self):
        planet = Planet()
        for _ in range(random.randrange(1,10)):
            planet.add_human(str(random.randrange(1,500)))
        for _ in range(random.randrange(1,10)):
            planet.add_robot(str(random.randrange(1,500)))

        self.planets.append(planet)




"""
if __name__ == "__main__":
    earth = Planet()
    earth.add_human()
    earth.add_human()
    earth.add_robot()
    print (earth)
    
"""