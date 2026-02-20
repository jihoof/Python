from assm.gasstation.db import players, price, blackmarket

# ------ Load ------
def load_money(id):
    return players.find_one({
        'id': id
    }, {'money': 1, '_id': 0})['money']

def load_diesel(id):
    return players.find_one({
            'id': id
    }, {'diesel': 1, '_id': 0})['diesel']
    
def load_gasoline(id):
    return players.find_one({
            'id': id
    }, {'gasoline': 1, '_id': 0})['gasoline']

def load_price():
    return price.find_one({
            'price': {'$exists': True}
    }, {'price':1, '_id': 0})

def load_items(id):
    return players.find_one({
        'id': id
    }, {'items': 1, '_id': 0})

def load_day(id):
    return players.find_one({
        'id': id
    }, {'day': 1, '_id': 0})['day']

def load_rating(id):
    return players.find_one({
        'id': id
    }, {'rate': 1, '_id': 0})['rate']

def load_handled_customers(id):
    return players.find_one({
        'id': id
    }, {'handled_customers': 1, '_id': 0})['handled_customers']

def load_blackmarket_product():
    return list(blackmarket.find({},{'_id': 0}))

# ------ Edit ------
def increase_money(id, amount):
    players.update_one({'id': id}, {"$inc": {'money': amount}})

def decrease_money(id, amount):
    players.update_one({'id': id}, {"$inc": {'money': -amount}})

def add_items(id, amount, name):
    if name in [item['name'] for item in players.find_one({"id": id}, {"_id": 0, "items": 1})["items"]]:
        players.update_one()