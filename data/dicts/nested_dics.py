

def short_pattern():
    pattern = {}

    pattern["sequence"] = "101"
    pattern["occurrences"] = 5

    return pattern

def medium_pattern():
    pattern = {}

    pattern["sequence"] = "111000"
    pattern["occurrences"] = 25

    return pattern

def long_pattern():
    pattern = {}

    pattern["sequence"] = "1100110011001100"
    pattern["occurrences"] = 50

    return pattern

def run():
    print ("Analysing Patterns...")
    total = {}
    total["shortP"] = short_pattern()
    total["mediumP"] = medium_pattern()
    total["longP"] = long_pattern()

    print (total)

run()