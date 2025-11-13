from Posmon import *
import os
import sys
import random
import time
import module

posmon_list = []
comp_list = random.sample([Phoenix(), Normie(), Rocky(), Swania()], 3)

def main():
    run = True
    num_posmon = 0
    player_list = []

    while run:

        print('===================================')
        print('0. 포스몬 선택')
        print('1. 배틀하기')
        print('2. 종료하기')
        print('===================================')
        chose = module.input_int(0, 2, '입력: ', '잘못된 입력입니다. 다시 입력하세요.')
        module.enter()
        
        if chose == 0:
            player_list = []
            break_condition = False
            while True:
                if break_condition == True:
                    break

                print("-1. 종료")   
                print("0. Normie")
                print("1. Rocky")
                print("2. Phoenix")
                print("3. Swania")
                
                name_type = ["Normie", "Rocky", "Phoenix", "Swania"]
                while True:
                    num = module.input_int(-1, 3, '포스몬을 선택하세요: ', '잘못된 입력입니다.')

                    # 이미 선택한 포스몬일 때
                    if name_type[num] in [posmon.name for posmon in player_list]:
                        print("이미 선택하셨습니다. 다시하세요")
                        continue
                    else:
                        if num == -1:
                            if len(player_list) > 0:
                                print('포스몬 선택이 완료되었습니다.')
                                print(f"당신의 포스몬 목록: {' '.join([posmon.name for posmon in player_list])}") 
                                break_condition = True
                                module.enter()
                                break
                            else:
                                print('포스몬을 최소 한마리 선택하세요.')
                                continue

                        elif num == 0:
                            player_list.append(Normie())
                            print('선택되었습니다.')

                        elif num == 1:
                            player_list.append(Rocky())
                            print('선택되었습니다.')

                        elif num == 2:
                            player_list.append(Phoenix())
                            print('선택되었습니다.')
                            
                        elif num == 3:
                            player_list.append(Swania())
                            print('선택되었습니다.')

                        if len(player_list) >= 3:
                            print(f'당신의 포스몬 목록: {' '.join([posmon.name for posmon in player_list])}')
                            break_condition = True
                            module.enter()
                            break 
        
        elif chose == 1:
            comp_posmon = 0
            player_posmon = 0
            if len(player_list) <= 0:
                print('포스몬을 선택해주세요.')
                module.enter()
            else:
                print(f'당신의 포스몬 목록: {' '.join([posmon.name for posmon in player_list])}')
                print(f'컴퓨터의 포스몬 목록: {' '.join([posmon.name for posmon in comp_list])}')
                print()
                print('배틀이 시작됩니다.')
                while True:
                    comp_str = ''.join(["X" if posmon.health <= 0 else "O" for posmon in comp_list])
                    player_str = ''.join(["X" if posmon.health <= 0 else "O" for posmon in player_list])
                    print('#'*40)
                    print(f'컴퓨터 포스몬: [{comp_str}] {len([x for x in comp_str if x == "O"])} / 3')
                    print(f'{comp_list[comp_posmon].name}                 | {comp_list[comp_posmon].type} {comp_list[comp_posmon].health} / {comp_list[comp_posmon].max_health}|')
                    print('                        VS')
                    print(f"{player_list[player_posmon].name}                  | {player_list[player_posmon].type} {player_list[player_posmon].health} / {player_list[player_posmon].max_health}|")
                    print(f'당신의 포스몬 [{player_str}] {len([x for x in player_str if x == 'O'])} / {len(player_list)}')
                    print('#'*40)
                    print(f'기술: (0) {player_list[player_posmon].moves[0].name} (1)  {player_list[player_posmon].moves[1].name} (2) {player_list[player_posmon].moves[2].name}')
                    print('#'*40)
                    select = module.input_all(0, 2, '입력: ', '잘못된 입력입니다.', 'e, s')

                    if select == 0:
                        player_list[player_posmon].moves[select].use()

        elif chose == 2:
            time.sleep(0.7)
            module.clear()
            print('게임을 종료합니다.')
            time.sleep(0.5)
            print()
            print()
            time.sleep(0.5)
            print("게임을 종료 중...", end='', flush=True)  # flush 추가
            for _ in range(random.randint(5, 10)):
                print(".", end='', flush=True)
                time.sleep(1)
            print()
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

    
if __name__ == '__main__':
    main()
