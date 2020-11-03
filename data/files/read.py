import os

def search(Fname):
    print ("Searching....")

    with open(Fname, "r") as file:
        for line in file:
            print (f"Looked in The {line}", end="")
    
    print ("\nDone!....")


def run():
    search("data/files/locations.txt")

run()