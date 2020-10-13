import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art

import basics.input.ascii_eyes as ascii_eyes
import basics.input.data_types as data_types
import basics.input.review as review
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input

from basics.functions.fun_calls import lower

def folder_sys():
    is_running = True

    while (is_running):
        print ("Which folder would you like to enter: ")
        print ("[A] Run 'Block A: Basics.input Programs")
        print ("[B] Run 'Block A: Basics.output Programs")
        print ("[C] Run 'Block A: Basics.repetition Programs")
        print ("[D] Run 'Block A: Basics.functions Programs")
        print ("[E] Run 'Block A: Basics.decisions Programs")
        print ("[Q] TO Go Back")
        folder = lower(input())

        if ("a" in folder):
            print("RUNNING....")
            print("")
            folder_input()
            print("")
        elif ("b" in folder):
            print("RUNNING....")
            print("")
            folder_output()
            print("")    
        elif ("c" in folder):
            print("RUNNING....")
            print("")
            folder_repetitions()
            print("")   
        elif ("d" in folder):
            print("RUNNING....")
            print("")
            folder_functions()
            print("") 
        elif ("e" in folder):
            print("RUNNING....")
            print("")
            folder_decisions()
            print("")
        elif ("q" in folder):
            print("RUNNING....")
            print("")
            break
            print("")
            



def folder_input():

    print ("Which program in Basics.input would you want to run? ")
    response = input()
    if ("ascii_eyes" in response or "ascii" in response or "ascii eyes" in response):
        print("RUNNING ASCII_EYES PROGRAM....")
        print("")
        ascii_eyes.run()
        print("")
    elif ("data_types" in response or "data" in response or "data types" in response):
        print("RUNNING DATA_TYPES PROGRAM....")
        print("")
        data_types.run()
        print("")
    elif ("review" in response):
        print("RUNNING REVIEW PROGRAM....")
        print("")
        review.run()
        print("")
    elif ("string_operators" in response or "string" in response or "string operators" in response):
        print("RUNNING STRING_OPERATORS PROGRAM....")
        print("")
        string_operators.run()
        print("")
    elif ("user_input" in response or "user" in response or "user input" in response):
        print("RUNNING USER_INPUT PROGRAM....")
        print("")
        user_input.run()
        print("")


def folder_functions():
    pass


def folder_decisions():
    pass


def folder_repetitions():
    pass


def folder_output():

    print ("Which program in Basics.Output would you want to run? ")
    response = input()
    if ("simple_message" in response or "simple" in response or "simple message" in response):
        print("RUNNING SIMPLE_MESSAGE PROGRAM....")
        print("")
        simple_message.run()
        print("")
    elif ("multiline_message" in response or "multiline" in response or "multiline message" in response):
        print("RUNNING MULTILINE_MESSAGE PROGRAM....")
        print("")
        multiline_message.run()
        print("")
    elif ("escape_characters" in response or "escape" in response or "escape characters" in response):
        print("RUNNING ESCAPE_CHARACTERS PROGRAM....")
        print("")
        escape_characters.run()
        print("")
    elif ("ascii_art" in response or "ascii" in response or "ascii art" in response):
        print("RUNNING ASCII_ART PROGRAM....")
        print("")
        ascii_art.run()
        print("")


def run():
    is_running = True

    while (is_running):
        print ("What Would you like to do? ")
        print ("[A] Run 'Block A: Basics Programs")
        print ("[Q] Quit Program")

        response = lower(input())

        if (response == "a"):
            folder_sys()
        elif (response == "q"):
            break
        else:
            print ("INVALID OPTION! PLEASE TRY AGAIN......")

run()
