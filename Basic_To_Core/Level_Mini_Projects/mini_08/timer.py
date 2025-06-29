import time

def countdown():
    for i in range(10, 1, -1):
        print(i)
        time.sleep(2)
    print("Time's up")

countdown()