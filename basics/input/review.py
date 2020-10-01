#Week 1 Final Program
import time

print(" ########## ")
print(" #  -  -  # ")
print(" #  ----  # ")
print(" ########## ")

time.sleep(1)

print(" ########## ")
print(" #  0  0  # ")
print(" #  ----  # ")
print(" ########## ")

time.sleep(1)

print(" ########## ")
print(" #  -  -  # ")
print(" #  ----  # ")
print(" ########## ")

time.sleep(1)

print(" ########## ")
print(" #  0  0  # ")
print(" #  ----  # ")
print(" ########## ")

time.sleep(1)

print ("Char 1: Oof, ouch, where am I...")
time.sleep(1)

location = input("What planet are you on: ")

print ("Char 2: you are on the planet {}. heh welcome".format(location))
time.sleep(2)

print ("Char 1: Thank you... but who are you?")

name = input("Enter Name: ")

print ("{}: My name is {} and I am a human. I found you half dead after your crash".format(name,name))
time.sleep(2)

print ("{}: these are your new stats: ".format(name))

lives = int(input("How many lives should he start with? "))
stamina = int(input("How much stamina should he start with? "))
level = 0

print ("Lives: "," ❤" * lives)
time.sleep(2)
print ("Stamina: "," ✺" * stamina)
time.sleep(2)
print ("Level:", level)
time.sleep(2)

print ("Beep: thats good to know... You can call me Beep if you wish")
time.sleep(2)

print ("{}: Nice to meet you Beep. ".format(name))
time.sleep(1)

