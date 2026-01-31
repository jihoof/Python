import time
from db import price

while True:
    change_time = 3600
    price.update_one({
        'product': {'$exists': True}, 
    })
    time.sleep(change_time)