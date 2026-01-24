import random
import time
import setting

while True:
    change_time = random.randint(2000000, 3000000)
    setting.price.update_one({
        'cnt': {"$exists": True}
   }, {
       '$set': {
           'cnt': {
                'gasoline': random.randint(90000000, 200000000),
                'diesel': random.randint(90000000, 200000000),
           },
           'price': {
                'gasoline': random.uniform(0.5, 2.5),
                'diesel': random.uniform(0.35, 2.25),
                'electric': random.uniform(0.15, 1.5)
            }
        }
   })
    time.sleep(change_time)

