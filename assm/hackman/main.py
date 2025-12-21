import setting
import random 
import module
import os
import sys
import getpass
import time
import rich

class Hackman:
    def __init__(self):
        
    def sign_up(self):

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
                'custom' : []

            })

    def admin_login():

        password = getpass.getpass('관리자 비밀번호 입력하세요: ')

        admin = setting.players.find_one({

            'nickname' : 'admin'

        })

        admin_password = admin['password']

        if password == admin_password:
            print('성공적으로 로그인 되었습니다.')
            print('환영합니다, 관리자님.')
            return True
        else:
            print('비밀번호가 잘못되었습니다.')
            return False
            
            

    def reveal_word(comp_word, used):
        for i in comp_word:
            if i not in used:
                print("_", end = " ")
            else:
                print(i, end = " ")
        return ""

    def print_status(comp_word, used, life):
        print("---------------------------------------------")
        print(f"Word: ", end = ' ')
        reveal_word(comp_word, used)
        print()
        print(f"Used: {' '.join(used)}")
        print(f"Life: {life}")
        print("---------------------------------------------")

    def is_word_guessed(comp_word, used):
        tmp = list(comp_word)
        tmp2 = len(tmp)
        tmp3 = 0
        for i in used:
            if i in comp_word:
                tmp3 += 1
        if tmp3 == tmp2:
            return True
        else:
            return False
        
    def print_user_list():
        user_list = list(setting.players.find({},{'_id' : 0, 'password' : 0}))
        module.beautiful_table(user_list, title = 'User List', show_index = True)

    def login():
        pass

    def main():
        play_again = "none"

        intel_setup = True
        run = True

        while run:
            if intel_setup == True:
                comp_word = random.choice(setting.WORD_LIST)
                print("Hangman game starts!")
                USED = []
                LIFE = 10
                intel_setup = False
            else:
                pass
            
            while True:
                module.clear()
                print('Hang Man game.inc')
                print("관리자 로그인을 하시려면 '1'을, 로그인 하시려면 '2'를, 계정을 생성하려면 '3'을 입력해주세요.")
                select = module.input_int(1,3,'입력: ','잘못된 입력입니다.')

                if select == 1:
                    admin = admin_login()
                    if admin == True:
                        module.clear()
                    
                        while True:
                            select = module.input_int(1,2,'관리자 메뉴를 열람할려면 1번, 로그아웃하기 위해선 2번을 입력해주새요: ', '비밀번호가 일치하지 않습니다.')
                            if select == 1:
                                print_user_list()
                                while True:
                                    select = module.input_int(1,2,'유저를 삭제하시려면 1번, 종료하려면 2번을 입력해주세요: ', '잘못된 입력입니다.')
                                    if select == 1:
                                        print()
                                        selected_user = input('삭제할 유저의 닉네임을 입력해주세요: ')
                                        if setting.players.find_one({

                                            'nickname' : selected_user
                                        }):
                                            setting.players.delete_one({

                                                'nickname' : selected_user

                                                })
                                            print('유저가 정상적으로 삭제되었습니다.')
                                            module.enter()
                                            continue
                                        else:
                                            print('해당 유저가 존재하지 않습니다.')
                                            module.enter()
                                            continue 
                                    else:
                                    break
                            else:
                                print('로그아웃 합니다.')
                                break


                    else:
                        print('비밀번호가 일치하지 않습니다.')
                        print('시작화면으로 되돌아갑니다.')
                        continue

                elif select == 2:
                    logedin = login()
                    if logedin == True:
                        print('로그인 되셨습니다.')
                        module.enter()
                        break
                
                elif select == 3:
                    pass



            print_status(comp_word, USED, LIFE)
            word_guessed = is_word_guessed(comp_word, USED)

            if LIFE == 0:
                print(f"The answer was {comp_word}. ")
                play_again = input("Do you want to play another game? ")
            elif word_guessed == True:
                print("Hangman Survived!")
                play_again = input("Do you want to play another game? ")

            if play_again == "yes":
                intel_setup = True
                play_again = "none"
                continue
            elif play_again == "no":
                break


            player_word = input("Choose a character: ")
            if player_word in USED:
                print("You have already checked this character. Try another one.")
                continue
            else:
                if player_word not in comp_word:
                    LIFE -= 1
                USED.append(player_word)
            
            if play_again == "yes":
                intel_setup = True
                play_again = "none"
                continue
            elif play_again == "no":
                break

main()

