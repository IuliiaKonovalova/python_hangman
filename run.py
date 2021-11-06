"""
Main file of the game
"""

import random
import string
import words_list

def get_valid_word():
    """
    Check whether the word is valid
    for the game
    """
    word = random.choice(words_list)
    while '-' in words_list or ' ' in words_list:
        word = random.choice(words_list)
    return word.upper()




