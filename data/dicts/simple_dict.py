
def pattern():
    sequences = {}

    sequences["short sequence"] = 3
    sequences["medium sequence"] = 2
    sequences["long sequence"] = 1

    return sequences


def run():
    print(pattern())


run()