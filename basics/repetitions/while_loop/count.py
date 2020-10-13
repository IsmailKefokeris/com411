def run():

    print ("How many live cables should I avoid")
    avoid = int(input())

    livec = 0

    while (livec != avoid):
        print ("Avoiding...", end="")
        livec += 1
        print ("Done! {} live cable(s) avoided!".format(livec))

    print ("All live cables have been avoided!")