!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".f(number))
elif number == 0:
    print("{:d} is zero".f(number))
else:
    print("{:d} is negative".f(number))
