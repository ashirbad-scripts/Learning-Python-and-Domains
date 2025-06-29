def logInputNxtLine():
    with open("Python_2025/Level_11 (Mini_Projects)/mini_05/logger.txt", "a") as file:
        while True:
            entry = input("Enter something (quit to exit): ")
            if entry.lower() == "quit" or entry.lower() == "exit":
                break
            file.write(entry + "\n")
            print("Entry Saved")
    
logInputNxtLine()