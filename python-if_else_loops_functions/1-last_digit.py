#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#my code
if number < -10 & number < 10:
    str = str(number)
    intero = int(str[-1])
else:
    str = str(number)
    intero = int(str)

if intero > 5:
    print(f"Last digit of {number} is {str[-1]} and is greater than 5")
elif intero == 0:
    print(f"Last digit of {number} is {str[-1]} and is 0")
else:
    print(f"Last digit of {number} is {str[-1]} and is less than 6 and not 0")
