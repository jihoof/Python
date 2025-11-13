import os
import sys
import math
import random
from posmon import *
from phs import *
from sts import *

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

import module

posmon_list = []
comp_list = random.sample([Phoenix(), Normie(), Rocky(), Swania()], 3)
player_list = []

def main():
    run = True
    num_posmon = 0

    while run:

        print('===================================')
        print('0. 포스몬 선택')
        print('1. 배틀하기')
        print('2. 종료하기')
        print('===================================')
        chose = module.input_int(0, 2, '입력: ', '잘못된 입력입니다. 다시 입력하세요.')
        module.enter()
        
        if chose == 0:
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
                            print('포스몬 선택이 완료되었습니다.')
                            time.sleep(0.3)
                            print('포스몬들에게는 귀속저주가 붙어있습니다.')
                            time.sleep(0.3)
                            print('한번 입양한 포스몬을 유기 할 수 없습니다.')
                            time.sleep(0.3)
                            print(f'당신의 포스몬 목록: {' '.join([posmon.name for posmon in player_list])}')
                            break_condition = True
                            module.enter()
                            break 
        
        elif chose == 1:
            comp_posmon = 0
            player_posmon = 0
            if len(posmon_list) <= 0:
                print('포스몬을 선택해주세요.')
                module.enter()
            else:
                print(f'당신의 포스몬 목록: {' '.join(posmon_list)}')
                print(f'컴퓨터의 포스몬 목록: {' '.join([posmon.name for posmon in comp_list])}')
                print()
                print('배틀이 시작됩니다.')
                while True:
                    comp_str = ''.join(["X" if posmon.health <= 0 else "O" for posmon in posmon_list])
                    comp_left = None
                    print('################################')
                    print(f'컴퓨터 포스몬: [{comp_str}]  / 3')
                    print(f'{comp_list[comp_posmon].name}                 {comp_list[comp_posmon].name} {comp_list[comp_posmon].health} / {comp_list[comp_posmon].max_health}|')
                    print('                        VS')
                    #선생님 마저 구현해주세요.

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
