
def run():
    print ("How many numbers should I sum up?")
    num = int(input())
    num2 = 0
    num3 = 0
    total = 0

    while (num2 != num):
        num2 += 1
        print ("Please enter number {} of {}".format(num2, num))
        num3 = int(input())
        total = num3 + total
        

    print ("The Answer is {}".format(total))


