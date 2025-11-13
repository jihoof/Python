import sys
import os
import time
import phs
import sts

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

import module

class Posmon:
    def __init__(self, health, max_health, attack, defence, moves, name, type):
        
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defence = defence
        self.moves = moves
        self.name = name
        self.type = type
        self.burnt = False
    
    def get_name(self) -> str:
        return self.name
    
    def get_max_health(self) -> int:
        return self.max_health
    
    def get_type(self) -> str:
        return self.type
    
    def reset_status(self, reset_health:bool = False):
        if reset_health == 'True':
            self.health = self.max_health
        else:
            pass

class Phoenix(Posmon):
    def __init__(self):
        super().__init__(86, 86, 20, 23, [phs.FireBress(), sts.Growl(), sts.SwordDance()], 'Phoenix', 'Fire') 

class Normie(Posmon):
    def __init__(self):
        super().__init__(80, 80, 20, 20, [phs.Tackle(), phs.Swift(), sts.TailWhip()], 'Normie', 'Normal')

class Rocky(Posmon):
    def __init__(self):
        super().__init__(85, 85, 15, 25, [phs.Tackle(), sts.Growl(), sts.TailWhip()], 'Rocky', 'Water')

class Swania(Posmon):
    def __init__(self):
        super().__init__(80, 80, 30, 10, [phs.ScissorsCross(), sts.SwordDance(), phs.Tackle], 'Swania', 'Grass')


# nomarl 받는거 주는 피해 1배 
#풀은 물한테 2배, 물은 불한테 2배 불은 풀한테 2배
#불은 물한테 0.5배 물은 풀한테 0.5배, 풀은 불한테 0.5배

def get_attack_ratio(attacker_type, defender_typer):
    if attacker_type == 'fire' and defender_typer == 'grass':
        attack_ratio = 2
    elif attacker_type == 'fire' and defender_typer == 'water':
        attack_ratio = 0.5
    elif attacker_type == 'water' and defender_typer == 'fire':
        attack_ratio = 2
    elif attacker_type == 'water' and defender_typer == 'grass':
        attack_ratio = 0.5
    elif attacker_type == 'grass' and defender_typer == 'water':
        attack_ratio = 2
    elif attacker_type == 'grass' and defender_typer == 'fire':
        attack_ratio = 0.5
    else:
        attack_ratio = 1

    return attack_ratio


class Move():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return self.name
    
    def get_speed(self) -> str:
        return self.speed
    
    def use(self, our_posmon:Posmon, oppnent_posmon:Posmon, is_player_move=True):
        pass





