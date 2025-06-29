from datetime import datetime

def logNote():
    notes = input("Enter notes: ")
    timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    with open("Level_11 (Mini_Projects)/mini_01/notes.txt", "w") as file:
        file.write(f"{timestamp} - {notes}\n")
    print("Notes Saved Succesfully")

logNote()

# RULE - 101 - MAINTAIN DIRECTORY
'''
IF YOU ARE OPEING lEVEL_6/... THEN LEVEL 6 MUST BE IN ROOT DIRECTORY ONLY
LIKE PYTHON>LEVEL6/....

IT WONT WORK :-
JS
PYTHON/lEVEL_6/.....

MAKE SURE YOUR OPEING FOLDER IS ONLY IN ROOT DIRECTORY 

'''