"""
Hangman Game
CodeAlpha Python Programming Internship - Task 1
A simple text-based Hangman game where the player guesses a word
one letter at a time using only Python's standard library.
"""

import random
import time

# A small predefined list of exactly 10 words for the game
WORD_LIST = [
    "python",
    "hangman",
    "computer",
    "keyboard",
    "internship",
    "function",
    "variable",
    "algorithm",
    "database",
    "compiler"
]

# Maximum number of incorrect guesses allowed
MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select one word from the given list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """
    Build the current display version of the word.
    Revealed letters are shown; everything else is an underscore.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_valid_guess(guessed_letters):
    """
    Ask the player for a single letter and validate it.
    Keeps asking until a valid, new letter is entered.
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) == 0:
            print("Please enter a letter. Input cannot be empty.")
        elif len(guess) > 1:
            print("Please enter only ONE letter at a time.")
        elif not ("a" <= guess <= "z"):
            print("Please enter a valid alphabet letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_single_game():
    """Play one complete round of Hangman."""
    word = choose_word(WORD_LIST)
    guessed_letters = []      # letters the player has already tried
    incorrect_guesses = 0

    print("\nA new word has been selected. Let's begin!")

    # Main game loop: continues until win or loss
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        current_display = display_word(word, guessed_letters)
        print("\nWord:", current_display)

        if guessed_letters:
            print("Guessed so far:", ", ".join(sorted(guessed_letters)))
        else:
            print("Guessed so far: None")

        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")

        # Check the win condition before asking for another guess
        if "_" not in current_display:
            print(f"\nCongratulations! You guessed the word: '{word}'")
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    # If we exit the loop, the player has run out of guesses
    print(f"\nGame over! You ran out of incorrect guesses.")
    print(f"The correct word was: '{word}'")


def ask_play_again():
    """Ask the player if they want to play another round."""
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Please answer 'yes' or 'no'.")


def main():
    """Program entry point: welcome message and game loop."""
    print("=" * 40)
    print("      WELCOME TO HANGMAN!")
    print("=" * 40)
    print("Try to guess the hidden word one letter at a time.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed. Good luck!")

    playing = True
    while playing:
        play_single_game()
        playing = ask_play_again()

    print("\nThanks for playing Hangman. Goodbye!")
    time.sleep(10)  # wait 10 seconds before the program exits


# Standard Python entry point check
if __name__ == "__main__":
    main()