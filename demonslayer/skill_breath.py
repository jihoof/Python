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
    def change_stat(self,stat_str, player_stat):
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
        
    def original_stat(player_stat, stat_str):
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
        self.name = game_dict["DragonSunHaloHeadDance"]["name"]
        self.detail = game_dict["DragonSunHaloHeadDance"]["detail"]
        self.selfEffect = game_dict["DragonSunHaloHeadDance"]["selfEffect"]
        self.enemyEffect = game_dict["DragonSunHaloHeadDance"]["enemyEffect"]

    def status_use(self, player, enemy):
        for field, stat_str in self.selfEffect.items():
            effect_str, turn = stat_str[0], stat_str[1]      
            player.stat[field] = self.change_stat(player.stat[field], effect_str)
            player.passive_list.append([field, turn, effect_str])  
            
        for field, stat_str in self.enemyEffect.items():
            effect_str, turn = stat_str[0], stat_str[1]      
            enemy.stat[field] = self.change_stat(player.stat[field], effect_str)
            enemy.passive_list.append([field, turn, effect_str])  

    def attack_use(self, enemy, player):
        Breath_damage_mulitiplier = self.enemyEffect["BreathMultiplier"]
        
        