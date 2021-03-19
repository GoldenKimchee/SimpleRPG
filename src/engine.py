import typing
import time
import sys
import os
import textwrap

def type(string: typing.Sequence):
    wrapped_text = textwrap.wrap(string, 30)
    for line in wrapped_text:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
def slow_type(string: typing.Sequence):
    wrapped_text = textwrap.wrap(string, 30)
    for line in wrapped_text:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # if microsoft, use cls. if linux/mac, use clear.