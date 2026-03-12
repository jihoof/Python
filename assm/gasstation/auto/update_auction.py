import time
from assm.gasstation.db import auction, players, transaction

def auction_server():
    while True:
        time.sleep(2)
        auction.update_many({},{'$inc': {'time_left': -2}})
        auction_ = list(auction.find())
        for product in auction_:
            if product['time_left'] <= 0:
                max_price = 0
                target_user = None
                for user in product['proposal']:
                    if user['price'] > max_price:
                        target_user = user['buyer']
                        max_price = user['price']
                players.update_one({'id': product['saler']}, {'$inc': {'money': max_price}})
                players.update_one({'id': str(target_user)}, {'$inc': {'money': -max_price}})
                transaction.add_items(str(target_user), 1, product['name'], product['product_introduce'], product['lowest_price'])
                transaction.decrease_items(product['saler'], 1, product['name'] )
                auction.delete_one({'name': product['name']})
                print(f'정상적으로 업데이트 됨! 물건 이름: {product['name']} {product['saler']} -> {target_user}')



