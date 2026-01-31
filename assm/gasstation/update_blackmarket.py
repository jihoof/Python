import random
import time
import setting

while True:
    change_time = 3600

    setting.price.update_one({
        'product': {'$exists': True}, 
    })
    time.sleep(change_time)