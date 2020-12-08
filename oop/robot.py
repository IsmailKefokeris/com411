from abc import ABC, abstractmethod
from inhabitant import Inhabitant

class Robot(Inhabitant):

    LAWS = "Protect, Obey and Survive"

    def __init__(self):
        super().__init__()

    def the_laws(self):
        print(Robot.LAWS)


    def display(self):
        print(f"I am {self.name}")
    
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'
    
    def __repr__(self):
        return f'Robot(name={self.name}, age={self.age})'


if __name__ == "__main__":
    robot = Robot()
    robot.the_laws()
    robot.move()
    print(repr(robot))