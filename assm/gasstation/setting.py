import DB_module

client = DB_module.client
db = client['jihoo']
players = db['gasstation-players']
npc = db['gasstation-npc']
price = db['gasstation-gas_price']
auction = db['gasstation-auction_house']