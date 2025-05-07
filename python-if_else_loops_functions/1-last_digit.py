#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

output = f"Last digit of {number} is {last_digit} and is "

if last_digit > 5:
    output += "greater than 5"
elif last_digit == 0:
    output += "0"
else:
    output += "less than 6 and not 0"

print(output)
