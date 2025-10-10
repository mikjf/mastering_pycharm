import random

print("Welcome to the HI - LO game")

# Pick a random number between 1 and 100
number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 & 100: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Got it: The number is {number}")
