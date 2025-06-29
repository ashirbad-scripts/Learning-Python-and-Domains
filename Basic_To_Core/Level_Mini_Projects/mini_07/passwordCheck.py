import re

def check_password_strength(password):
    if len(password) < 8:
        return "❌ Password is too short. Must be at least 8 characters."
    elif not re.search(r"\d", password):
        return "❌ Password must contain at least one digit."
    elif not re.search(r"[A-Za-z]", password):
        return "❌ Password must contain at least one letter."
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "❌ Password must contain at least one special character."
    else:
        return "✅ Password is strong."

# Loop until correct password
while True:
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

    # Log result to file
    with open("Python_2025/Level_11 (Mini_Projects)/mini_07/pass.txt", "w", encoding="utf-8") as file:
        file.write(f"Password Attempt: {password}\nResult: {result}\n{'-'*40}\n")

    if result == "✅ Password is strong.":
        break


# RULE - 101 - MAINTAIN DIRECTORY
'''
IF YOU ARE OPEING lEVEL_6/... THEN LEVEL 6 MUST BE IN ROOT DIRECTORY ONLY
LIKE PYTHON>LEVEL6/....

IT WONT WORK :-
JS
PYTHON/lEVEL_6/.....

MAKE SURE YOUR OPEING FOLDER IS ONLY IN ROOT DIRECTORY 

'''