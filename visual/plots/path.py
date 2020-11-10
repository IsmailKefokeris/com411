import matplotlib.pyplot as plt

def coordinate():
    x = input("Enter X value: ")
    y = input("Enter Y value: ")

    return (x,y)

def path():
    print ("Retrieving Paths...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

def run():
    values = path()

    plt.plot(values[0],values[1], "ro--")
    plt.show()

run()