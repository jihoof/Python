import random
from setting import *
import os
from IPython.display import clear_output

def clear_screen():
    os.system('cls') # Windows 콘솔 창에서 실행 시 주석 해제
    clear_output() # jupyter notebook 외 실행 시 주석 처리할 것
    return

def print_stairs(stair_num, com_move, player_move ):
    print(f"총 계단 수: {stair_num}")
    print(f"PLAYER:   ○ < {player_move}>")
    print(f"COMPUTER:   ● < {com_move}>")
    print()
    


def main():
    print("======================")
    print("[묵찌빠 계단 오르기]")
    print("======================")
    print("○          ●")
    print("█          █")
    print("██        ██")
    print("███      ███")
    print("████    ████")
    print("█████  █████")
    print("████████████")
    while True:
        stair_num = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> "))
        if stair_num <= 30 and stair_num >= 10:
            clear_screen()
            break
    


main()