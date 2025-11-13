import random
import time
import math
import sys

def input_int_minmax(min_v, max_v, prompt, err_msg):
    """단순한 정수 입력 헬퍼 (원래 module.input_int 대체)"""
    while True:
        try:
            s = input(prompt)
            v = int(s)
            if v < min_v or v > max_v:
                print(err_msg)
                continue
            return v
        except ValueError:
            print(err_msg)

def roulette_gamble():
    # 사용자 입력
    betting_money = input_int_minmax(100, 9999999999999999999, 
                                     '베팅할 금액을 입력하세요. *최소 금액은 100달러입니다: ',
                                     '잘못된 입력입니다')

    # 원문 텍스트(확률표) — 그대로 출력
    print("""도박 확률:
    x0: 31%
    x1: 31%
    x2: 21%
    x3: 11%
    x4: 4%
    x5: 2% """)
    time.sleep(0.8)

    # 확률 분포(총합 100) — 원문 비율을 리스트로 만듦
    sectors = []
    sectors += ['x0'] * 31
    sectors += ['x1'] * 31
    sectors += ['x2'] * 21
    sectors += ['x3'] * 11
    sectors += ['x4'] * 4
    sectors += ['x5'] * 2
    # 확인: len(sectors) == 100

    # 룰렛 애니메이션 준비
    wheel = ['x0','x1','x2','x3','x4','x5']  # 시각적 회전용 (고정된 6칸)
    # 실제 결과은 sectors(확률 리스트)에서 랜덤 추출
    chosen_index = random.randint(0, 99)   # 0..99
    result_label = sectors[chosen_index]   # 예: 'x2'

    # 애니메이션: 휠이 빠르게 돌다가 점점 느려져서 결과에 정지
    # 표현 방법: wheel 리스트를 계속 순환하면서 현재 포인터 위치를 출력
    spin_cycles = random.randint(3, 6)  # 전체 반복 횟수
    total_steps = spin_cycles * len(wheel) + (['x0','x1','x2','x3','x4','x5'].index(result_label) if result_label in wheel else 0)
    # 위의 단순 정지 인덱스가 정확히 결과와 매치되지 않을 수 있으므로, 대신
    # 우리는 확률 기반의 sectors에서 나온 결과를 시각적으로 맞추기 위해
    # final_slot_index를 계산 (wheel의 인덱스들 중 하나로 착지)
    # map label -> wheel index (시각적으로 배치)
    label_to_wheel_index = {'x0':0, 'x1':1, 'x2':2, 'x3':3, 'x4':4, 'x5':5}
    final_wheel_index = label_to_wheel_index[result_label]

    # 이제 실제 애니메이션 스텝을 계산: 충분히 돌다가 final_wheel_index로 멈춤
    # 시작 위치 랜덤
    pos = random.randint(0, len(wheel)-1)
    steps = random.randint(30, 50)  # 최소 회전 스텝 (시각적으로 충분히 돌게)
    steps += final_wheel_index - (pos + steps) % len(wheel)  # 보정해서 정확히 멈춤

    # 애니메이션 루프
    delay = 0.03
    for step in range(steps + 1):
        current = (pos + step) % len(wheel)
        # 출력: wheel을 한 줄로 보여주고 현재 포인터 강조
        # 예: [ x0 ] x1 [x2] x3 x4 x5  -> 현재는 x2 에 포인터
        display = []
        for i, label in enumerate(wheel):
            if i == current:
                display.append(f"[{label}]")
            else:
                display.append(f" {label} ")
        sys.stdout.write("\r" + " ".join(display))
        sys.stdout.flush()
        # 점점 느려지게
        time.sleep(delay)
        delay *= 1.03  # 느려짐

    print()  # 줄 바꿈

    # 결과 출력 및 배당 적용 (원래 코드 의도대로 multiplier 적용)
    multiplier_map = {'x0':0, 'x1':1, 'x2':2, 'x3':3, 'x4':4, 'x5':5}
    multiplier = multiplier_map[result_label]
    payout = betting_money * multiplier

    print(f"룰렛 결과: {result_label} (배수: x{multiplier})")
    if multiplier == 0:
        print(f"안타깝습니다. 베팅 금액 ${betting_money} 전부를 잃었습니다.")
    else:
        print(f"축하합니다! 당신은 ${betting_money} → ${payout} 를 획득했습니다.")

    return result_label, multiplier, payout

if __name__ == "__main__":
    roulette_gamble()
