
def ass_calculate():
    print ("Program Started!...")

    char = input("Please enter a standard letter: ")

    if (len(char) == 1):
        ass = ord(char)
        print ("The Decimal Ascii Code for {} is {}".format(char, ass))
        return ass
    else:
        print ("ONE CHARACTER OR LETTER ONLY.....PRogram ENDed")


def run():
    ass_calculate()