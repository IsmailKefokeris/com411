import os

def search(Fname):
    print ("Searching....")

    with open(Fname, "r") as file:
        for line in file:
            print (f"Looked in The {line}")
    
    print ("Done!....")


def run():
    search("read.txt")

run()