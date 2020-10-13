
def display_ladder(steps):

    count = 0

    while (count != steps):
        count += 1
        print ("|   |")
        print ("-----")

def create_ladder():
    print ("How many steps does the ladder have? ")

    ladderStep = int(input())

    return display_ladder(ladderStep)


def run():
    create_ladder()

