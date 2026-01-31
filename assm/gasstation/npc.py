import random
import llm
import repo.jihoo.assm.gasstation.config as config
import uuid
import repo.jihoo.assm.gasstation.libs.module as module

class Npc:
    def __init__(self):
        if config.npc.count_documents({}) < 0:
            data = self.add_npc()
        else:
            if module.chance(60):
                data = self.add_npc()
            else:
                data = random.choice(list(config.npc.find()))
        
        self.id           = data['id']
        self.name         = data['name']
        self.talk_history = data['talk_history']
        self.likeablity   = data['likeability']
        self.visit_cnt    = data['visit_cnt']
        
    def add_npc(self):
        data = {
            'id' : str(uuid.uuid4()),
            'name' : str(llm.llm_answer('npc에게 사용될 수있는 랜덤한 이름을 만들어줘. 이름만 답해.')),
            'talk_history' : [],
            'likeability' : 0, #ai한테 대화 바탕 호감도 측정
            'visit_cnt' : 0
        }
        config.npc.insert_one(data)
        return data
    
    def update_npc(self):
        data = {
            'id': self.id,
            'name': self.name,
            'talk_history': self.talk_history,
            'likeability': self.likeablity,
            'visit_cnt': self.visit_cnt
        }
        config.npc.update_one({
            'id': self.id
        }, {
            '$set': data
        })

    def chatbot(self):
        print("챗봇 시작")
        
        while True:
            query = str(self.talk_history) + input("입력: ")
            answer = llm.llm_answer(query)
            
            history = {
                'query': query,
                'answer': answer
            }
            self.talk_history.append(history)
            self.update_npc()


test = Npc()
test.chatbot()