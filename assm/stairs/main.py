import random
import os
import rich

def print_scissors():
    print("┌────────────────────┐")
    print("│               ▩▩   │")
    print("│       ▩▩    ▩▩▩▩▩  │")
    print("│     ▩▩▩▩▩  ▩▩▩▩▩▩▩ │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩         │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩       │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│   ▩▩▩▩▩▩▩ ▩▩▩▩▩▩▩  │")
    print("│    ▩▩▩▩▩▩   ▩▩▩▩▩  │")
    print("│      ▩▩▩      ▩▩   │")
    print("└────────────────────┘")

def print_rock():
    print("┌────────────────────┐")
    print("│                    │")
    print("│     ▩▩▩▩▩          │")
    print("│    ▩▩▩▩▩▩▩▩▩       │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│   ▩▩▩▩▩▩▩▩▩▩       │")
    print("│    ▩▩▩▩▩▩▩         │")
    print("│                    │")
    print("└────────────────────┘")
    
def print_paper():
    print("┌───────────────────┐")
    print("│                   │")
    print("│     ▩▩▩▩▩         │")
    print("│    ▩▩▩            │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩  │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│    ▩▩▩▩▩          │")
    print("│                   │")
    print("└───────────────────┘")

def clear_screen():
    os.system('cls') # Windows 콘솔 창에서 실행 시 주석 해제
    return

def print_stairs(stair_number, comp_move, player_move ):
    
    print(f"총 계단 수: {stair_number}")
    print(f"PLAYER:   ○ < {player_move}>")
    print(f"COMPUTER:   ● < {comp_move}>")
    print()

    all_list = [[]]
    for _ in range(stair_number+1):
        all_list[0].append(" ")

    if stair_number % 2 != 0:
        for i in range(1, ((stair_number+1)//2) + 1):
            l = []
            for _ in range(i):
                l.append('■')
            for _ in range((stair_number+1)-(i*2)):
                l.append(" ")
            for _ in range(i):
                l.append('■')
            all_list.append(l)
            
    
    elif stair_number % 2 == 0:
        for i in range(1, (stair_number//2) + 1):
            l = []
            for _ in range(i):
                l.append('■')
            for _ in range((stair_number+1)-(i*2)):
                l.append(" ")
            for _ in range(i):
                l.append('■')
            all_list.append(l)
            

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
        print(*line, sep = '')

def enter(): #엔터키 입력받았을 때 clear
    while True:
        print("\n계속하려면 엔터를 눌러주세요...")
        enter = input("")
        if enter == "":
            os.system('cls')
            break

def comp_choose():
    comp_choose = random.choice(['가위','바위','보'])
    return comp_choose

def main():
    player_move = 0
    comp_move = 0

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

    print_stairs(stair_num, comp_move, player_move)
    enter()
    
    who_win = None

    while True:

        print('[공격권 결정 가위바위보]')
        player_choice = input('가위, 바위, 보 중 하나 선택: ')
        comp_choice = comp_choose()

        print('[컴퓨터 선택]')
        if comp_choice == '가위':
            print_scissors()
        elif comp_choice == '바위':
            print_rock()
        else:
            print_paper()
        
        print('[플레이어 선택]')
        if player_choice == '가위':
            print_scissors()
        elif player_choice == '바위':
            print_rock()
        else:
            print_paper()

        # 승리 규칙 딕셔너리 (key가 value를 이김)
        rules = {
            '가위': '보',
            '바위': '가위',
            '보': '바위'
        }

        if comp_choice == player_choice:
            print('[결과] 무승부입니다.')
            enter()
            continue

        else:
            if rules[comp_choice] == player_choice:
                print('[결과] 컴퓨터 공격, 플레이어 수비입니다.')
                enter()
                who_win = 'comp'
            else:
                print('[결과] 플레이어 공격, 컴퓨터 수비입니다.')
                enter()
                who_win = 'player'

        move_win = 1
        while True:
            print('[묵찌빠]')
            print(f'승리 시 이동 칸 수:  {move_win}')
            if who_win == 'comp':
                print('컴퓨터 공격, 플레이어 수비입니다.')
            else:
                print('플레이어 공격, 컴퓨터 수비입니다.')
            player_choice = input('가위, 바위, 보 중 하나 선택: ')
            comp_choice = comp_choose()

            print('[컴퓨터 선택]')
            if comp_choice == '가위':
                print_scissors()
            elif comp_choice == '바위':
                print_rock()
            else:
                print_paper()
            
            print('[플레이어 선택]')
            if player_choice == '가위':
                print_scissors()
            elif player_choice == '바위':
                print_rock()
            else:
                print_paper()

            if player_choice == comp_choice:
                print('[결과] 묵찌빠 종료')
                if who_win == 'comp':
                    print(f'컴퓨터 승, {move_win}칸 이동합니다.')
                    print()
                else:
                    print(f'플레이어 승, {move_win}칸 이동합니다.')
                    print()                
                enter()

            else:
                if rules[comp_choice] == player_choice:
                    print('[결과] 컴퓨터 공격, 플레이어 수비입니다.')
                    who_win = 'comp'
                else:
                    print('[결과] 플레이어 공격, 컴퓨터 수비입니다.')
                    who_win = 'player'
                    
                enter()
                move_win += 1
                continue

main()

