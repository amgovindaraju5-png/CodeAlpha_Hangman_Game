"""
Basic unit tests for hangman.py.

These cover the parts of the game that don't require console input
(word selection, word display, and the constants the task requires).
get_valid_guess() and the full game loop are interactive by design and
are instead covered by manual/scripted playthroughs, not unit tests.
"""

import unittest

from hangman import (
    WORD_LIST,
    MAX_INCORRECT_GUESSES,
    choose_word,
    display_word,
)


class TestWordList(unittest.TestCase):
    def test_exactly_ten_words(self):
        self.assertEqual(len(WORD_LIST), 10)

    def test_all_words_are_lowercase_strings(self):
        for word in WORD_LIST:
            self.assertIsInstance(word, str)
            self.assertEqual(word, word.lower())

    def test_max_incorrect_guesses_is_six(self):
        self.assertEqual(MAX_INCORRECT_GUESSES, 6)


class TestChooseWord(unittest.TestCase):
    def test_returns_word_from_list(self):
        for _ in range(50):
            self.assertIn(choose_word(WORD_LIST), WORD_LIST)


class TestDisplayWord(unittest.TestCase):
    def test_no_letters_guessed(self):
        self.assertEqual(display_word("python", []), "_ _ _ _ _ _")

    def test_some_letters_guessed(self):
        self.assertEqual(display_word("python", ["p", "y"]), "p y _ _ _ _")

    def test_all_letters_guessed(self):
        self.assertEqual(
            display_word("python", list("python")), "p y t h o n"
        )

    def test_repeated_letters_all_revealed(self):
        # "elephant" has two "e"s and should reveal both from one guess
        self.assertEqual(
            display_word("elephant", ["e"]), "e _ e _ _ _ _ _"
        )

    def test_unrelated_guesses_ignored(self):
        self.assertEqual(display_word("python", ["z", "q"]), "_ _ _ _ _ _")


if __name__ == "__main__":
    unittest.main()
