
def movements():
    path = []
    path.append("Move Forward")
    path.append("10")
    path.append("Move Backward")
    path.append("5")
    path.append("Move Left")
    path.append("3")
    path.append("Move Right")
    path.append("1")
    return path

def run():
    move = movements()
    print ("Moving...")
    count = 0
    step = 1
    while (count != 8 and step != 9):
        print ("{} for {} steps".format(move[count],move[step]))
        step += 2
        count += 2

