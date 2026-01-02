import setting
import random 
import module
import getpass
import llm

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
                'live_status' : {
                    "left_life" : 0, "current_used" : [], "current_word" : 'None', "playing" : False
                },
                'ai_list' : [],
                'bought_dlc' : [],
                'coin' : 0
            })
            print('정상적으로 계정이 생성되었습니다.')
            module.enter()

    def give_coin(self, difficulty):
        if difficulty == 'very easy':
            giving_coin = 1
        elif difficulty == 'easy':
            giving_coin = 5
        elif difficulty == 'medium':
            giving_coin = 10
        elif difficulty == 'hard':
            giving_coin = 20
        elif difficulty == 'very hard':
            giving_coin = 50
        elif difficulty == 'hell':
            giving_coin = 100
    
    def load_coin(self):
        coin = setting.players.find_one({
            "nickname" : self.nickname
        },{
            "_id":0,"coin":1
        })
        return coin
    
    def update_coin(self, amount):
        setting.players.update_one({
            'nickname' : self.nickname
        }, {
            '$inc' : {
                "coin" : amount
            }                
        })

    def ai_word_list(self):
        answer = llm.llm_answer("Make a 5 word list that could be used in hangman game. The diffculty must be very hard. Only english word, but it does not to be on every dictionary Give your answer in 'word1 word2 word3 ...' form'")
        return answer.split()

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
        for i in comp_word:
            if i in used:
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
        },{
            "_id":0,"custom":1
        })
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

    def update_status(self, life, used_word):
        setting.players.update_one({
            "nickname" : self.nickname
        }, {
            "$set" : {
                "live_status.left_life" : life,
                "live_status.current_used" : used_word
            }
        })
        
    def reset_status(self):
        setting.players.update_one({
            "nickname" : self.nickname
        }, {
            "$set" : {
                "live_status.left_life" : 0,
                "live_status.current_used" : [],
                "live_status.current_word" : "None",
                "live_status.playing" : False
            }
        })      

    def dlc(self):
        #TODO 현재 보유 코인 출력
        while True:
            print('Dlc 상점에 오신걸 환영합니다.')
            # custom 유저 한테 업로드 
            # 가격 유저 업로드 가격 비례 코인 지불 가격 2배
            # 다른 구매하면 자기한테 알림오고 수수료 50% 코인(like 대한민국 세금) 지급
            select = module.input_int(1, 2, 'Dlc 상점에 업로드 현재 커스텀 리스트를 업로드하려면 1을 Dlc 상점을 구경하려면 2를 입력해주세요: ', '잘못된 입력입니다.')
            if select == 1:
                custom_list = self.custom_load()
                if len(custom_list) == 0:
                    print('커스텀 리스트에 아무 단어도 존재하지 않습니다.')
                    print('전 화면으로 되돌하갑니다. ')
                    continue
                else:
                    upload_status = self.upload_custom(custom_list)
                    if not upload_status:
                        print('Unexpected critical error occured. Error code: -1336')
                        print('도움을 위해선 고객센터에 연락해주시기 바랍니다. 전화번호: 1336')
            else:
                print('현재 구입가능한 Dlc 상점의 상품들을 보여드리겠습니다. ')
                print('정보 로딩중...')
                product_list = list(setting.dlc.find({},{'id_':0}))
                print('로딩 완료!')
                module.beautiful_table(product_list, title = '상품 정보', show_index = True)
                select = input('구매할 상품의 이름을 입력해주세요.')
                
    def buy_dlc(self, price):
        pass

    def upload_custom(self, custom_list):
        name = input('Dlc에 업로드할 단어리스트의 이름을 입력해주세여: ')
        price = module.input_int(0, 99999, 'Dlc에 업로드할 단어리스트의 가격을 설정해주세요(0 ~ 99,999): ', '잘못된 입력입니다.')
        print('가격이 상정되었습니다. 가격 비례 수수료와 업로드 가격을 자동 측정합니다.')
        charge = 30
        print('가격 책정중...')
        upload_fee = llm.llm_answer(f"""
        You are evaluating a product listed in a DLC shop for a game.
        The product’s listed price is {price}.

        The platform takes a fixed 30% commission fee from all sales. This commission must be fully considered.

        Determine a reasonable **initial registration cost** to list this product. Your calculation must:
        1. Consider net revenue after the 30% commission.
        2. Never return the original price or a value equal to the listed price.
        3. Factor in expected sales, market fairness, and reasonable profit margins.
        4. Reflect risk mitigation for unsold products (i.e., the registration cost should not be higher than likely net revenue per sale).

        Return only a single integer value representing the final registration cost.
        Do **not** include explanations, text, symbols, or formatting — numbers only (int).
        """)
        upload_fee = int(upload_fee)
        print('책정 완료!')
        select = module.input_int(f'책정 결과, 업로드 비용은 {upload_fee}이고 수수료는 30%입니다. 상품은 dlc상점에 등록하겠습니까? 등록하려면 1을 취소하려면 2를 입력하세요: ')
        if select == 1:
            if not setting.dlc.find_one({
                'name' : name
            }):  
                print('등록비를 약탈합니다.')
                coin = self.load_coin()
                if coin > upload_fee:
                    setting.dlc.insert_one({
                        'name' : name,
                        'price' : price,
                        'word_list' : custom_list,
                        'charge' : charge
                    })
                    print('상품이 정상적으로 등록되었습니다.')
                    return True
                else:
                    print('이미 존재하는 상품 이름입니다.')
                    module.enter()
                    return False
            else:
                print('코인 부족하여 등록에 실패했습니다.')
                print('메인화면으로 되돌아갑니다.')
                module.enter()
                return False
                
        else:
            print('원래 화면으로 되돌아갑니다.')
            module.enter()
            return False



    def main(self):
        play_again = None 
        run = True

        while run:
            select = module.input_int(1,2,'게임을 플레이하려면 1을 Dlc 상점을 오픈하려면 2을 입력해주세요: ', '잘못된 입력입니다.')
            if select == 1:
                live_status = setting.players.find_one({
                    'nickname' : self.nickname
                })["live_status"]
                print('환영합니다.')
                
                history = False
                if live_status["playing"]:
                    select = module.input_int(
                        0, 1, 
                        '진행하던 게임이 존재합니다. 이어 플레이하시겠습니다까? (이어하려면 0을 새로 시작하려면 1을 입력하세요.) ', 
                        '잘못된 입력입니다.'
                    )
                    if select == 0:
                        history = True
                        comp_word = live_status["current_word"]
                        USED = live_status["current_used"]
                        LIFE = live_status["left_life"]
                        
                if history == False:
                    select = module.input_str(
                        '플레이하고 싶은 레벨을 선택해주세요(very easy, easy, medium, hard, very hard, hell, custom): ', 
                        '잘못된 입력입니다.', 
                        ['very easy', 'easy', 'medium', 'hard', 'very hard', 'hell', 'custom']
                    )
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
                        }, {
                            "_id":0, "word_list":1
                        })
                        self.word_list = difficulty["word_list"]
                        giving_coin = self.give_coin(select)
                        module.enter()

                    comp_word = random.choice(self.word_list)
                    USED = []
                    LIFE = 10
                
                while True:
                    print("Hangman game starts!")
                    setting.players.update_one({
                        "nickname" : self.nickname
                    }, {
                        "$set" : {
                            "live_status.current_word" : comp_word,
                            "live_status.playing" : True
                        }
                    })

                    module.clear()
                    self.print_status(comp_word, USED, LIFE)
                    word_guessed = self.is_word_guessed(comp_word, USED)
                    self.update_status(LIFE, USED)
                    play_again = 'none'

                    if LIFE == 0:
                        print(f"The answer was {comp_word}. ")
                        self.reset_status()
                        play_again = module.input_str("Do you want to play another game(Y/n): ", '잘못된 입력입니다.', ['Y', 'y', 'N', 'n'])
                    elif word_guessed == True:
                        print("Hangman Survived!")
                        self.reset_status()
                        self.update_coin(giving_coin)
                        print(f'게임을 클리어하여, 난이도에 따라 코인 {giving_coin}개가 지급되었습니다.')
                        play_again = module.input_str("Do you want to play another game(Y/n): ", '잘못된 입력입니다.', ['Y', 'y', 'N', 'n'])

                    if play_again.lower() == "y":
                        self.reset_status() 
                        break
                    elif play_again.lower() == "n":
                        self.reset_status()
                        module.shut_down()
                        
                    while True:
                        player_word = input("Choose a character: ")
                        if len(player_word) == 1:
                            break
                        print("한 글자만 입력해주세요.")
                        
                    if player_word in USED:
                        print("You have already checked this character. Try another one.")
                        module.enter()
                        continue
                    else:
                        if player_word not in comp_word:
                            LIFE -= 1
                        USED.append(player_word)
            
            else:
                self.dlc()

game = Hackman()    
game.main()



