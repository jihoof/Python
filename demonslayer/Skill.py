from load import game_dict

class Skill:
    def __init__(self, skill_name):
        self.skill_name = skill_name
        
        self.detail = game_dict[skill_name]["detail"]
        self.selfEffect = game_dict[skill_name]["selfEffect"]
        self.enemyStatus = game_dict[skill_name]["enemyStatus"]
        self.enemyDamage = game_dict[skill_name]["enemyDamage"]
        
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
            player.effect_on_object.append([field, turn, effect_str])  
            
        for field, stat_str in self.enemyStatus.items():
            effect_str, turn = stat_str[0], stat_str[1]      
            enemy.stat[field] = self.change_stat(player.stat[field], effect_str)
            enemy.effect_on_object.append([field, turn, effect_str])  
    
    def change_stat(self, player_stat, stat_str):
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


    def calculate_damage(self, player, enemy):
        
        damage = (((player.stat["BreathLevel"] * self.BreathMultiplier) + (player.stat["PhysicalAilities" * self.MartialMultiplier])) * enemy.stat["DamageTakenMultiplier"]) * player.stat["DamageDealMultiplier"]

        return damage