
print ("How many bars should be charged?")
charge = int(input())

bars = 0

while (bars != charge):
    print ("Charging", end = "")
    bars += 1
    print (" ❂" * bars)

print ("The battery is fully charged")