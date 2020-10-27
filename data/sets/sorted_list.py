
def observed():
    observations = []

    for count in range(5):
        sees = input("What observation? ")
        observations.append(sees)

    return observations

def remove_observations(value):
    print ("Do you want to remove an observation?")
    action = input()
    observations = value

    if ("yes" in action):
        while "yes" in action:
            print ("Enter the observation you want to remove...")
            rem = input()
            observations.remove(rem)
            print ("Do you want to remove an observation?")
            action = input()
    return observations

def run():
    observations_origin = observed()
    observations_rem = remove_observations(observations_origin)
    count = 0
    arranged = set()

    while count != len(observations_rem):
        var = observations_rem[count]
        coun = observations_rem.count(var)
        fin = "{}, {}".format(var, coun)
        arranged.add(fin)

        count += 1

    print (sorted(arranged))

run()