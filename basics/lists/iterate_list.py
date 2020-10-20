
def directions():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn Left")
    directions.append("Turn Right")

    return directions

def menu():
    print("Select a direction Please")
    direct = directions()

    for index in range(len(direct)):
        print("{}:{}.".format(index, direct[index]))


def run():
    menu()

