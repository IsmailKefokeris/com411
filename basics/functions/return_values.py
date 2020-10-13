

def sum_weights(beep, bop):
    total = beep + bop
    return total

def avg_weight(beep, bop):
    weight = sum_weights(beep, bop)

    average = weight / 2
    return average

def run():

    bot1 = int(input("Please Enter the weight for Beep: "))
    bot2 = int(input("Please Enter the weight for Bop: "))

    action = input("Enter an action (sum or average): ")

    if ("sum" in action):
        print ("The Sum of Beep and Bops Weight is: ", sum_weights(bot1, bot2))
    elif ("average" in action):
        print ("The average for beep and bops weight is: ", avg_weight(bot1, bot2))
    else:
        print ("ERRORRRR.... ENTER either Sum or Average.....")

run()

