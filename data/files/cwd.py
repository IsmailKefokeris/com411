
import os

def cwd():
    path = os.getcwd()
    print (f"Current Working FOlder Path: {path}")
    print ("The Folder contains the following")

    for file in os.listdir(path):
        print (file)

def run():
    print("Processing....")
    cwd()

run()

