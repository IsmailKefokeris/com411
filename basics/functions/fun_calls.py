
def display(word):
    print ("-----------")
    print ("|         |")
    print ("|   {}   |".format(word))
    print ("|         |")
    print ("-----------")

def lower(word):
    return word.lower()

def upper(word):
    return word.upper()

def mirror(word):
    print ("your word is {}".format(word))
    rever = word[::-1]
    print ("This is it mirrored....{}".format(rever))

def repeat(word, times):
    
    count = 0

    while (count != times):
        count += 1

        if (count % 2 == 0):
            print (upper(word))
        else:
            print(word)


def run():
    word = str(input("Please enter a word: "))

    action = str(input("What would you like to do with it...(display in a box, lowercase, uppercase, mirror, repeat.)? "))

    if ("display" in action or "box" in action):
        display(word)
    elif ("lowercase" in action or "lower" in action):
        print ("your word lowered is: ", lower(word))
    elif ("uppercase" in action or "upper" in action):
        print ("your word uppered is: ", upper(word))
    elif ("mirror" in action):
        mirror(word)
    elif ("repeat" in action):
        tim = int(input("How many times do you want it to repeat? "))

        repeat(word, tim)
    else:
        print("I asked for one of the before mention....ugh never mind stupid")


run()
