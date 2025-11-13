class Move:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return self.name
    
    def get_speed(self) -> str:
        return self.speed
    
    def use(self) -> None:
        pass

    def get_attack_ratio(self, attacker_type, defender_typer):
        '''
            nomarl 받는거 주는 피해 1배 
            풀은 물한테 2배, 물은 불한테 2배 불은 풀한테 2배
            불은 물한테 0.5배 물은 풀한테 0.5배, 풀은 불한테 0.5배
        '''
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
