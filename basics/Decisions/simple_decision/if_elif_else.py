
direction = input("What direction should i move the paintbrush(up, down, left or right)? ")



if (direction == "up"):
    print("up")
elif (direction == "down"):
    print("down")
elif (direction == "left"):
    print("left")
elif (direction == "right"):
    print("right")
else:
    print("what?!?! gimme a direction")

print("i am painting in the direction {}".format(direction))