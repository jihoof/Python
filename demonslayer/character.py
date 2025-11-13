import os
import sys
import skill_blood_demon_art
import skill_breath
import passive
import skill_normal
import skill_ultimate
import color

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

import module

def show_info(grade, level, rank, awake, max_health, martial_arts_level, breath, 
              start_stamina, max_stamina, ultimate_meter, 
              skill1, skill2, skill3, ultimate, passives):
    
    print(f"{color.Color.BRIGHT_CYAN}{'-'*40}{color.Color.RESET}")
    print(f"{color.Color.YELLOW}등급{color.Color.RESET}: {color.Color.GREEN}{grade}{color.Color.RESET} | {color.Color.MAGENTA}Rank{color.Color.RESET}: {color.Color.CYAN}{rank}{color.Color.RESET}")
    print(f"{color.Color.YELLOW}Level{color.Color.RESET}: {level} (Awake {awake})")
    print(f"{color.Color.RED}체력{color.Color.RESET}: {max_health:.1f}")
    print(f"{color.Color.BLUE}체술{color.Color.RESET}: {martial_arts_level:.1f}")
    print(f"{color.Color.CYAN}호흡{color.Color.RESET}: {breath:.1f}")
    print(f"{color.Color.WHITE}스태미너{color.Color.RESET}: {start_stamina}/{max_stamina}")
    print(f"{color.Color.MAGENTA}궁극기 게이지{color.Color.RESET}: {ultimate_meter}")
    print()
    
    print(f"{color.Color.GREEN}스킬 1{color.Color.RESET}: {getattr(skill1, 'name', skill1)}")
    print(f"{color.Color.GREEN}스킬 2{color.Color.RESET}: {getattr(skill2, 'name', skill2)}")
    print(f"{color.Color.GREEN}스킬 3{color.Color.RESET}: {getattr(skill3, 'name', skill3)}")
    print(f"{color.Color.RED}궁극기{color.Color.RESET}: {getattr(ultimate, 'name', ultimate)}")

    # 패시브 출력
    passive_names = [getattr(p, 'name', getattr(p, '__class__', type('')).__name__) for p in (passives or [])]
    print(f"{color.Color.BRIGHT_YELLOW}패시브{color.Color.RESET}: {color.Color.BRIGHT_WHITE}{', '.join(passive_names)}{color.Color.RESET}")

    print(f"{color.Color.BRIGHT_CYAN}{'-'*40}{color.Color.RESET}")

#속성 

# 등급별 데이터
grade_data = {
    "없음": {"level": 100, "stat_bonus": 0, "rank": 0},
    "갑": {"level": 110, "stat_bonus": 100, "rank": 1},
    "을": {"level": 120, "stat_bonus": 100, "rank": 2},
    "병": {"level": 130, "stat_bonus": 150, "rank": 3},
    "정": {"level": 140, "stat_bonus": 150, "rank": 4},
    "무": {"level": 150, "stat_bonus": 200, "rank": 5},
    "기": {"level": 160, "stat_bonus": 200, "rank": 6},
    "경": {"level": 170, "stat_bonus": 250, "rank": 7},
    "신": {"level": 180, "stat_bonus": 250, "rank": 8},
    "임": {"level": 190, "stat_bonus": 300, "rank": 9},
    "계": {"level": 200, "stat_bonus": 400, "rank": 10},
    "주": {"level": 210, "stat_bonus": 1000, "rank": 11}
}


# 누적 스탯 보너스 계산
def get_total_stat_bonus(rank):
    total = 0
    for data in grade_data.values():
        if data["rank"] <= rank:
            total += data["stat_bonus"]
    return total

########## 차라리 부모 클래스 character 두고 2단 상속을 할까? 완료

class Character():
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level,
                 stat_per_level_health, stat_per_level_attack):
        self.level = level
        self.max_level = 100 # grade 따라서로 바꿔야됨
        self.grade = grade
        self.awake = awake
        self.base_breath = base_breath
        self.base_blood_demon_art_level = base_blood_demon_art_level
        self.stat_per_level_health = stat_per_level_health
        self.stat_per_level_attack = stat_per_level_attack

        grade_info = grade_data.get(self.grade, grade_data["없음"])
        self.rank = grade_info["rank"]
        self.stat_bonus = get_total_stat_bonus(self.rank)

        self.max_health = (base_health + (self.stat_per_level_health * self.level) + self.stat_bonus) * (1 + (self.awake / 10))
        self.martial_arts_level = (base_martial_arts_level + (self.stat_per_level_attack * self.level) + self.stat_bonus) * (1 + (self.awake / 10))

        if base_breath > 0:
            self.breath = (base_breath + (stat_per_level_attack * self.level) + self.stat_bonus) * (1 + (self.awake / 10))
        else:
            self.breath = 0

        if self.base_blood_demon_art_level > 0:
            self.blood_demon_art_level = (self.base_blood_demon_art_level + (stat_per_level_attack * self.level) + self.stat_bonus) * (1 + (self.awake / 10))
        else:
            self.blood_demon_art_level = 0

        if self.awake == 5:
            self.start_stamina = 30
            self.max_stamina = 110
            self.ultimate_meter = ultimate_meter - 100
        else:
            self.start_stamina = 20
            self.max_stamina = 100
            self.ultimate_meter = ultimate_meter

    def show_info_breath(self):
        print(f"{color.Color.BRIGHT_CYAN}{'-'*40}{color.Color.RESET}")
        print(f"{color.Color.YELLOW}등급{color.Color.RESET}: {color.Color.GREEN}{self.grade}{color.Color.RESET} | {color.Color.MAGENTA}Rank{color.Color.RESET}: {color.Color.CYAN}{self.rank}{color.Color.RESET}")
        print(f"{color.Color.YELLOW}Level{color.Color.RESET}: {self.level} (Awake {self.awake})")
        print(f"{color.Color.RED}체력{color.Color.RESET}: {self.max_health:.1f}")
        print(f"{color.Color.BLUE}체술{color.Color.RESET}: {self.martial_arts_level:.1f}")
        print(f"{color.Color.CYAN}호흡{color.Color.RESET}: {self.breath:.1f}")
        print(f"{color.Color.WHITE}스태미너{color.Color.RESET}: {self.start_stamina}/{self.max_stamina}")
        print(f"{color.Color.MAGENTA}궁극기 게이지{color.Color.RESET}: {self.ultimate_meter}")
        print()
        
        print(f"{color.Color.GREEN}스킬 1{color.Color.RESET}: {getattr(self.skill1, 'name', self.skill1)}")
        print(f"{color.Color.GREEN}스킬 2{color.Color.RESET}: {getattr(self.skill2, 'name', self.skill2)}")
        print(f"{color.Color.GREEN}스킬 3{color.Color.RESET}: {getattr(self.skill3, 'name', self.skill3)}")
        print(f"{color.Color.RED}궁극기{color.Color.RESET}: {getattr(self.ultimate, 'name', self.ultimate)}")

        # 패시브 출력
        passive_names = [getattr(p, 'name', getattr(p, '__class__', type('')).__name__) for p in (self.passives or [])]
        print(f"{color.Color.BRIGHT_YELLOW}패시브{color.Color.RESET}: {color.Color.BRIGHT_WHITE}{', '.join(passive_names)}{color.Color.RESET}")

        print(f"{color.Color.BRIGHT_CYAN}{'-'*40}{color.Color.RESET}")       

    def show_info_demon(self):
        print(f"{color.Color.BRIGHT_CYAN}{'-'*40}{color.Color.RESET}")
        print(f"{color.Color.YELLOW}등급{color.Color.RESET}: {color.Color.GREEN}{self.grade}{color.Color.RESET} | {color.Color.MAGENTA}Rank{color.Color.RESET}: {color.Color.CYAN}{self.rank}{color.Color.RESET}")
        print(f"{color.Color.YELLOW}Level{color.Color.RESET}: {self.level} (Awake {self.awake})")
        print(f"{color.Color.RED}체력{color.Color.RESET}: {self.max_health:.1f}")
        print(f"{color.Color.BLUE}체술{color.Color.RESET}: {self.martial_arts_level:.1f}")
        print(f"{color.Color.CYAN}혈귀술{color.Color.RESET}: {self.blood_demon_art_level:.1f}")
        print(f"{color.Color.WHITE}스태미너{color.Color.RESET}: {self.start_stamina}/{self.max_stamina}")
        print(f"{color.Color.MAGENTA}궁극기 게이지{color.Color.RESET}: {self.ultimate_meter}")
        print()
        
        print(f"{color.Color.GREEN}스킬 1{color.Color.RESET}: {getattr(self.skill1, 'name', self.skill1)}")
        print(f"{color.Color.GREEN}스킬 2{color.Color.RESET}: {getattr(self.skill2, 'name', self.skill2)}")
        print(f"{color.Color.GREEN}스킬 3{color.Color.RESET}: {getattr(self.skill3, 'name', self.skill3)}")
        print(f"{color.Color.RED}궁극기{color.Color.RESET}: {getattr(self.ultimate, 'name', self.ultimate)}")

        # 패시브 출력
        passive_names = [getattr(p, 'name', getattr(p, '__class__', type('')).__name__) for p in (self.passives or [])]
        print(f"{color.Color.BRIGHT_YELLOW}패시브{color.Color.RESET}: {color.Color.BRIGHT_WHITE}{', '.join(passive_names)}{color.Color.RESET}")

        print(f"{color.Color.BRIGHT_CYAN}{'-'*40}{color.Color.RESET}")


class R:
    # 부모 클래스
   class R(Character):
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        
        super().__init__(
            level=level,
            grade=grade,
            awake=awake,
            ultimate_meter=ultimate_meter,
            base_breath=base_breath,
            base_health=base_health,
            base_martial_arts_level=base_martial_arts_level,
            base_blood_demon_art_level=base_blood_demon_art_level,
            stat_per_level_health=10,
            stat_per_level_attack=2
        )

class SR(Character):
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        
        # Character __init__ 호출, 레벨별 스탯 증가량 10, 2로 설정
        super().__init__(
            level=level,
            grade=grade,
            awake=awake,
            ultimate_meter=ultimate_meter,
            base_breath=base_breath,
            base_health=base_health,
            base_martial_arts_level=base_martial_arts_level,
            base_blood_demon_art_level=base_blood_demon_art_level,
            stat_per_level_health=80,
            stat_per_level_attack=3
        )


class SSR(Character):
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        
        # Character __init__ 호출, 레벨별 스탯 증가량 10, 2로 설정
        super().__init__(
            level=level,
            grade=grade,
            awake=awake,
            ultimate_meter=ultimate_meter,
            base_breath=base_breath,
            base_health=base_health,
            base_martial_arts_level=base_martial_arts_level,
            base_blood_demon_art_level=base_blood_demon_art_level,
            stat_per_level_health=100,
            stat_per_level_attack=15
        )

class UR(Character):
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        
        # Character __init__ 호출, 레벨별 스탯 증가량 10, 2로 설정
        super().__init__(
            level=level,
            grade=grade,
            awake=awake,
            ultimate_meter=ultimate_meter,
            base_breath=base_breath,
            base_health=base_health,
            base_martial_arts_level=base_martial_arts_level,
            base_blood_demon_art_level=base_blood_demon_art_level,
            stat_per_level_health=150,
            stat_per_level_attack=45
        )

class LR(Character):
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        
        # Character __init__ 호출, 레벨별 스탯 증가량 10, 2로 설정
        super().__init__(
            level=level,
            grade=grade,
            awake=awake,
            ultimate_meter=ultimate_meter,
            base_breath=base_breath,
            base_health=base_health,
            base_martial_arts_level=base_martial_arts_level,
            base_blood_demon_art_level=base_blood_demon_art_level,
            stat_per_level_health=250,
            stat_per_level_attack=70
        )

class EX(Character):
    def __init__(self, level, grade, awake, ultimate_meter,
                 base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        
        # Character __init__ 호출, 레벨별 스탯 증가량 10, 2로 설정
        super().__init__(
            level=level,
            grade=grade,
            awake=awake,
            ultimate_meter=ultimate_meter,
            base_breath=base_breath,
            base_health=base_health,
            base_martial_arts_level=base_martial_arts_level,
            base_blood_demon_art_level=base_blood_demon_art_level,
            stat_per_level_health=500,
            stat_per_level_attack=250
        )

#실험용 첫 캐릭
class WhatIsSoFunTysikuniYourich(EX):
    def __init__(self, level, grade, awake, ultimate_meter, base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level):
        super().__init__(level, grade, awake, ultimate_meter, base_breath, base_health, base_martial_arts_level, base_blood_demon_art_level)
        self.skill1 = skill_normal.FlashCut()
        self.skill2 = skill_breath.PhantomSunCrimson()
        self.skill3 = skill_breath.DragonSunHaloHeadDance()#분노 상태로 1,2,3스킬 다변형
        self.ultimate = ""
        self.passives = [passive.ThePerfectSun(), passive.ThePersonWho(), passive.DemonSlayerMarkV(), passive.TransparantWorldVI(), passive.RedSowrdVI()]

#테스트
if __name__ == "__main__":

    character1 = WhatIsSoFunTysikuniYourich(

        level = 210,
        grade='주',
        awake=5,
        ultimate_meter=2500,
        base_breath=14329,
        base_health=32938,
        base_martial_arts_level=12429,
        base_blood_demon_art_level=0
    )

    

    character1.show_info_breath()
    print()




