"""
Main file of the game
"""

import random
import string
from words_list import *

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
  print(letters_in_word)
  print(word_to_use)
  print(alphabet)

main()


