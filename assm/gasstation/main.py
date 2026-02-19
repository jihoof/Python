from .libs.module import input_int, enter, clear, shut_down, input_str, beautiful_table
from .libs.auth import sign_up, sign_in
from .db import players, auction
from .db.transaction import load_money, load_diesel, load_gasoline, load_day, load_rating, load_handled_customers, decrease_money, load_items, load_price, load_blackmarket_product
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
            select = input_int(0, 9, '입력: ', '잘못된 입력입니다.') 
            enter()
            if select == 0:
                pass
            elif select == 1:
                while True:
                    diesel_price = round(load_price['diesel'], 2)
                    gasoline_price = round(load_price['gasoline'], 2)
                    electric_price = round(load_price['electric'], 2)
                    print('기름 상점에 오신걸 환영합니다.')
                    print('구매를 희망하는 종류의 ')
                      
            elif select == 2:
                self.show_current_status()

            elif select == 3:
                self.go_to_the_next_day()

            elif select == 4:
                self.go_to_shop()

            elif select == 5:
                self.auction_house()

    def menu(self):
        enter()
        clear()
        
        while True:
            print('뇌절 주유소에 오신걸 환영합니다.')
            select = input_int(1, 4, "1. 로그인\n2. 계정 생성\n3. 크레딧\n4. 게임 종료\n입력: ", '잘못된 입력입니다.')
            enter()
            
            if select == 1:
                sign_in_ = sign_in()
                enter()
                clear()
                if sign_in_[1]:
                    self.id = sign_in_[0]["id"]
                    break
                
            elif select == 2:
                sign_up()
                enter()
                clear()
                
            elif select == 3:
                pass
            
            else:
                shut_down()
    # load

    # others
    def wait_for_a_vehicle(self):
        pass
    
    def refill(self):
        pass

    def show_current_status(self):
        self.day = load_day(self.id)
        self.money = load_money(self.id)
        self.diesel = load_diesel(self.id)
        self.gasoline = load_gasoline(self.id)
        self.rating = load_rating(self.id)
        self.handled_customers = load_handled_customers(self.id)
        
        print('-'*8+'STATUS'+'-'*8)
        print(f'Day: {self.day}')
        print(f'Rating: {self.rating}')
        print(f'Money: {self.money}')
        print(f'Total Customers Handled: {self.handled_customers}')
        print(f'Left Diesel: {self.diesel}')
        print(f'Left Gasoline: {self.gasoline}')
        print('-'*22)
        enter()

    def go_to_the_next_day(self):
        self.day = load_day(self.id)
        self.money = load_money(self.id)
        next_money = 100*(1.25 ** (self.day+1))
        print(f'다음날로 넘어가기 위한 조건: {next_money} 달러 필요.')
        sleep(1)
        enter()
        if self.money >= next_money:
            decrease_money(self.id, next_money)
            players.update_one({
                'id':self.id
            }, {'$inc': {'multiplier': 0.1}})
            players.update_one({
                'id': self.id
            }, {'$inc': {'day': 1}})
            self.day = load_day(self.id)
            print('다음날로 넘어갑니다.')
            print(f'현재 일차: {self.day}')
            enter()
        else:
            print('조건을 만족하지 않았습니다.')
            enter()
            return None
        

    def go_to_shop(self):
        print('사상 최대 규모의 암시장, 블랙마켓에 오신걸 환영합니다.')
        select = input_int(1,3,"""
1. 상품 보기
2. 블랙마켓 지분 인수하기
3. 블랙마켓 나가기
입력: 
""", "잘못된 입력입니다.")
        if select == 1:
            print('구매 가능한 모든 상품의 중류을 출력합니다.')
            beautiful_table(load_blackmarket_product(), title='상품 목록')
            select = input_str('구매 하고 싶은 물건의 이름을 적어주세요.\n입력: ', '존재하지 않는 품목입니다. ', [n['name'] for n in load_blackmarket_product()])
            enter()
            if load_money() > dict(load_blackmarket_product()):


        elif select == 2:
            pass
        else:
            print('주유소로 복귀합니다.')
            enter()
            return None

    def auction_house(self):
        money = load_money(self.id)
        print(money)
        if money >= 1000000:
            print('\n사상 최대 규묘의 경매장 The Black Tear에 오신걸 환영합니다.\n회원님의 정보를 동기화 중입니다.')
            
            auction_house_membership = players.find_one({
                'id': self.id
            }, {'auction_house_membership_level': 1, '_id':0})['auction_house_membership_level']

            call_name = {
                0:'VVIP',
                1:'VIP',
            }
            print(f'\n회원 이름: {self.id}, 회원 등급: {auction_house_membership}등급')
            print(f"환영합니다, {call_name.get(auction_house_membership, '일반회원')}님.\n")
            
            enter()
            while True:
                select = input_int(1, 4,"1. 경매장 나가기\n2. 상품 등록\n3. 상품 구매 \n4. 멤버쉽 구매", '잘못된 입력입니다.')
                
                if select == 1:
                    print('\n경매장을 나갑니다.')
                    break
                
                elif select == 2:
                    print('\n현재 보유중인 모든 아이템, 기름, 차량을 출력합니다.')
                    diesel = load_diesel(self.id)   
                    gasoline = load_gasoline(self.id)
                    items = load_items(self.id)    
                    
                    print("-"*8 + "INVENTORY" + "-"*8)
                    print(f"현재 보유 중인 디젤: {diesel}\n현재 보유 중인 가솔린: {gasoline}\n")
                    for item in items:
                        print(f"아이템: {item['name']}, 보유 개수: {item['cnt']}")
                    print("-"*22)
                    
                    select = input_str('입력: ', '잘못된 입력입니다.', ['가솔린', '디젤'] + [key['name'] for key in load_items(self.id)])
                    select2 = input_int(10000, 9**99, '상품의 가격을 입력하세요: ', '최소가격 미달 또는 상한 초과.')
                    select3 = input('상품 설명을 입력하세요.')
                    try:
                        auction.insert_one({
                            'name': select,
                            'price': select2,
                            'product_introduce': select3,
                            'proposal': []
                        })
                    except:
                        print('Unexpected fatal error occured. error code: -1')
                        sleep(2)
                        print('Rebooting faliure')
                        print('시스템을 강제 종료합니다.')
                        sleep(2)
                        shut_down()

                elif select == 3:
                    pass
                else:
                    next = auction_house_membership - 1
                    print(f'현재 회원 등급: {auction_house_membership}, 다음 등급: {next}')
                    price = {
                        4: 15000000,
                        3: 50000000,
                        2: 150000000,
                        1: 500000000,
                        0: 900000000
                    }
                    print(F'멤버쉽 {next}등급 가격은 {price[next]}만 달러입니다.')
                    select = input_int(1,2, "1. 구매\n2. 취소\n입력: ", "잘못된 입력입니다.")
                    if select == 1:
                        money -= price[next]
                        decrease_money(self.id, price[next])
                        enter()
                    else:
                        enter()
                        continue

        else:
            print('경호실장: 진입 불가하십니다.')
            enter()
            return

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