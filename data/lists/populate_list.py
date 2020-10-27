
def directions():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Move left")
    directions.append("Move right")

    return directions

def menu():

    print ("Please select a direction: ")

    direct = directions()

    for index in range (len(direct)):
        print ("{}: {}.".format(index, direct[index]))
    
    select = int(input())

    print("{}...is the direction you chose".format(direct[select]))
    return select

def run():
    route = []

    print ("Working out escape route....")

    for _count in range(5):
        slct = menu()
        direct = directions()
        route.append(direct[slct])

    print ("Escape Route: {}".format(route))
    
