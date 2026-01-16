import random
import time
import setting

while True:
    change_time = random.randint(2000, 4000)
    setting.price.update_one({
        'price': {"$exists": True}
   }, {
       '$set': {
           'gasoline': random.uniform(0.5, 2.5),
           'diesel': random.uniform(0.35, 2.25),
           'electric': random.uniform(0.15, 1.5)
        }
   })
    time.sleep(change_time)

