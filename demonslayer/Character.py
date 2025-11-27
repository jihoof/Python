from Skill_breath import DragonSunHaloHeadDance
from load import game_dict
import json
from rich.console import Console
from rich.table import Table


class Character:
    def __init__(self, name, skill, stat_list):
        self.name = name
        self.stat = {}
        self.skill = skill
        self.effect_on_object = []
        self.init_stat(stat_list)
    
    def init_stat(self, stat_list):
        for i, key in enumerate(game_dict.keys()):                
            self.stat[key] = stat_list[i]
            if key == "RedSword":
                break
    
    def next_turn(self):
        print("턴이 지났습니다")
        for passive in self.effect_on_object:
            passive[1] -= 1
        
        for passive in self.effect_on_object:
            if passive[1] == 0:
                self.stat[passive[0]] = self.original_stat(self.stat[passive[0]], passive[2])
                self.effect_on_object.remove(passive)

    def print_status(self):
        console = Console()

        table = Table(title=f"[bold yellow]{self.name} Status[/bold yellow]", expand=True)

        table.add_column("Stat", justify="left", style="cyan", no_wrap=True)
        table.add_column("Value", justify="center", style="bold white")
        table.add_column("Description", justify="left", style="green")

        for key, value in self.stat.items():
            desc = self.stat.get(key, "No description")
            table.add_row(key, str(value), desc)

        console.print(table)



class R(Character):
    def __init__(self, name, skill, stat_list):
        super().__init__(name, skill, stat_list)

class Tanjiro(R):
    def __init__(self):
        skill = [DragonSunHaloHeadDance()]
        stat_list = [1, 1, 1, 1500, 1500, 100, 20, 1500, 1500, 100, 100, 50, 50, 0, 0, 0, 0, 0, 0, False, 0, 0, 0, 0, 0, False, 0, 0, 0, 0, 0, 0, 0]
        super().__init__("RTanjiro", skill, stat_list)


                
if __name__ == "__main__":
    
    player = Character("Tanjiro Kamado")

    choice = int(input("Choose a skill (0: DragonSunHaloHeadDance, 1: FlashCut): "))
    selected_skill = player.skill[choice]

    selected_skill.status_use(player, None)