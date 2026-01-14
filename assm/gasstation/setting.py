import DB_module

client = DB_module.client
db = client['jihoo']
players = db['gasstation-players']
npc = db['gasstation-npc']