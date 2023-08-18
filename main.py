# GUESSING NUMBER GAME

import random

# We ask the user to enter the top value
top_value = input("Which is the max number you want to guess? ")

if top_value.isdigit():     # validates if a string is a number
    top_value = int(top_value)
    if top_value <= 1:
        print("Please enter a number bigger than 1 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

# Creating a random number
number_to_guess = random.randint(1, top_value)

# Create scoring system
attempts = 1
max_attempts = 10

# To keep repeating the action until we stop it
while True:
    # Check if there are attempts remaining
    if attempts > max_attempts:
        print("You failed ): you're out of attempts. Better luck next time.")
        break

    print("--------------------------------")
    print(f"Attempt {attempts}/{max_attempts}.")
    player_guess = input("What's your guess? ")

    if player_guess.isdigit():
        player_guess = int(player_guess)

        if player_guess < 1 or player_guess > top_value:
            # If the player choose a number out of range
            # Formats a string to write variables without concatenating
            print(f"Please choose a number between 1 and {top_value}")
        elif player_guess < number_to_guess:
            attempts += 1
            print("Guess higher 🎢.")
        elif player_guess > number_to_guess:
            attempts += 1
            print("Go down boy 🛝.")
        else:
            print(f"Congrats 😶‍🌫️. You guessed the number, it was {number_to_guess}")
            print(f"You did it on {attempts} attempts!")
            quit()
    else:
        print("Please enter a number next time.")
