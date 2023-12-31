#format the program to run in a gui
from tkinter import *
import sys

# Main function
# In all functions 'uc' refers to 'user choice'

def main():
    while True:
        print("Please select from the following options: ")
        uc = input("1. Madlib one 2. Madlib two 3. Madlib three 4. Exit : ")
        if uc == "4":
            sys.exit()
        elif uc == "1":
            madlib_1()
        elif uc == "2":
            madlib_2()
        elif uc == "3":
            madlib_3()
        else:
            print("Invalid input please select one of the following options provided.")
        
# madlib 1 function

def madlib_1():
    while True:
        uc = input("To start the madlib press 1 to start or press 2 to go to the main menu: ")
        if uc == "1":
            break
        elif uc == "2":
            main()
        else:
            print("Invalid input please select one of the following options provided.")
    
    print("Please select words that corospond with the desccription.\n")

    # verbpt refers to a verb in the past tense
    # a present participle is a verb ending in 'ing' like 'reading' 'writing' 'walking'

    adjective_1 = input("Select an adjective: ")
    name_1 = input("Select a name: ")
    adjective_2 = input("Select an adjective: ")
    noun_1 = input("Select a noun: ")
    name_2 = input("Select a name: ")
    verbpt_1 = input("Select a past tense verb: ")
    noun_2 = input("Select a noun: ")
    verbpt_2 = input("Select a past tense verb: ")
    name_3 = input("Select a name: ")
    noun_3 = input("Select a noun: ")
    verbpresentparticiple = ("Select a present participle verb: ")
    adjective_3 = input("Select an adjective: ")
    pluralnoun = input("Select a plural noun: ")
    name_4 = input("Select a name: ")
    verbpt_3 = input("Select a past tense verb: ")
    noun_4 = input("Select a noun: ")
    verbpt_4 = input("Select a past tense verb: ")

    print(f'''
          On a {adjective_1} night, {name_1} found themselves standing before an {adjective_2} mansion.
          It was said to be haunted by the {noun_1} of its previous owner. As {name_2}
          {verbpt_1} the door, a {noun_2} {verbpt_2} from within.
          Inside, {name_3} noticed a {noun_3} {verbpresentparticiple} on its own. The {adjective_3} air
          was suddenly filled with the sound of {pluralnoun}. Frightened, {name_4} {verbpt_3} to
          leave, only to find that the {noun_4} had mysteriously {verbpt_4} behind them.
          ''')

    while True:
        uc = input("To restart the madlib please select 1 to return to the main menu select 2: ")
        if uc == "1":
            madlib_1()
        elif uc == "2":
            main()
        else:
            print("Invalid input please select one of the following options provided.")

# madlib 2 function

def madlib_2():
    while True:
        uc = input("To start the madlib press 1 to start or press 2 to go to the main menu: ")
        if uc == "1":
            break
        elif uc == "2":
            main()
        else:
            print("Invalid input please select one of the following options provided.")
    
    print("Please select words that corospond with the desccription.\n")

    adjective_1 = input("Select an adjective: ")
    name_1 = input("Select a name: ")
    noun_1 = input("Select a noun: ")
    adjective_2 = input("Select an adjective: ")
    pluralnoun_1 = input("Select a plural noun: ")
    noun_2 = input("Select a noun: ")
    verbpt_1 = input("Select a past tense verb: ")
    name_2 = input("Select a name: ")
    adjective_3 = input("Select an adjective: ")
    pluralnoun_2 = input("Select a plural noun: ")
    verbpt_2 = input("Select a past tense verb: ")
    adjective_4 = input("Select an adjective: ")
    noun_3 = input("Select a noun: ")
    verbpt_3 = input("Select a past tense verb: ")
    adjective_5 = input("Select an adjective: ")
    noun_4 = input("Select a noun: ")
    name_3 = input("Select a name: ")
    noun_5 = input("Select a noun: ")

    print(f'''
          In the {adjective_1} heart of the town, {name_1} dared to venture into the {noun_1} at midnight.
          The {adjective_2} moonlight cast eerie shadows over the {pluralnoun_1}, and a {noun_2} {verbpt_1}
          in the distance. {name_2} felt a {adjective_3} chill as they walked between the {pluralnoun_2}.
          Suddenly, the ground {verbpt_2} beneath their feet, and a {adjective_4} {noun_3} {verbpt_3}
          up from the earth. The air was filled with a {adjective_5} {noun_4}, and {name_3} realized
          the {noun_5} of the graveyard were not resting in peace.
          ''')

    while True:
        uc = input("To restart the madlib please select 1 to return to the main menu select 2: ")
        if uc == "1":
            madlib_2()
        elif uc == "2":
            main()
        else:
            print("Invalid input please select one of the following options provided.")
        
# madlib 3 function

def madlib_3():
    while True:
        uc = input("To start the madlib press 1 to start or press 2 to go to the main menu: ")
        if uc == "1":
            break
        elif uc == "2":
            main()
        else:
            print("Invalid input please select one of the following options provided.")
    
    print("Please select words that corospond with the desccription.\n")

    noun_1 = input("Select a noun: ")
    adjective_1 = input("Select an adjective: ")
    name_1 = input("Select a name: ")
    occupation = input("Select an occupation: ")
    adjective_2 = input("Select an adjective: ")
    pluralnoun_1 = input("Select a plural noun: ")
    verbpt_1 = input("Select a past tense verb: ")
    adjective_3 = input("Select an adjective: ")
    noun_2 = input("Select a noun: ")
    name_2 = input("Select a name: ")
    verbpt_2 = input("Select a past tense verb: ")
    adjective_4 = input("Select an adjective: ")
    noun_3 = input("Select a noun: ")
    adjective_5 = input("Select an adjective: ")
    noun_4 = input("Select a noun: ")
    verbpt_3 = input("Select a past tense verb: ")
    adjective_6 = input("Select an adjective: ")
    verbpt_4 = input("Select a past tense verb: ")
    pluralnoun_2 = input("Select a plural noun: ")
    name_3 = input("Select a name: ")
    verb = input("Select a verb: ")
    adjective_7 = input("Select an adjective: ")

    print(f'''
          The abandoned {noun_1} at the edge of town had always been the subject of {adjective_1} stories. {name_1}, a
          {occupation}, dared to investigate it one {adjective_2} night. The {pluralnoun_1} of the building {verbpt_1}
          eerily in the moonlight, and a {adjective_3} {noun_2} seemed to echo through the halls. Inside, {name_2}
          {verbpt_2} a {adjective_4} {noun_3}, which made them feel {adjective_5}. Then, the {noun_4} {verbpt_3}. A
          {adjective_6} apparition {verbpt_4} in the shadows, whispering {pluralnoun_2}. Terrified,
          {name_3} knew it was time to {verb} this {adjective_7} place.
          ''')

    while True:
        uc = input("To restart the madlib please select 1 to return to the main menu select 2: ")
        if uc == "1":
            madlib_3()
        elif uc == "2":
            main()
        else:
            print("Invalid input please select one of the following options provided.")          

# starts the program at the main function

print("Welcome to madlibs!\n")
main()