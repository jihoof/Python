from setting import *
import random 
comp_word = "apple"
used = ["a", "b"]

def reveal_word(comp_word, used):
    for i in comp_word:
        if i not in used:
            print("_", end = " ")
        else:
            print(i, end = " ")

def print_status(comp_word, used, life):
    print("---------------------------------------------")
    print(f"Word: {reveal_word(comp_word, used)}")
    print(f"Used: {' '.join(used)}")
    print(f"Life: {life}")
    print("---------------------------------------------")

print_status(comp_word, used, LIFE)