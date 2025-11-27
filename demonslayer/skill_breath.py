import os
import sys
import math
import status_effect
import module
import character
import json

with open(os.path.join(os.path.dirname(__file__), 'dictionary.json'), 'r', encoding='utf-8') as f:
    game_dict = json.load(f)

class Skill:
    def __init__(self, skill_name):
        self.skill_name = skill_name
        
        self.detail = game_dict[skill_name]["detail"]
        self.selfEffect = game_dict[skill_name]["selfEffect"]
        
        self.enemyStatus = game_dict[skill_name]["enemyStatus"]
        self.enemyDamage = game_dict[skill_name]["enemyDamage"]
        
        # Enemy status & damage stats
        self.BreathMultiplier = self.enemyDamage['BreathMultiplier']
        self.MartialMultiplier = self.enemyDamage['MartialMultiplier']
        self.RegenerationInhibitionLevel = self.enemyStatus['RegenerationInhibitionLevel']
        self.BrandOfTheSunLevel = self.enemyStatus['BrandOfTheSunLevel']
    
    def status_use(self, player, enemy):
        for field, stat_str in self.selfEffect.items():
            effect_str, turn = stat_str[0], stat_str[1]      
            player.stat[field] = self.change_stat(player.stat[field], effect_str)
            player.passive_list.append([field, turn, effect_str])  
            
        for field, stat_str in self.enemyEffect.items():
            effect_str, turn = stat_str[0], stat_str[1]      
            enemy.stat[field] = self.change_stat(player.stat[field], effect_str)
            enemy.passive_list.append([field, turn, effect_str])  
    
    def change_stat(self, stat_str, player_stat):
        if type(stat_str) == bool:
            return stat_str

        elif 'x' in stat_str:
            multiplier = float(stat_str.split('_')[1])
            return player_stat * multiplier

        elif '+' in stat_str:
            addition = float(stat_str.split('_')[1])
            return player_stat + addition

        elif '-' in stat_str:
            subtraction = float(stat_str.split('_')[1])
            return player_stat - subtraction
        
    def original_stat(self, player_stat, stat_str):
        if type(stat_str) == bool:
            return not stat_str
        
        elif 'x' in stat_str:
            multiplier = float(stat_str.split('_')[1])
            return player_stat / multiplier
        
        elif '+' in stat_str:
            addition = float(stat_str.split('_')[1])
            return player_stat - addition
        
        elif '-' in stat_str:
            subtraction = float(stat_str.split('_')[1])
            return player_stat + subtraction


class DragonSunHaloHeadDance(Skill):
    def __init__(self):
        super().__init__("DragonSunHaloHeadDance")

    def attack_use(self, enemy, player):
        damage = None

class FlashCut(Skill):
    def __init__(self):
        super().__init__("FlashCut")

    def attack_use(self, enemy, player):
        damage = None

class Character:
    def __init__(self, name):
        self.name = name
        self.stat = {}
        self.skill = [DragonSunHaloHeadDance()]
        self.passive_list = []
        self.init_stat([100, 50, 30, 20, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ])
    
    def init_stat(self, stat_list):
        for i, key in enumerate(game_dict.keys()):                
            self.stat[key] = stat_list[i]
            if key == "RedSword":
                break
            
        print(json.dumps(self.stat, indent=4, ensure_ascii=False))
        
player = Character("Tanjiro Kamado")

choice = int(input("Choose a skill (0: DragonSunHaloHeadDance, 1: FlashCut): "))
selected_skill = player.skill[choice]

selected_skill.status_use(player, None)