#beep is looking for a spare battery
print ("Where should I look?")
look = input()

if ("bedroom" in look):
    print ("Where in the bedroom should i look?")
    look = input()
    if ("bed" in look):
        print("found some shoes but not THE BATTERY!")
    else:
        print("Found some mess here but not battery ;-;")
elif ("bathroom" in look):
    print ("Where in the Bathroom should i Look??")
    look = input()
    if ("bathtub" in look):
        print ("Found a rubber ducky here but NOT THE BATTERY!!")
    else:
        print ("Found a Wet Surface... not the battery ;-;")

elif ("lab" in look):
    print ("Where in the Lab should i Look??")
    look = input()
    if ("table" in look):
        print ("Yes! I found my battery!")
    else:
        print ("Found some tools but no battery.")
else:
    print ("not sure where that is exactly but ill keep looking alone '='")