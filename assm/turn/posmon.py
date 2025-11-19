from Phs import *
from Sts import *

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
        self.default_attack = attack
        self.default_defence = defence
    
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
            self.attack = self.default_attack
            self.defence = self.default_defence


class Phoenix(Posmon):
    def __init__(self):
        super().__init__(86, 86, 20, 23, [FireBress(), Growl(), SwordDance()], 'Phoenix', 'Fire') 

class Normie(Posmon):
    def __init__(self):
        super().__init__(80, 80, 20, 20, [Tackle(), Swift(), TailWhip()], 'Normie', 'Normal')

class Rocky(Posmon):
    def __init__(self):
        super().__init__(85, 85, 15, 25, [Tackle(), Growl(), TailWhip()], 'Rocky', 'Water')

class Swania(Posmon):
    def __init__(self):
        super().__init__(80, 80, 30, 10, [ScissorsCross(), SwordDance(), Tackle()], 'Swania', 'Grass')






