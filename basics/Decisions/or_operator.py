#beep picking an adventure

print ("enter the type of adventure (scary, short, long, safe)")
adventure = input()


if ("scary" in adventure or "short" in adventure):
    print ("Entering the dark forest")
elif ("long" in adventure or "safe" in adventure):
    print ("taking the safe route woop")
else:
    print ("Not sure which route to take lol...")