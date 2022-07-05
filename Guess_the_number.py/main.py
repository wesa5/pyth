
import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_chosen_number(user_guess, chosen_number, turns):
    if user_guess > chosen_number:
        print("Too High")
        return turns - 1
    elif user_guess < chosen_number:
        print("Too Low")
        return turns - 1
    else:
        (f"You got it! the aswer was {chosen_number}")

def set_difficulty():
    level = input("Chose a dificulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():

    print(logo)

    print("\nWelcome to the Number Guessing Game!")
    print("Am thinking of a number between 1 and 100")

    chosen_number = random.randint(1,100)

    turns = set_difficulty()
    
    user_guess = 0
    while user_guess != chosen_number:

        print(f"You have {turns} attempts remaining to guess the number.")
            
        user_guess = int(input("Make a guess: "))
        
        turns = check_chosen_number(user_guess, chosen_number, turns)
        if turns == 0:
            print("You've run out of guesses. You Lose")
            return


game()