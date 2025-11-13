import sys
import os
import time
from posmon import *

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

import module

class PhysicalMove(Move):
    def __init__(self, power, name, speed):
        super().__init__(name, speed)
        self.power = power

    def get_power(self) -> int:
        return self.power
    


class Tackle(PhysicalMove):
    def __init__(self):
        super().__init__(power=25, name="Tackle", speed = 0)

    def use(self, our_posmon:Posmon, ai_posmon:Posmon, is_player_move=True):

        if is_player_move == True:
            attack_ratio = get_attack_ratio(our_posmon.type, ai_posmon.type)
            original_health = ai_posmon.health
            ai_posmon.health -= max(self.power + our_posmon.attack - ai_posmon.defence) * attack_ratio
            print(f'당신의 포스몬이 태클을 사용합니다.')  
            print(f'상대 포스몬의 체력이 감소합니다. ({ai_posmon.health} <- {original_health} )')
        else:
            attack_ratio = get_attack_ratio(ai_posmon.type, our_posmon.type)
            original_health = our_posmon.health
            our_posmon.health -= max(self.power + ai_posmon.attack - our_posmon.defence) * attack_ratio
            print(f'상대의 포스몬이 태클을 사용합니다.')  
            print(f'당신의 포스몬의 체력이 감소합니다. ({our_posmon.health} <- {original_health} )')
            

            
                

class ScissorsCross(PhysicalMove):
    def __init__(self):
        super().__init__(power = 30, name="ScissorsCross", speed = 0)

    def use(self, our_posmon:Posmon, ai_posmon:Posmon, is_player_move=True):

        if is_player_move == True:
            attack_ratio = get_attack_ratio(our_posmon.type, ai_posmon.type)
            original_health = ai_posmon.health
            ai_posmon.health -= max(self.power + our_posmon.attack - ai_posmon.defence) * attack_ratio
            print(f'당신의 포스몬이 시저크로스를 사용합니다.')  
            print(f'상대 포스몬의 체력이 감소합니다. ({ai_posmon.health} <- {original_health} )')
        else:
            attack_ratio = get_attack_ratio(ai_posmon.type, our_posmon.type)
            original_health = our_posmon.health
            our_posmon.health -= max(self.power + ai_posmon.attack - our_posmon.defence) * attack_ratio
            print(f'상대의 포스몬이 시저크로스를 사용합니다.')  
            print(f'당신의 포스몬의 체력이 감소합니다. ({our_posmon.health} <- {original_health} )')
            
    
class Swift(PhysicalMove):
    def __init__(self):
        super().__init__(power = 0, name = 'Swift', speed = 3)
         
    def use(self, our_posmon:Posmon, ai_posmon:Posmon, is_player_move=True):

        if is_player_move == True:
            attack_ratio = get_attack_ratio(our_posmon.type, ai_posmon.type)
            original_health = ai_posmon.health
            ai_posmon.health -= max(self.power + our_posmon.attack - ai_posmon.defence) * attack_ratio
            print(f'당신의 포스몬이 스피드스타를 사용합니다.')  
            print(f'상대 포스몬의 체력이 감소합니다. ({ai_posmon.health} <- {original_health} )')
        else:
            attack_ratio = get_attack_ratio(ai_posmon.type, our_posmon.type)
            original_health = our_posmon.health
            our_posmon.health -= max(self.power + ai_posmon.attack - our_posmon.defence) * attack_ratio
            print(f'상대의 포스몬이 스피드스타를 사용합니다.')  
            print(f'당신의 포스몬의 체력이 감소합니다. ({our_posmon.health} <- {original_health} )')
            
class FireBress(PhysicalMove):
    def __init__(self):
        super().__init__(power = 40, name = 'FireBress', speed = 5)
    
    def use(self, our_posmon:Posmon, ai_posmon:Posmon, is_player_move = True):

        if is_player_move == True:
            attack_ratio = get_attack_ratio(our_posmon.type, ai_posmon.type)
            original_health = ai_posmon.health
            ai_posmon.health -= max(self.power + our_posmon.attack - ai_posmon.defence) * attack_ratio
            burnt = module.chance(50)
            if burnt == True and ai_posmon.burnt == False:
                ai_posmon.burnt = True
            else:
                pass

            print(f'당신의 포스몬이 화염의 호흡 오의 • 제9의 형 「연옥」을 사용합니다.')  
            print(f'상대 포스몬의 체력이 감소합니다. ({ai_posmon.health} <- {original_health} )')

        else:
            attack_ratio = get_attack_ratio(our_posmon.type, ai_posmon.type)
            original_health = ai_posmon.health
            our_posmon.health -= max(self.power + ai_posmon.attack - our_posmon.defence) * attack_ratio
            burnt = module.chance(50)
            if burnt == True and ai_posmon.burnt == False:
                ai_posmon.burnt = True
            else:
                pass

            print(f'당신의 포스몬이 화염의 호흡 오의 • 제9의 형 「연옥」을 사용합니다.')  
            print(f'상대 포스몬의 체력이 감소합니다. ({our_posmon.health} <- {original_health} )')