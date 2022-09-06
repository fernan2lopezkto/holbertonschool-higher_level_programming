#!/usr/bin/python3
import random
from tkinter import commondialog
number = random.randint(-10000, 10000)
str = str(number)
intero = int(str[-1])
if intero > 5:
    print(f"Last digit of {number} is {str[-1]} and is greater than 5")
elif intero == 0:
    print(f"Last digit of {number} is {str[-1]} and is 0")
else:
    print(f"Last digit of {number} is {str[-1]} and is less than 6 and not 0")
