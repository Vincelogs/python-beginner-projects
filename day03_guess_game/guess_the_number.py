# guess_the_number.py

import random

print("🎯 Welcome to Guess the Number Game 🎯")
secret_number = random.randint(1, 10)
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"✅ Correct! You guessed it in {attempts} tries.")
