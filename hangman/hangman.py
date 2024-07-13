import random
from random_word import RandomWords
from PyMultiDictionary import MultiDictionary

# Initialize the RandomWords and MultiDictionary objects
r = RandomWords()
dictionary = MultiDictionary()

def fetch_random_word():
    while True:
        word = r.get_random_word().upper()
        if get_word_info(word):
            return word

def get_word_info(word):
    meaning = dictionary.meaning('en', word.lower())
    synonyms = dictionary.synonym('en', word.lower())
    if meaning:
        # Extract the first definition from the dictionary
        definition = next(iter(meaning['definitions']))['definition']
        return definition, synonyms
    else:
        return None, None

def display_hangman(lives):
    stages = [
        '''
           -----
           |   |
           X   |
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
    lives = 7

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

    # Fetch and display the word definition and synonyms
    definition, synonyms = get_word_info(word)
    print(f"Definition of {word}: {definition}")
    if synonyms:
        print(f"Synonyms of {word}: {', '.join(synonyms)}")
    else:
        print(f"No synonyms found for {word}.")

def main():
    play_again = 'Y'
    while play_again.upper() == 'Y':
        word = fetch_random_word()
        play_game(word)
        play_again = input("Do you want to play again? (Y/N): ")

if __name__ == "__main__":
    main()
