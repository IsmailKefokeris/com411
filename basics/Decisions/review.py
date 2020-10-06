
print ("what is your name?")
name = input()

if (len(name) < 5):
    print ("nice to meet you {}".format(name))
    print ("what kinds of hobbies do you have?")
    hobby = input()
    if ("gaming" in hobby or "photography" in hobby):
        print ("OH WOW.. I LOVE {} so muchhhh".format(hobby))
    elif ("exercise" in hobby or "dancing" in hobby):
        print ("ew {} is such a boring thing to do".format(hobby))
    else:
        print ("I dont really understand but have fun lol....")
if (len(name) > 5):
    print ("you have really long name can I call you something shorter?")
    shortname = input("yes or no: ")
    if ("yes" in shortname):
        print ("OH boy what can i call you??")
        nikname = input()
        print ("nice you meet you {}".format(nikname))
        print ("what kinds of hobbies do you have?")
        hobby = input()
        if ("gaming" in hobby or "photography" in hobby):
            print ("OH WOW.. I LOVE {} so muchhhh".format(hobby))
        elif ("exercise" in hobby or "dancing" in hobby):
            print ("ew {} is such a boring thing to do".format(hobby))
        else:
            print ("I dont really understand but have fun lol....")    
    elif ("no" in shortname):
        print ("uhm well okay then ill call you cunt :(")
    else:
        print ("uhmm..... i cant understand that BYE")