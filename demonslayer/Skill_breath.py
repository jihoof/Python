from Skill import Skill

class DragonSunHaloHeadDance(Skill):
    def __init__(self):
        super().__init__("DragonSunHaloHeadDance")

    def attack_use(self, enemy, player):
        damage = self.calculate_damage(player, enemy)

        enemy.stat["Health"] -= damage
        

class FlashCut(Skill):
    def __init__(self):
        super().__init__("FlashCut")

    def attack_use(self, enemy ,player):
        damage = None