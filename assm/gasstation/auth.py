import DB_module
import module
import setting
import getpass

def sign_up():
    nickname = input('아이디를 입력하세요: ')
    password = getpass.getpass('비밀번호 입력하세요: ')

    if setting.players.find_one({
        'nickname' : nickname 
    }):
        print('이미 존재하는 아이디 입니다.')
    else:
        setting.players.insert_one({
            'nickname' : nickname,
            'password' :  password, 
            'custom' : [],
            'cleared' : [],
            'live_status' : {
                "left_life" : 0, "current_used" : [], "current_word" : 'None', "playing" : False
            },
            'ai_list' : [],
            'bought_dlc' : [],
            'coin' : 0
        })
        print('정상적으로 계정이 생성되었습니다.')
        module.enter()

def sign_in():
    nickname = input('닉네임을 입력하세요: ')
    password = getpass.getpass('비밀번호를 입력하세요: ')

    if setting.players.find_one({
        "nickname" : nickname,
        "password" : password
    }):
        return nickname
    else:
        return False