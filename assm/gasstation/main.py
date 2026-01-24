import DB_module
import module
import setting
import auth
from time import sleep

class GasStation:
    def __init__(self):
        pass

    def main(self):
        self.menu()
        while True:
            print('*'*5 + '뇌절 주유소' + '*'*5)
            print('0. Wait for a vehicle')
            print('1. Refill tanks')
            print('2. Show current status') # 현재 자산 등등 추가 표시
            print('3. Go to the next day') # 상점에서 침대를 구매해야 ㄱㄴ
            print('4. Go to shop') # 업그레이드 장비 등등
            print('5. Auction house') # 경매장
            print('6. Go to menu')
            print('7. Open inventory') # 인벤토리
            print('8. Go a drive') # 상점에서 차량 구매후 이용 가능
            print('9. Save and quit')
            select = module.input_int(0, 9, '입력: ', '잘못된 입력입니다.') 
            module.enter()
            if select == 0:
                pass
            elif select == 1:
                while True:
                    diesel_price = round(self.load_price['diesel'], 2)
                    gasoline_price = round(self.load_price['gasoline'], 2)
                    electric_price = round(self.load_price['electric'], 2)
                    print('기름 상점에 오신걸 환영합니다.')
                    print('구매를 희망하는 종류의 ')
            elif select == 2:
                pass
            elif select == 3:
                self.go_to_the_next_day()

    def menu(self):
        module.enter()
        module.clear()
        while True:
            print('뇌절 주유소에 오신걸 환영합니다.')
            select = module.input_int(1, 4,"""
1. 로그인
2. 계정 생성
3. 크레딧
4. 게임 종료
입력: """, '잘못된 입력입니다.')
            module.enter()
            if select == 1:
                sign_in = auth.sign_in()
                module.enter()
                module.clear()
                if sign_in[1]:
                    self.id = sign_in[0]["id"]
                    break
            elif select == 2:
                auth.sign_up()
                module.enter()
                module.clear()
            elif select == 3:
                pass
            else:
                module.shut_down()
    # load
    def load_money(self):
        self.money = setting.players.find_one({
                'id': self.id
            }, {'money': 1, '_id': 0})['money']

    def load_diesel(self):
        self.diesel = setting.players.find_one({
                'id': self.id
            }, {'diesel': 1, '_id': 0})['diesel']
        
    def load_gasoline(self):
        self.gasoline = setting.players.find_one({
                'id': self.id
            }, {'gasoline': 1, '_id': 0})['gasoline']
    
    def load_price(self):
        price = setting.price.find_one({
                'price': {'$exsits': True}
            }, {'price':1, '_id': 0})
        return price

    # others
    def wait_for_a_vehicle(self):
        pass
    
    def refill(self):
        pass

    def show_current_status(self):
        pass

    def go_to_the_next_day(self):
        setting.players.update_one({
            'id': self.id
        }, {'$inc': {'day': 1}})
        self.day = setting.players.find_one({'id': self.id}, {'day':1, '_id': 0})['day']
        print('다음날로 넘어갑니다.')
        print(f'현재 일차: {self.day}')
        module.enter()
        #TODO 조건 추가

    def go_to_shop(self):
        pass

    def auction_house(self):
        if self.money >= 1000000:
            print('경매장에 오신걸 환영합니다.')
            print('회원님의 정보를 동기화 중입니다.')
            self.auction_house_membership = setting.players.find_one({
                'id': self.id
            }, {'auction_house_membership_level': 1, '_id':0})['auction_house_membership_level']
            print(f'회원 이름: {self.id}, 회원 등급: {self.auction_house_membership}등급')
            print('동기화 완료! ')
            if self.auction_house_membership == 1:
                print('환영합니다, VIP님.')
            elif self.auction_house_membership == 0:
                print('환영합니다, VVIP님.')
            else:
                print('환영합니다.')
            module.enter()
            while True:
                select = module.input_int(1, 4,"""
1. 경매장 나가기
2. 상품 등록
3. 상품 구매
4. 멤버쉽 구매
""", '잘못된 입력입니다.')
                if select == 1:
                    break
                elif select == 2:
                    pass
                elif select == 3:
                    pass
                else:
                    next = self.auction_house_membership - 1
                    print(f'현재 회원 등급: {self.auction_house_membership}')
                    print(f'다음 등급: {next}')
                    price = {
                        4:15000000,
                        3:50000000,
                        2:150000000,
                        1:500000000,
                        0:1000000000
                        }
                    print(F'멤버쉽 {next}등급 가격은 {price[next]}만 달러입니다.')
                    select = module.input_int(1,2, """
1. 구매
2. 취소
""", "잘못된 입력입니다.")
                    if select == 1:
                        self.money -= price
                        self.decrease_money(price)
                        module.enter()
                    else:
                        module.enter()
                        continue

        else:
            print('경호실장: 진입 불가하십니다.')
            return

    def increase_money(self, amount):
        setting.players.update_one({'id': self.id}, {"$inc": {'money': amount}})

    def decrease_money(self, amount):
        setting.players.update_one({'id': self.id}, {"$ind": {'money': -amount}})

    def open_inventory(self):
        pass

    def save_and_quit(self):
        pass

    def credit(self):
        pass

    def upload_auction(self):
        pass

player = GasStation()
player.main()