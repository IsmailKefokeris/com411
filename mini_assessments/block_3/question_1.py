import sys
import matplotlib.pyplot as plt


def combined():
    fig, ax = plt.subplots()
    triangle1x = [3,5,7,3]
    triangle1y = [3,5,3,3]

    ax.plot(triangle1x, triangle1y, "r--o")

    triangle2x = [3,5,7,3]
    triangle2y = [5,3,5,5]

    ax.plot(triangle2x, triangle2y, "b:s")

    triangle3x = [3,3,7,3]
    triangle3y = [3,5,4,3]

    ax.plot(triangle3x, triangle3y, "g-.*")

    triangle4x = [7,7,3,7]
    triangle4y = [3,5,4,3]

    ax.plot(triangle4x, triangle4y, "y-p")

    plt.show()


def separated():

    fig, ax = plt.subplots(2,2)

    triangle1x = [3,5,7,3]
    triangle1y = [3,5,3,3]

    ax[0,0].plot(triangle1x, triangle1y, "r--o")

    triangle2x = [3,5,7,3]
    triangle2y = [5,3,5,5]

    ax[0,1].plot(triangle2x, triangle2y, "b:s")

    triangle3x = [3,3,7,3]
    triangle3y = [3,5,4,3]

    ax[1,0].plot(triangle3x, triangle3y, "g-.*")

    triangle4x = [7,7,3,7]
    triangle4y = [3,5,4,3]

    ax[1,1].plot(triangle4x, triangle4y, "y-p")

    plt.show()

def data():
    coords = {}

    coords["triangle1"] = [[3,5,7,3],[3,5,3,3],["r--o"]]

    coords["triangle2"] = [[3,5,7,3],[5,3,5,5],["b:s"]]

    coords["triangle3"] = [[3,3,7,3],[3,5,4,3],["g-.*"]]

    coords["triangle4"] = [[7,7,3,7],[3,5,4,3],["y-p"]]

    lis = []

    lis.append(coords["triangle1"])
    lis.append(coords["triangle2"])
    lis.append(coords["triangle3"])
    lis.append(coords["triangle4"])

    return lis

def improved_separated():
    coord = data()
    print(coord)
    fig, ax = plt.subplots(2,2)

    ax[0,0].plot(coord[0][0], coord[0][1],"r--o") #format is coord[0][2]
    ax[0,1].plot(coord[1][0], coord[1][1],"b:s") #format is coord[1][2]
    ax[1,0].plot(coord[2][0], coord[2][1],"g-.*") #format is coord[2][2]
    ax[1,1].plot(coord[3][0], coord[3][1],"y-p") #format is coord[3][2]


#the list does include the format but for some odd reason 
#when I input it the format of the plot does not change

    plt.show()

improved_separated()
