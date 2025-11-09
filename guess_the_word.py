import random

# Predefined list of words
word_list = ['python', 'developer', 'hangman', 'challenge', 'program']

# Select a random word
secret_word = random.choice(word_list)
guessed_word = ['_'] * len(secret_word)
attempts_left = 6
guessed_letters = set()

print(" Welcome to Guess the Word!")
print("You have", attempts_left, "attempts to guess the word.")

# Game loop
while attempts_left > 0 and '_' in guessed_word:
    print("\nCurrent word:", ' '.join(guessed_word))
    guess = input("🔤 Guess a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Process guess
    if guess in secret_word:
        print("✅ Correct!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("❌ Incorrect.")
        attempts_left -= 1
        print("Attempts left:", attempts_left)

# End of game
if '_' not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n😢 Out of attempts. The word was:", secret_word)
