import setting
import random 
import module
import getpass
import time

class Hackman:
    def __init__(self):
        self.nickname = None
        
        while True:
            module.clear()
            print('Hang Man game.inc')
            print("관리자 로그인을 하시려면 '1'을, 로그인 하시려면 '2'를, 계정을 생성하려면 '3'을 입력해주세요.")
            select = module.input_int(1,3,'입력: ','잘못된 입력입니다.')

            if select == 1:
                admin = self.admin_login()
                if admin == True:
                    module.clear()
                
                    while True:
                        select = module.input_int(1,2,'관리자 메뉴를 열람할려면 1번, 로그아웃하기 위해선 2번을 입력해주새요: ', '비밀번호가 일치하지 않습니다.')
                        if select == 1:
                            self.print_user_list()
                            while True:
                                select = module.input_int(1,2,'유저를 삭제하시려면 1번, 종료하려면 2번을 입력해주세요: ', '잘못된 입력입니다.')
                                if select == 1:
                                    print()
                                    selected_user = input('삭제할 유저의 닉네임을 입력해주세요: ')
                                    if setting.players.find_one({'nickname' : selected_user}):
                                        setting.players.delete_one({'nickname' : selected_user})
                                        print('유저가 정상적으로 삭제되었습니다.')
                                        continue
                                    else:
                                        print('해당 유저가 존재하지 않습니다.')
                                        continue 
                                else:
                                    module.enter()
                                    break
                        else:
                            print('로그아웃 합니다.')
                            module.enter()
                            break


                else:
                    print('비밀번호가 일치하지 않습니다.')
                    print('시작화면으로 되돌아갑니다.')
                    continue

            elif select == 2:
                nickname = self.sign_in()
                if nickname:
                    print('로그인 되셨습니다.')
                    self.nickname = nickname
                    module.enter()
                    break
                else:
                    print('닉네임 또는 비밀번호 일치하지않습니다.')
                    module.enter()

            
            elif select == 3:
                self.sign_up()
                
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
                'custom' : [],
                'cleared' : [],
                'live_status' : {}

            })
            print('정상적으로 계정이 생성되었습니다.')
            module.enter()

    def sign_in(self):
        nickname = input('닉네임을 입력하세요: ')
        password = getpass.getpass('비밀번호를 입력하세요: ')

        if setting.players.find_one({

            "nickname" : nickname,
            "password" : password

        }):
            return nickname
        else:
            return False
        
    
    def admin_login(self):

        password = getpass.getpass('관리자 비밀번호 입력하세요: ')

        admin = setting.players.find_one({'nickname' : 'admin'})
        admin_password = admin['password']

        if password == admin_password:
            print('성공적으로 로그인 되었습니다.')
            print('환영합니다, 관리자님.')
            module.enter()
            return True
        else:
            print('비밀번호가 잘못되었습니다.')
            module.enter()
            return False
            
    def reveal_word(self, comp_word, used):
        for i in comp_word:
            if i not in used:
                print("_", end = " ")
            else:
                print(i, end = " ")
        return ""

    def print_status(self, comp_word, used, life):
        print("---------------------------------------------")
        print(f"Word: ", end = ' ')
        self.reveal_word(comp_word, used)
        print()
        print(f"Used: {' '.join(used)}")
        print(f"Life: {life}")
        print("---------------------------------------------")

    def is_word_guessed(self, comp_word, used):
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
        
    def print_user_list(self):
        user_list = list(setting.players.find({},{'_id' : 0, 'password' : 0}))
        module.beautiful_table(user_list, title = 'User List', show_index = True)
    
    def custom_edit(self):
        add_word = input('커스텀 단어 리스트의 추가할 단어들을 입력해주세요.(종료하려면 0을 입력): ')

        if add_word == '0':
            return False
        else:
            add_word = add_word.split()
            setting.players.update_one({
                "nickname" : self.nickname
            }, {
                "$addToSet" : {
                    "custom" : {
                        "$each" : add_word
                    },                    
                }
            })
            print('정상적으로 추가 되었습니다.')
            module.enter()
            return True

    
    def custom_load(self):
        custom = setting.players.find_one({

            "nickname" : self.nickname

        },{"_id":0,"custom":1})
        return custom["custom"]

    def custom_delete(self):
        self.custom_list = self.custom_load()
        module.beautiful_table(self.custom_list, title = 'Custom Word List', show_index = True)
        delete_words = input('커스텀 단어 리스트의 삭제할 단어들을 입력해주세요.(종료하려면 0을 입력): ')
        if delete_words == '0':
            return False
        else:
            delete_words = delete_words.split()
            for i in delete_words:
                if i not in self.custom_list:
                    print('Error index out of range. Error code: 374.')
                    print('도움을 원하시면 고객센터에 연락해주시기 바랍니다.')
                    return False
            setting.players.update_one({
                "nickname" : self.nickname
            },{
                "$pull" : {
                    "custom" : {
                        "$in" : delete_words
                    }
                }
            })
            print('정상적으로 삭제되었습니다.')
            module.enter()
            return True
        


    def custom_menu(self):
        print('커스텀 매뉴에 오신걸 환영합니다.')
        select = module.input_int(1,3,'커스텀 리스트를 수정하려면 1번, 되돌아가시려면 2번을, 플레이 하시려면 3번을 입력해주세요: ', '잘못된 입력입니다.')
        if select == 1:
            while True:
                select = module.input_int(1,3, '단어를 추가하려면 1을, 삭제하려면 2를, 되돌아가려면 3을 입력해주세요: ', '잘못된 입력입니다.')
                if select == 1:
                    if not self.custom_edit():
                        print('Unexpected error occured. Error code -1')
                        module.enter()
                        continue
                elif select == 2:
                    if not self.custom_delete():
                        module.enter()
                        continue
                else:
                    print('되돌아갑니다.')
                    module.enter()
                    break

                    
        elif select == 2:
            return False
        
        else:
            return self.custom_load()


    def main(self):

        play_again = None
        intel_setup = True
        run = True

        while run:
            
            print('환영합니다.')
            select = module.input_str('플레이하고 싶은 레벨을 선택해주세요(very easy, easy, medium, hard, very hard, hell, custom): ', '잘못된 입력입니다.', ['very easy', 'easy', 'medium', 'hard', 'very hard', 'hell', 'custom'])
            if select == 'custom':
                custom = self.custom_menu()
                if not custom:
                    print('커스텀 메뉴를 종료합니다.')
                    module.enter()
                    continue
                else:
                    self.word_list = custom

            else:
                difficulty = setting.levels.find_one({

                        "difficulty" : select

                    }, {"_id":0, "word_list":1})
                self.word_list = difficulty["word_list"]
                module.enter()
            
            while True:
                if intel_setup == True:
                    print("Hangman game starts!")
                    comp_word = random.choice(self.word_list)
                    USED = []
                    LIFE = 10
                    intel_setup = False
                else:
                    pass
                
                module.clear()
                self.print_status(comp_word, USED, LIFE)
                word_guessed = self.is_word_guessed(comp_word, USED)

                if LIFE == 0:
                    print(f"The answer was {comp_word}. ")
                    play_again = input("Do you want to play another game(yes/no): ")
                elif word_guessed == True:
                    print("Hangman Survived!")
                    play_again = input("Do you want to play another game(yes/no): ")

                if play_again == "yes":
                    intel_setup = True
                    play_again = "none"
                    break
                elif play_again == "no":
                    module.shut_down()
                    


                player_word = input("Choose a character: ")
                if player_word in USED:
                    print("You have already checked this character. Try another one.")
                    module.enter()
                    continue
                else:
                    if player_word not in comp_word:
                        LIFE -= 1
                    USED.append(player_word)
                
                if play_again == "yes":
                    intel_setup = True
                    play_again = "none"
                    break
                elif play_again == "no":
                    module.shut_down()

game = Hackman()
game.main()

