import assm.gasstation.libs.module as module
import assm.gasstation.config as config
from assm.gasstation.db import players
import getpass
import hashlib
import os

def sign_up():
    while True:
        nickname = input('플레이어 아이디를 입력하세요(변경 불가): ')
        if players.find_one({'id' : nickname }):
            print('이미 존재하는 아이디 입니다.')
            continue
        
        password = getpass.getpass('비밀번호 입력하세요: ')
        re_password = getpass.getpass('비밀번호를 다시 입력하세요: ')

        if password != re_password:
            print("재입력한 비밀번호가 올바르지 않습니다")
            continue
            
        break
    
    salt = os.urandom(16)
    encrypted_password = hash_password(password, salt)

    players.insert_one({
        'id' : nickname,
        'password' :  encrypted_password, 
        'salt': salt,
        'items': [],
        'bought_upgrades': [],
        'money': 100,
        'diesel': 0,
        'gasoline': 0,
        'cars': [],
        'auction_house_membership_level': 5,
        'day': 0,
        'rate': 0,
        'handled_customers': 0,
        'multiplier': 1.0
    })
    print('정상적으로 계정이 생성되었습니다.')
    module.enter()

def sign_in():
    while True:
        nickname = input('플레이어 id를 입력하세요: ')
        password = getpass.getpass('비밀번호를 입력하세요: ')

        info = players.find_one({"id" : nickname})
        if not info:
            print("유저가 존재하지 않습니다")
            break
            
        salt = info['salt']
        encrypted_password = hash_password(password, salt)
        
        if info['password'] != encrypted_password:
            print("비밀번호가 올바르지 않습니다")
            continue
        
        print("로그인 되었습니다")
        return info, True
    
def hash_password(password, salt):
    return hashlib.sha256(salt + password.encode()).hexdigest()

