

def observed():
    observations = []
    count = 0
    while count != 7:
        sees = input("What do you see? ")
        observations.append(sees)
        count += 1
    return observations

def run():
    print ("Counting Observations...")
    observing = observed()
    appear = set()
    count = 0

    while count != len(observing):
        var = observing[count]
        coun = observing.count(var)
        fin = "{}, {}".format(var, coun)

        appear.add(fin)
        count += 1

    print (appear)

run()

