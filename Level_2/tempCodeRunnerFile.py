secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct")
        # break
    else:
        print("try Again")