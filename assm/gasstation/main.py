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
            if select == 0:
                pass
            elif select == 1:
                while True:
                    diesel_price = round(self.load_price['diesel'], 2)
                    gasoline_price = round(self.load_price['gasoline'], 2)
                    electric_price = round(self.load_price['electric'], 2)
                    print('기름 상점에 오신걸 환영합니다.')
                    print('구매를 희망하는 종류의 ')

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
            }, {'money': 1, '_id': 0})

    def load_diesel(self):
        self.diesel = setting.players.find_one({
                'id': self.id
            }, {'diesel': 1, '_id': 0})

    def load_gasoline(self):
        self.gasoline = setting.players.find_one({
                'id': self.id
            }, {'gasoline': 1, '_id': 0})
    
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
        pass

    def go_to_shop(self):
        pass

    def auction_house(self):
        pass

    def open_inventory(self):
        pass

    def save_and_quit(self):
        pass

player = GasStation()
player.menu()