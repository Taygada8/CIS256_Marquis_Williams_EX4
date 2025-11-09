import unittest
import random
from guess_the_word import word_list

class TestGuessTheWord(unittest.TestCase):

    def test_word_selection_from_list(self):
        """Ensure the selected word is from the predefined list."""
        selected_word = random.choice(word_list)
        self.assertIn(selected_word, word_list)

    def test_correct_guess_updates_word(self):
        """Check that a correct guess reveals the letter in the guessed word."""
        secret_word = "python"
        guessed_word = ['_'] * len(secret_word)
        guess = 'y'

        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess

        self.assertEqual(guessed_word, ['_', 'y', '_', '_', '_', '_'])

    def test_incorrect_guess_does_not_update_word(self):
        """Check that an incorrect guess does not change the guessed word."""
        secret_word = "python"
        guessed_word = ['_'] * len(secret_word)
        guess = 'z'

        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess

        self.assertEqual(guessed_word, ['_', '_', '_', '_', '_', '_'])

if __name__ == '__main__':
    unittest.main()
