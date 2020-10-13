
def ass_char():
    print ("Program Started!...")

    code = int(input("Please enter ASCII code: "))

    if (abs(code) in range(32, 127)):
        char = chr(code)
        print ("The character represented by the ASCII code {} is {}".format(code, char))
        return char
    else:
        print (".....PRogram ENDed")

def run():
    ass_char()