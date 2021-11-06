"""
Main file of the game
"""

import random
import string
from words_list import *
from colorama import Fore, Style

def get_valid_word():
    """
    Check whether the word is valid for the game
    """
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word.upper()

def main():
    word_to_use = get_valid_word()
    letters_in_word = set(word_to_use)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print(letters_in_word)
    print(word_to_use)
    print(alphabet)
    
    lives = 6

    while len(letters_in_word) > 0 and lives > 0:
        # Loops till the conditions are met
        # Print reminded lives
        print(f'''
{Style.BRIGHT}Lives: {Fore.RED}{lives}{Fore.WHITE}
''')
        # Print used letters
        if len(used_letters) > 0:
            print(f'''
You've used these letters: {' '.join(used_letters)}
            ''')
        # Get the hidden word
        secret_word = [letter if letter in used_letters else '_' for letter in word_to_use]
        print(f'''Current word: {' '.join(secret_word)}''')
        # Get user input
        user_guess = input('Guess a letter: ').upper()
        # Check if the user input is valid
        if user_guess in alphabet - used_letters:
            # Add user input to the used_letters set
            used_letters.add(user_guess)
            # if guess is correct remove from user_guess
            if user_guess in letters_in_word:
                letters_in_word.remove(user_guess)
                if len(letters_in_word) == 0:
                  print(f'''
You guessed correctly!
The word was {word_to_use}
Lives left: {lives}
                  ''')
            # Otherwise, reduce lives
            else:
                lives -= 1
        elif user_guess in used_letters:
            print("You've already used it!")
        else:
            print('invalid')
        
    if lives == 0:
      print(f'''You've died! The word was: {word_to_use}''')
main()


