import time
from Move import Move
import module

class StatusMove(Move):
    def __init__(self, speed, name):
        super().__init__(name, speed)

class Growl(StatusMove):
    def __init__(self):
        super().__init__(name = 'Growl', speed = 1)
    
    def use(self, our_posmon, ai_posmon, is_player_move = True):
        if is_player_move == True:
            if our_posmon.defence <= 1:
                print(f'{our_posmon.name}이 {self.name}을/를 사용합니다.')
                time.sleep(0.5)
                print(f'상대의 포스몬의 공격력이 이미 최소치입니다. 방어력이 감소하지 않습니다.')
                time.sleep(0.3)
                module.enter()
            else:
                cur_attack = ai_posmon.attack
                ai_posmon.attack -= 5
                print(f'{our_posmon.name}이 {self.name}을/를 사용합니다.')
                time.sleep(0.5)
                print(f'상대의 포스몬의 공격력이 5 감소합니다. {cur_attack} -> {ai_posmon.attack} ')
                time.sleep(0.3)
                module.enter()  
        else:
            if our_posmon.defence <= 1:
                print(f'{ai_posmon.name}이 {self.name}을/를 사용합니다.')
                time.sleep(0.5)
                print(f'당신의 포스몬의 공격력이 이미 최소치입니다. 방어력이 감소하지 않습니다.')
                time.sleep(0.3)
                module.enter()
            else:
                cur_attack = our_posmon.attack
                our_posmon.attack -= 5
                print(f'{ai_posmon.name}이 {self.name}을/를 사용합니다.')
                time.sleep(0.5)
                print(f'당신의 포스몬의 공격력이 5 감소합니다. {cur_attack} -> {our_posmon} ')
                time.sleep(0.3)
                module.enter() 

class SwordDance(StatusMove):
    def __init__(self):
        super().__init__(name = 'SwordDance', speed = 0)

    def use(self, our_posmon, ai_posmon, is_player_move = True):
        if is_player_move == True:
            cur_attack = our_posmon.attack
            our_posmon.attack += 10
            print(f'{our_posmon.name}이 {self.name}을/를 사용합니다.')
            time.sleep(0.5)
            print(f' 당신의 포스몬의 공격력이 10 증가합니다. {cur_attack} -> {our_posmon.attack} ')
            time.sleep(0.3)
            module.enter()  
        else:
            cur_attack = ai_posmon.attack
            ai_posmon.attack += 10
            print(f'{ai_posmon.name}이 {self.name}을/를 사용합니다.')
            time.sleep(0.5)
            print(f'상대의 포스몬의 공격력이 10 증가합니다. {cur_attack} -> {ai_posmon} ')
            time.sleep(0.3)
            module.enter()   

class TailWhip(StatusMove):
    def __init__(self):
        super().__init__(name = 'TailWhip', speed = 1)
    
    def use(self, our_posmon, ai_posmon, is_player_move = True):
        if is_player_move == True:
            angry = module.chance(50)
            if angry == True:
                cur_attack = ai_posmon.attack
                ai_posmon.attack += 5
                print(f'{our_posmon.name}이 {self.name}을/를 사용합니다.')
                time.sleep(0.5)
                print(f'상대의 포스몬이 당신의 포스몬의 애교를 보고 분노를 표출합니다. {cur_attack} -> {ai_posmon.attack}')
                time.sleep(0.3)
                module.enter()
            else:
                if our_posmon.defence <= 1:
                    print(f'{our_posmon.name}이 {self.name}을/를 사용합니다.')
                    time.sleep(0.5)
                    print(f'상대의 포스몬의 방어력이 이미 최소치입니다. 방어력이 감소하지 않습니다.')
                    time.sleep(0.3)
                    module.enter()
                else:
                    cur_defence = ai_posmon.defence
                    ai_posmon.defence -= 5
                    print(f'{our_posmon.name}이 {self.name}을/를 사용합니다.')
                    time.sleep(0.5)
                    print(f'상대의 포스몬의 방어력이 감소합니다. {cur_defence} -> {ai_posmon.defence}')
                    time.sleep(0.3)
                    module.enter()
        
        else:
            if angry == True:
                cur_attack = our_posmon.attack
                our_posmon.attack += 5
                print(f'{ai_posmon.name}이 {self.name}을/를 사용합니다.')
                time.sleep(0.5)
                print(f'당신의 포스몬이 상대의 포스몬의 애교를 보고 분노를 표출합니다. {cur_attack} -> {our_posmon.attack}')
                time.sleep(0.3)
                module.enter()
            else:
                if our_posmon.defence <= 1:
                    print(f'{ai_posmon.name}이 {self.name}을/를 사용합니다.')
                    time.sleep(0.5)
                    print(f'당신의 포스몬의 방어력이 이미 최소치입니다. 방어력이 감소하지 않습니다.')
                    time.sleep(0.3)
                    module.enter()
                else:
                    cur_defence = our_posmon.defence
                    our_posmon.defence -= 5
                    print(f'당신의 포스몬의 방어력이 감소합니다. {cur_defence} -> {our_posmon.defence}')
