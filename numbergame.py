import random
import module
import time


picked_number = random.randint(1,100)
left_life = 5

while True:

    player_num = module.input_int(1, 100, "숫자를 고르세요: ", "잘못된 입력입니다.")

    if player_num == picked_number:
        print("게임 클리어.")
        time.sleep(2)
        module.shut_down()

    elif player_num > picked_number:
        left_life -= 1
        print("숫자가 더 작습니다.")
        time.sleep(0.5)
        print(f"남은 목숨:  {left_life}")
        module.enter()
    
    elif player_num < picked_number:
        left_life -= 1
        print("숫자가 더 큽니다.")
        time.sleep(0.5)
        print(f"남은 목숨:  {left_life}")
        module.enter()
        