
def climb_ladder(remain, passed):

    if (remain > passed):
        print ("Still a wayyy to goo ;-;")
    elif (remain < passed):
        print ("Woo almost there")
    else:
        print ("well welll wellllllwell....ERrrorr>>....Breaking DO.w..n....")
    

def run():
    value1 = int(input("Enter the remaining steps: "))
    value2 = int(input("Enter the steps passed: "))

    climb_ladder(value1, value2)