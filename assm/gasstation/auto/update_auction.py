import time
from db import auction, players

def auction_server():
    while True:
        time.sleep(60)
        auction.update_many({},{'$inc': {'time_left': -60}})
        auction_ = list(auction.find())
        for product in auction_:
            if product['time_left'] <= 0:
                max_price = 0
                target_user = None
                for user in product['proposal']:
                    if user['price'] > max_price:
                        target_user = user
                players.update_one({'id': product['saler']}, {'$inc': {'money': max_}})
                players.update_one    
                auction.delete_one({'name': product['name']})

