
def cross_bridge(steps):
    count = 0
    
    while count != steps:
        count += 1
        print ("Crossed step...")
        

    if count > 5:
        print ("The bridge is collapsing!! HURRY")
    else:
        print ("We must keep going!")


def run():
    step = int(input("Enter the amount of steps "))
    cross_bridge(step)