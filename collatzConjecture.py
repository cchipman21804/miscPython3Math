# https://en.wikipedia.org/wiki/Collatz_conjecture
# https://youtu.be/094y1Z2wpJg
# Pick a number
# If number is odd, multiply by 3 and add 1
# If number is even, divide by 2
# If number equals 1, exit
# Count the iterations to the exit
#
import datetime as dt
from datetime import timedelta
#
startedAt = dt.datetime.now()
validInput = False
while not validInput:
    x = input("Enter the seed number: ")
    try:
        x = int(x)
    except ValueError:
        print("\n")
    else:
        validInput = True
#
# Set iterations to 0
i = 0
while x > 1:
    if x % 2 == 0:
        x /= 2
    else:
        x = x*3 + 1
    i += 1
    print(int(x))
print(f"Iterations: {i}")
endedAt = dt.datetime.now()
print(f"Runtime: {(endedAt - startedAt).seconds} seconds")
