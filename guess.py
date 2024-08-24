import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (Range: 1-10, Trials: 5)")
    print("2. Medium (Range: 1-100, Trials: 7)")
    print("3. Hard (Range: 1-1000, Trials: 15)")

    # Choose difficulty level
    while True:
        level = input("Enter the level number (1, 2, or 3): ")
        if level == '1':
            max_range = 10
            max_trials = 5
            break
        elif level == '2':
            max_range = 100
            max_trials = 7
            break
        elif level == '3':
            max_range = 1000
            max_trials = 10
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

    # Generate a random number within the chosen range
    number_to_guess = random.randint(1, max_range)
    number_of_guesses = 0

    print(f"\nI'm thinking of a number between 1 and {max_range}. You have {max_trials} attempts to guess it.")

    # Loop until the user guesses the correct number or runs out of attempts
    while number_of_guesses < max_trials:
        guess = input("Enter your guess: ")

        # Make sure the input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        number_of_guesses += 1

        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {number_of_guesses} tries.")
            break

        if number_of_guesses < max_trials:
            print(f"Tries left: {max_trials - number_of_guesses}")
        else:
            print(f"Sorry, you've used all your {max_trials} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guessing_game()
