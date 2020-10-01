
#Robot Default Face

print(" ########## ")
print(" #  -  -  # ")
print(" #  ----  # ")
print(" ########## ")

print ("I am feeling at ease, what should my new eyes be?")

eyes = input()

print ("Brilliant!!")

#tried using format but cant really get it to work with the ascii art correctly
print(" ########## ")
print(" # {}  {} # ".format(eyes,eyes))
print(" #  ----  # ")
print(" ########## ")

#just manually entering it and adjusting it seems to have worked better for now
print(" ########## ")
print(" # ", eyes,"", eyes,  " # ")
print(" #  ----  # ")
print(" ########## ")


