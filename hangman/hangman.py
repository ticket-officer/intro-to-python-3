import random
import nltk
from nltk.corpus import words
import os

def download_words():
    try:
        nltk.data.find('corpora/words.zip')
    except LookupError:
        print("Downloading the 'words' corpus...")
        nltk.download('words')

def load_words():
    return words.words()

def choose_word(words_list):
    return random.choice(words_list).upper()

def display_hangman(lives):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        ---------
        '''
    ]
    return stages[lives]

def play_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6

    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of lives. The word was " + word + ". Maybe next time!")

def main():
    download_words()
    words_list = load_words()
    word = choose_word(words_list)
    play_game(word)

if __name__ == "__main__":
    main()
