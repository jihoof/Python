# import
from DB_module import *
from rich.console import Console
from rich.table import Table

# settings
db = client["jihoo"]
players = db["hangman-players"]
console = Console()

def sign_up(nick_name, password):
    if players.find({

        'nickname' : nick_name 

    }):
        print('이미 존재함 ㅅㄱ')

    players.insert_one({

        'nickname' : nick_name,
        'password' :  password 

    })

# main

nickname = input()
password = input()

sign_up(nickname, password)
















