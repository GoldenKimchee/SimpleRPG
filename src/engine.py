import typing
import time
import sys
import os
import textwrap

"""Defines methods that run the main game."""

def type(string: typing.Sequence):
    """Prints out letters one by one to console."""
    wrapped_text = textwrap.wrap(string, 30) # Creates a list with each item being no longer than 30 indexes
    for line in wrapped_text: # For each line,
        for character in line: # print each character one by one
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05) # Waits in between each letter typed (in seconds)
        print()

def slow_type(string: typing.Sequence):
    """Prints out letters one by one to console slowly."""
    wrapped_text = textwrap.wrap(string, 30)
    for line in wrapped_text:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.3) # Waits longer between each letter typed
        print()

def custom_type(string: typing.Sequence, speed: int, float):
    """Prints out letters one by one to console at speed specified."""
    wrapped_text = textwrap.wrap(string, 30)
    for line in wrapped_text:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(speed) # Waits whatever time the user specifies
        print()

def clear():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # if microsoft, use cls. if linux/mac, use clear.