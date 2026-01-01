import DB_module

client = DB_module.client
db = client['jihoo']
players = db['hangman-players']
levels = db['hangman-levels']
dlc = db['hangman-dlc']

LIFE = 10
WORD_LIST = ['apple', 'april', 'banana', 'blue', 'coral', 'dictionary', 'flower', 'peach',
'strawberry', 'watermelon']
USED = []


