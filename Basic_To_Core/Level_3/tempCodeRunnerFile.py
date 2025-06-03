value = 5

def modify():
    global value
    value += 10

def read():
    print(f"Current value : {value}")

modify()
read()