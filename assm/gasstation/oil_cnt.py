import random
import time
import setting

while True:
    change_time = random.randint(2000000, 3000000)
    setting.price.update_one({
        'cnt': {"$exists": True}
   }, {
       '$set': {
           'gasoline': random.randint(90000000, 200000000),
           'diesel': random.randint(90000000, 200000000),
        }
   })
    time.sleep(change_time)

