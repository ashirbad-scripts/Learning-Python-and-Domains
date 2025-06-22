# Use the random module to generate a random number between 10 and 50.
import random
randomNumber = random.randint(10,50)
print("Random number between 10 and 50 : ", randomNumber)


# -----------------------------------------------------------
# Import only the randint function from the random module.
from random import randint

# To avoid 0
a = randint(0, 2) + 1
print(a)


# -----------------------------------------------------------
# Generate a Random Floating-Point Number Between 0 and 1 (random)
import random

random_float = random.random()
print("Random float between 0 and 1:", random_float)


# -----------------------------------------------------------
# Random floating point nummber in specific range
import random
num = random.uniform(5.5, 9.5)
print(num)


# -----------------------------------------------------------
# Pick random element from a list 
import random
colors = ["red", "blue", "green", "white"]
picked = random.choice(colors)
print(picked)


# -----------------------------------------------------------
# Pick multiple random elements
from random import sample, choice
names = ["alice", "john", "ray", "willow"]
pickedNames = choice(names)
pickedNamesR = sample(names, 3)

print(pickedNames)
print(pickedNamesR)


# -----------------------------------------------------------
# Multiple random choices
import random
fruits = ["apple", "orange", "peach", "cranberry"]
picked1 = random.choices(fruits, k=2)
picked2 = random.choices(fruits, k=10)

print(picked1)
print(picked2)


# -----------------------------------------------------------
# Shuffle
from random import shuffle
cards = ["Ace", "king", "queen", "Jack"]
shuffle(cards)
print(cards)


# -----------------------------------------------------------
# Toss a coin
import random
coin = random.choice(['Heads','Tails'])
print(coin)


# -----------------------------------------------------------
# Roll  a dice
import random
diceRoll = random.randint(1,6)
print(diceRoll)



# -----------------------------------------------------------
import random

animals = ['cat', 'dog', 'rabbit']
picking = random.choices(animals, weights=[1, 3, 5], k=5)
print(picking)

'''
    'cat' has a weight of 1 out of the total weight (1 + 3 + 1 = 5). 
    So, the probability of picking a 'cat' in a single selection 
    is approximately  1/5 or 20%
 
    'dog' has a weight of 3 out of the total weight of 5. So, the 
    probability of picking a 'dog' in a single selection is approximately  
    3/5 or 60%.

    'rabbit' has a weight of 1 out of the total weight of 5. So, the 
    probability of picking a 'rabbit' in a single selection is approximately  
    1/5 or 20%
    
'''