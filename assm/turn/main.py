from Posmon import *
import os
import sys
import random
import time
import module
import rich

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
            rcomp_posmon = comp_list[comp_posmon]
            rplayer_posmon = player_list[player_posmon]
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
                    print(f'{rcomp_posmon.name}                 | {rcomp_posmon.type} {rcomp_posmon.health} / {rcomp_posmon.max_health}|')
                    print('                        VS')
                    print(f"{rplayer_posmon.name}                  | {rplayer_posmon.type} {rplayer_posmon.health} / {rplayer_posmon.max_health}|")
                    print(f'당신의 포스몬 [{player_str}] {len([x for x in player_str if x == 'O'])} / {len(player_list)}')
                    print('#'*40)
                    print("기술: ", end = "")
                    for i in range(len(rplayer_posmon.moves)):
                        print(f"({i}) {rplayer_posmon.moves[i].name}", end = " ")
                    print('\n'+'#'*40)
                    select = input('입력: ')


                    if 'o' in select:
                        tmp = select.split()
                        attack_num = int(tmp[1])
                        com_attack_num = random.randint(0,2)
                        rplayer_posmon_skill = rplayer_posmon.moves[attack_num]
                        rcomp_posmon_skill = rcomp_posmon.moves[com_attack_num]
                        if rplayer_posmon_skill.speed >= rcomp_posmon_skill.speed:
                            rplayer_posmon_skill.use(rplayer_posmon, rcomp_posmon, True)
                            module.enter()
                            rcomp_posmon_skill.use(rplayer_posmon, rcomp_posmon, False)
                            module.enter()
                        if rplayer_posmon_skill.speed < rcomp_posmon_skill.speed:
                            rcomp_posmon_skill.use(rplayer_posmon, rcomp_posmon, False)
                            module.enter()
                            rplayer_posmon_skill.use(rplayer_posmon, rcomp_posmon, True)
                            module.enter()
                    
                    if 'e' in select:
                        print('#' * 40)
                        for i in range(len(player_list)):
                            print(f'{(i)} {player_list[i].name}    |{player_list[i].type} {player_list[i].health} / {player_list[i].max_health}')
                        print('#' * 40)
                        module.enter()

                    if 's' in select:
                        tmp = select.split()
                        change_num = int(tmp[1])
                        player_posmon = change_num
                        rplayer_posmon = player_list[player_posmon]
                        module.enter()
                    

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
