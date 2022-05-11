from random import randint
from art import logo

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10

def compare_numbers(user_guess, secret_number, attempts_left):
    if user_guess > secret_number:
        print("Too high.")
        return attempts_left - 1
    elif user_guess < secret_number:
        print("Too low.")
        return attempts_left - 1
    else:
        print(f"You got it! The answer was {user_guess}")
        exit()

def select_level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return EASY_LEVEL_ATTEMPTS

def start_game():
    print(logo)
    print(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    secret_number = randint(0, 100)
    attempts_left = select_level()
    while attempts_left !=0:
        print(f"You have {attempts_left} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        attempts_left = compare_numbers(user_guess, secret_number, attempts_left)
        print(attempts_left)

    print("You've run out of guesses, you lose.")

start_game()











