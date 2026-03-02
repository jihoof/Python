import time
from db import auction, players

def auction_server():
    while True:
        time.sleep(60)
        auction.update_many({},{'$inc': {'time_left': -60}})
        auction_ = list(auction.find())
        for i in auction_:
            if i['time_left'] <= 0:
                for j in i['proposal']:
                    tmp = j
                    if j > tmp:
                        max_ = j
                players.update_one({'id': i['saler']}, {'$inc': {'money': max_}})
                players.update_one    
                auction.delete_one({'name': i['name']})


id : 10