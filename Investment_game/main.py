from setting import *
import math
import numpy
import numba 
import random
import copy
import json

path_morning = 'Python/Investment_game/news/morning_news.json'
path_evening = 'Python/Investment_game/news/evening_news.json'

with open(path_morning, 'r', encoding='utf-8') as file:
    morning_data = json.load(file)
with open(path_evening, 'r', encoding='utf-8') as file:
    evening_data = json.load(file)

playermoney = 100_000

def PlayerMoney(playermoney, percentage):
    playermoney += playermoney * percentage

def morning_news_print():
    num = random.randint(0, 4)
    print(morning_data['K-전자']['morning_news'][num]['news']) #뉴스는 5개 
    print(morning_data['금']['morning_news'][num]['news'])
    print(morning_data['비트코인']['morning_news'][num]['news'])
    print(morning_data['애플']['morning_news'][num]['news'])
    print(morning_data['에너지']['morning_news'][num]['news'])
    print(morning_data['건설']['morning_news'][num]['news'])

morning_news_print()