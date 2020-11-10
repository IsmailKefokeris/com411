import matplotlib.pyplot as plt

def data():
    paths = {}
    line = int(input("What type of line? 0 - Dotted, 1 - Dashed, 2 - Solid: "))
    colour = int(input("What Colour? 0 - Red, 1 - Green, 2 - Blue: "))
    mark = int(input("What type of Marker? 0 - Circle, 1 - Square, 2 - Triangle: "))

    if line == 0:
        paths["line"] = ":"
    elif line == 1:
        paths["line"] = "--"
    elif line == 2:
        paths["line"] = "-"

    if colour == 0:
        paths["colour"] = "r"
    elif colour == 1:
        paths["colour"] = "g"
    elif colour == 2:
        paths["colour"] = "b"
    
    if mark == 0:
        paths["mark"] = "o"
    elif mark == 1:
        paths["mark"] = "s"
    elif mark == 2:
        paths["mark"] = "^"
    
    return paths
    

def generate():
    amount = int(input("How many lines would you like to display? "))
    wayX = [1, 5, 7,8,10,15] 
    wayY = [1, 6, 4,7,9,14] 
    
    for _ in range(amount):
        info = data()
        plt.plot(wayX,wayY, info["colour"] + info["mark"] + info["line"])
        plt.show()
        


def run():
    print("Running....")
    generate()
    print("Done!!!")

run()

