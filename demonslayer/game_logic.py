def next_turn(self):
    print("턴이 지났습니다")
    for passive in self.passive_list:
        passive[1] -= 1
    
    for passive in self.passive_list:
        if passive[1] == 0:
            self.stat[passive[0]] = original_stat(self.stat[passive[0]], passive[2])
            self.passive_list.remove(passive)