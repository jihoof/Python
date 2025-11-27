from Skill_breath import DragonSunHaloHeadDance
from load import game_dict
import json

class Character:
    def __init__(self, name):
        self.name = name
        self.stat = {}
        self.skill = [DragonSunHaloHeadDance()]
        self.effect_on_object = []
        self.init_stat([100, 50, 30, 20, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ])
    
    def init_stat(self, stat_list):
        for i, key in enumerate(game_dict.keys()):                
            self.stat[key] = stat_list[i]
            if key == "RedSword":
                break
            
        print(json.dumps(self.stat, indent=4, ensure_ascii=False))
    
    def next_turn(self):
        print("턴이 지났습니다")
        for passive in self.effect_on_object:
            passive[1] -= 1
        
        for passive in self.effect_on_object:
            if passive[1] == 0:
                self.stat[passive[0]] = self.original_stat(self.stat[passive[0]], passive[2])
                self.effect_on_object.remove(passive)
                
if __name__ == "__main__":
    player = Character("Tanjiro Kamado")

    choice = int(input("Choose a skill (0: DragonSunHaloHeadDance, 1: FlashCut): "))
    selected_skill = player.skill[choice]

    selected_skill.status_use(player, None)