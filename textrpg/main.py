import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
mpPlayer = player()

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command. ')
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('#' * 20)
    print('# Welcom to the Text RPG! #')
    print('#' * 20)
    print('           - Play -            ')
    print('           - Help -            ')
    print('           - Quit -            ')
    print('    Copyright 2017 btong.me    ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print('#' * 20)
    print('# Welcom to the Text RPG! #')
    print('#' * 20)
    print(' # Use up, down, left, right to move #')
    print(' # Type your commands to them # ')
    print(' # Use "lock" to inspect something # ')
    print(' # Good luck and have fun! # ')
    title_screen_selections()

def start_game():
    pass


DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {

    'a1': False, 'a2': False 

}