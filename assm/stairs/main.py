import random
import os

def clear_screen():
    os.system('cls') # Windows 콘솔 창에서 실행 시 주석 해제
    return

def print_stairs(stair_number, comp_move, player_move ):
    print(f"총 계단 수: {stair_number}")
    print(f"PLAYER:   ○ < {player_move}>")
    print(f"COMPUTER:   ● < {comp_move}>")
    print()

    all_list = [[] for i in range(stair_number+2)]
    for _ in range(stair_number+1):
        all_list[0].append(" ")
    if stair_number % 2 != 0:
        for i in range(1, ((stair_number+1)//2) + 1):
            for _ in range(i):
                all_list[i].append('■')
            for _ in range((stair_number+1)-(i*2)):
                all_list[i].append(" ")
            for _ in range(i):
                all_list[i].append('■')
    
    elif stair_number % 2 == 0:
        for i in range(1, (stair_number//2) + 1):
            for _ in range(i):
                all_list[i].append('■')
            for _ in range((stair_number+1)-(i*2)):
                all_list[i].append(" ")
            for _ in range(i):
                all_list[i].append('■')

    if comp_move + player_move != stair_number:
        if player_move <= (stair_number-1) // 2:
            all_list[player_move][player_move] =  "○"
        elif player_move > (stair_number-1) // 2:
            all_list[stair_number-player_move][player_move] = "○"
        if comp_move >(stair_number-1) // 2:
            all_list[stair_number-comp_move][-comp_move-1] =  "●"
        elif comp_move <= (stair_number-1) // 2:
            all_list[comp_move][-comp_move-1] = "●"

    else:
        if player_move <= (stair_number-1) // 2:
            all_list[player_move][player_move] =  "◴"
        elif player_move > (stair_number-1) // 2:
            all_list[stair_number-player_move][player_move] = "◴"

    for line in all_list:
        for i in line:
            print(i,end = '')
        print()
    
# def main():
#     player_move = 0
#     comp_move = 0

#     print("======================")
#     print("[묵찌빠 계단 오르기]")
#     print("======================")
#     print("○          ●")
#     print("█          █")
#     print("██        ██")
#     print("███      ███")
#     print("████    ████")
#     print("█████  █████")
#     print("████████████")
#     while True:
#         stair_num = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> "))
#         if stair_num <= 30 and stair_num >= 10:
#             clear_screen()
#             break

#     print_stairs(stair_num, comp_move, player_move)


# main()

print_stairs(25, 0, 0)