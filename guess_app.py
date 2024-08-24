import random
import streamlit as st

def guessing_game():
    st.title("Guessing Game")
    st.write("Welcome to the Guessing Game!")
    
    # Choose difficulty level
    level = st.radio(
        "Choose a difficulty level:",
        ("Easy (Range: 1-10, Trials: 5)",
         "Medium (Range: 1-50, Trials: 7)",
         "Hard (Range: 1-100, Trials: 10)")
    )

    if "Easy" in level:
        max_range = 10
        max_trials = 5
    elif "Medium" in level:
        max_range = 50
        max_trials = 7
    elif "Hard" in level:
        max_range = 100
        max_trials = 10

    # Initialize game state
    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, max_range)
        st.session_state.number_of_guesses = 0

    guess = st.number_input(f"Enter a number between 1 and {max_range}: ", min_value=1, max_value=max_range, step=1)

    if st.button("Guess"):
        st.session_state.number_of_guesses += 1

        if guess < st.session_state.number_to_guess:
            st.write("Too low!")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high!")
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.number_of_guesses} tries.")
            st.session_state.number_to_guess = random.randint(1, max_range)
            st.session_state.number_of_guesses = 0
            
        if st.session_state.number_of_guesses < max_trials:
            st.write(f"Tries left: {max_trials - st.session_state.number_of_guesses}")
        else:
            st.write(f"Sorry, you've used all your {max_trials} attempts. The number was {st.session_state.number_to_guess}.")
            st.session_state.number_to_guess = random.randint(1, max_range)
            st.session_state.number_of_guesses = 0


if __name__ == "__main__":
    guessing_game()
