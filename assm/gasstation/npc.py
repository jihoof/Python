import random
import math
import llm
import setting
import uuid
import module

class Npc:
    def __init__(self):
        if setting.npc.count_documents() < 0:
            self.add_npc()
        else:
            make_new = module.chance(70)
            if make_new:
                self.add_npc()
            else:
                selected_npc = random.choice(list(setting.npc.find()))
                

    def add_npc():
        setting.npc.insert_one({
            'id' : str(uuid.uuid4()),
            'name' : str(llm.answer('npc에게 사용될 수있는 랜덤한 이름을 만들어줘. 이름만 답해.')),
            'talk_history' : [],
            'likeability' : 0, #ai한테 대화 바탕 호감도 측정
            'visit_cnt' : 0
        })


    def normal_response_before_refill(self):
        pass

    def normal_response_after_refill(self, reply):
        pass
    
    def abnormal_response_before_refill(self, reply):
        pass

    def abnormal_response_after_refill(self, reply):
        pass


