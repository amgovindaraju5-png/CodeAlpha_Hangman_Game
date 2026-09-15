# Hangman Game

## Project Title
Hangman — CodeAlpha Python Programming Internship, Task 1

## Project Description
A simple text-based Hangman game where the player guesses a hidden word
one letter at a time. The game runs entirely in the console and uses
only Python's standard library.

## Objective
Build a Hangman game that demonstrates core Python concepts — random
selection, loops, conditionals, strings, and lists — within a small,
clearly explainable scope, as specified by the CodeAlpha Task 1 brief.

## Features
- 10 predefined words, one chosen at random each round
- Guess one letter at a time
- Input validation: empty input, numbers, symbols, multiple characters,
  uppercase letters, non-English characters, and repeated guesses are
  all detected and handled with a clear message
- Displays which letters have already been guessed
- Maximum of 6 incorrect guesses per round
- Win and loss detection, with the answer revealed on a loss
- Replay support — play as many rounds as you like, with a full state
  reset between rounds
- Clean exit with a short delay after the player quits

## Technologies Used
- Python 3
- Standard library only: `random`, `time`
- No external packages, no GUI, no graphics, no audio, no APIs

## Python Concepts Used
- `random.choice()` for word selection
- `while` loops for the game loop, guess validation, and replay loop
- `if` / `elif` / `else` for input validation and game logic
- Strings (word storage, comparison, formatting)
- Lists (`WORD_LIST`, `guessed_letters`)
- Functions for separation of concerns

## How to Run
```bash
python hangman.py
```

## Game Rules
- A word is chosen at random from a list of 10 words.
- Guess one letter at a time.
- Correct letters are revealed in their position(s) in the word.
- Incorrect letters count against a limit of 6 wrong guesses.
- You win by revealing every letter before running out of guesses.
- You lose if you reach 6 incorrect guesses — the word is then revealed.
- After each round you can choose to play again or exit.

## Example Gameplay
```text
========================================
      WELCOME TO HANGMAN!
========================================
Try to guess the hidden word one letter at a time.
You have 6 incorrect guesses allowed. Good luck!

A new word has been selected. Let's begin!

Word: _ _ _ _ _ _
Guessed so far: None
Incorrect guesses remaining: 6
Guess a letter: p
Good guess! 'p' is in the word.

Word: p _ _ _ _ _
Guessed so far: p
Incorrect guesses remaining: 6
Guess a letter: z
Sorry, 'z' is not in the word.

Word: p _ _ _ _ _
Guessed so far: p, z
Incorrect guesses remaining: 5
...
```

## Project Structure
```
hangman/
├── hangman.py        # main game
├── test_hangman.py   # unit tests for the non-interactive game logic
├── requirements.txt  # intentionally empty — standard library only
├── .gitignore
└── README.md
```

## Code Walkthrough
| Function             | Responsibility                                        |
| --------------------- | ------------------------------------------------------ |
| `choose_word()`        | Randomly selects a word from `WORD_LIST`               |
| `display_word()`       | Builds the underscore/letter view of the current word  |
| `get_valid_guess()`    | Prompts for and validates a single-letter guess        |
| `play_single_game()`   | Runs one full round: display, guess, win/loss check    |
| `ask_play_again()`     | Asks whether to start another round                    |
| `main()`               | Entry point — welcome message, game loop, goodbye       |

**How a win is detected:** the display string is rebuilt from
`guessed_letters` on every turn; once it contains no more underscores,
every letter has been found and the round is won.

**How the guess limit works:** `incorrect_guesses` starts at 0 and only
increases when a guessed letter isn't in the word. The main loop runs
while `incorrect_guesses < MAX_INCORRECT_GUESSES` (6), so the player
gets exactly 6 wrong guesses before losing.

## Running the Tests
```bash
python -m unittest test_hangman.py -v
```

## Learning Outcomes
- Practiced structuring a small program into single-purpose functions
- Practiced input validation and handling edge cases (case sensitivity,
  empty input, non-alphabetic input, duplicate guesses)
- Reinforced the use of lists and strings for state tracking
- Practiced writing basic unit tests for non-interactive logic
- Learned to scope a project to its stated requirements rather than
  over-building it

## Scope Note
This project intentionally stays within the Task 1 brief — console I/O
only, no GUI, no graphics, no external APIs or packages.