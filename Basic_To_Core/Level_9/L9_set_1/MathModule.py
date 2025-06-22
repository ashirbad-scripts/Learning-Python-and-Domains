#  Use the math module to calculate the square root of a number.
import math

num = 15.23

a = math.ceil(num)
print("a = ", a)
print(f"Square root of {a} :  {math.sqrt(a)}")

b = math.floor(num)
print("b = ", b)
print(f"Square root of {b} : {math.sqrt(b)}")

# -----------------------------------------------------------
# Calculate factorial
import math
result = math.factorial(5)
print(result)

# Run separately
from math import factorial
r = factorial(5)
print(r)


# -----------------------------------------------------------
# Learn pow (x raised to y)
import math
p = math.pow(2,3)
print(p)


# -----------------------------------------------------------
# Find GCD
from math import gcd
hcf = gcd(24,45)
print(hcf)


# -----------------------------------------------------------
# convert degree to radians
from math import radians
dToR = radians(45)
print(dToR)


# -----------------------------------------------------------
# calculate log
from math import log
calculations = log(10)
calculationsBase1 = log(10, 10)
calculationsBase2 = log(100, 10)

print(calculations)
print(calculationsBase1)
print(calculationsBase2)


# -----------------------------------------------------------
# Use pi
from math import pi
print("Value of pi: ", pi)

# Another example
import math
def areaCircle(r):
    result = math.pi * (r*r)
    return result

print(areaCircle(2))


