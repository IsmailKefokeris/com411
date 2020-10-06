#start
print ("how many cables should i remove??")
#user input
num = int(input())
removed = 0

#while loop initiated
while (removed != num):
    removed += 1
    print ("Removed Cable {}".format(removed))
    

#end message
print ("Done removing all {} cables".format(num))
