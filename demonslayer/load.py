import os, json
with open(os.path.join(os.path.dirname(__file__), 'dictionary.json'), 'r', encoding='utf-8') as f:
    game_dict = json.load(f)
