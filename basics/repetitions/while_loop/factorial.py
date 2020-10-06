
print ("please enter a number")
num = int(input())

#calculate factorial
count = 0
total = 1


while (count < num):
    count += 1
    #the total variable keeps the new equal every loop, for instance the factorial of 5 is 
    #total = 1 * 1, total = 1 * 2, total = 2 * 3, total = 6 * 4, total = 24 * 5, total = 120
    total = total * count

print (total)