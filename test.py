class Posmon:
    def __init__(self, life):
        self.life = life

posmon_list = [Posmon(0), Posmon(100), Posmon(0), Posmon(50), Posmon(1)]

life_str = ''.join(["X" if posmon.life <= 0 else "0" for posmon in posmon_list]) # list comprehension

life_str = "" # for loop
for posmon in posmon_list:
    if posmon.life >= 0:
        life_str += "0"
    else:
        life_str += "X"

class Normie:
    def __init__(self, life):
        self.life = life
        self.type = "Normie"

class Rocky:
    def __init__(self, life):
        self.life = life
        self.type = "Rocky"

class Phoenix:
    def __init__(self, life):
        self.life = life
        self.type = "Phoenix"

player_list = []

for i in range(3):
    print("0. Normie")
    print("1. Rocky")
    print("2. Phoenix")

    name_type = ["Normie", "Rocky", "Phoenix"]
    while True:
        num = int(input("번호 선택: "))

        # 이미 선택한 포스몬일 때
        if name_type[num] in [posmon.type for posmon in player_list]:
            print("이미 선택하셨습니다. 다시하세요")
            continue
        else:
            if num == 0:
                player_list.append(Normie(100))
            elif num == 1:
                player_list.append(Rocky(100))
            elif num == 2:
                player_list.append(Phoenix(100))
            break

print(f"뽑은 포스몬 목록: {" ".join([posmon.type for posmon in player_list])}")
