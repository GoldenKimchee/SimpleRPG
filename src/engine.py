import typing
import time
import sys
import os
import textwrap

"""Defines methods that run the main game."""

def type(string: typing.Sequence, width: int = 30):
    """Prints out letters one by one to console."""
    wrapped_text = textwrap.wrap(string, width) # Creates a list with each item being no longer than 30 indexes
    for line in wrapped_text: # For each line,
        for character in line: # print each character one by one
            sys.stdout.write(character)
            sys.stdout.flush()
            if character in ["!", ".", ",", "?"]:
                time.sleep(0.3)
            time.sleep(0.05) # Waits in between each letter typed (in seconds)
        print() # since textwrap.wrap does not include \n

def slow_type(string: typing.Sequence, width: int = 30):
    """Prints out letters one by one to console slowly."""
    wrapped_text = textwrap.wrap(string, width)
    for line in wrapped_text:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            if character in ["!", ".", ",", "?"]:
                time.sleep(0.3)
            time.sleep(0.3) # Waits longer between each letter typed
        print()

def custom_type(string: typing.Sequence, speed: int, float, pause: int = 0.3, width: int = 30):
    """Prints out letters one by one to console at speed specified."""
    wrapped_text = textwrap.wrap(string, width)
    for line in wrapped_text:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            if character in ["!", ".", ",", "?"]:
                time.sleep(pause)
            time.sleep(speed) # Waits whatever time the user specifies
        print()

def clear():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # if microsoft, use cls. if linux/mac, use clear.

def get_input(responses: list) -> str:
    """responses will be a list of options, gets input until it matches an option"""
    user_response = ""
    while user_response.strip() not in responses: # continue prompting input until it matches a response
        print("> ", end= "")
        user_response = input()
    return user_response
