import random

def check_guess(guess, number, attempts):
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {number}.")
        return 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
guess = 0
attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid difficulty. Defaulting to 'easy'.")
    attempts = 10

while attempts > 0 and guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_guess(guess, number, attempts)
    if attempts == 0 and guess != number:
        print(f"You've run out of guesses. The number was {number}.")
