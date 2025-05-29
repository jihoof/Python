from setting import *
import random 

def reveal_word(comp_word, used):
    for i in comp_word:
        if i not in used:
            print("_", end = " ")
        else:
            print(i, end = " ")
    return ""

def print_status(comp_word, used, life):
    print("---------------------------------------------")
    print(f"Word: ", end = ' ')
    reveal_word(comp_word, used)
    print()
    print(f"Used: {' '.join(used)}")
    print(f"Life: {life}")
    print("---------------------------------------------")

def is_word_guessed(comp_word, used):
    tmp = list(comp_word)
    tmp2 = len(tmp)
    tmp3 = 0
    for i in used:
        if i in comp_word:
            tmp3 += 1
    if tmp3 == tmp2:
        return True
    else:
        return False

play_again = "none"

intel_setup = True
run = True
while run:
    if intel_setup == True:
        comp_word = random.choice(WORD_LIST)
        print("Hangman game starts!")
        USED = []
        LIFE = 10
        intel_setup = False
    else:
        pass

    print_status(comp_word, USED, LIFE)
    word_guessed = is_word_guessed(comp_word, USED)

    if LIFE == 0:
        print(f"The answer was {comp_word}. ")
        play_again = input("Do you want to play another game? ")
    elif word_guessed == True:
        print("Hangman Survived!")
        play_again = input("Do you want to play another game? ")

    if play_again == "yes":
        intel_setup = True
        play_again = "none"
        continue
    elif play_again == "no":
        break


    player_word = input("Choose a character: ")
    if player_word in USED:
        print("You have already checked this character. Try another one.")
        continue
    else:
        if player_word not in comp_word:
            LIFE -= 1
        USED.append(player_word)
    
    if play_again == "yes":
        intel_setup = True
        play_again = "none"
        continue
    elif play_again == "no":
        break

