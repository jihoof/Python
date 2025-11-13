import os
import sys
import math
import status_effect

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

import module

#치명타 종류
#소 1.5배
#중 2배 기본
#대 2.5배
#특대 3배

class FlashCut():
    def __init__(self):
        self.name = "「일섬」"
        self.damage_ratio = 4500
        self.damage_ratio_breath = 500
        self.explanition = (
            f"자신에게 치명타 저항 무시(100%)를 부여한다(3턴 지속). "
            f"자신의 체술이 200% 증가한다(7턴 지속, 특수, 중복불가). "
            f"자신에게 필중효과를 부여한다(1턴 지속). "
            f"자신에게 실명무시를 부여한다(1턴 지속). "
            f"지정적에게 재생 억제(V)를 부여한다.(99턴 지속, 특수, 중첩 가능, 제거/약화 불가.)" #v를 로마 숫자 5단계 최고단계
            f"지정적에게 체술 {self.damage_ratio}%, 호흡 {self.damage_ratio_breath}%의 복합 근접 공격(총 3타)를 가한다. "
            f"마지막 공격때 무조건 치명타기 발동된다(치명타 대미지 비율: 특대)" # 3배 원래는 중으로 2배
            # 1타 좌측에서 우측으로 광속 베기, 2타 반대방향 반베기, 3타 전방 일섬으로 마무리 
            # 벽력일섬 업그레이드판. 요리이치는 모든 호흡의 시초.
        )
        self.self_status_effect = [status_effect.BlindnessResistance(), status_effect.GuaranteedHit(), status_effect.IncreaseMartialArtLevel(), status_effect.IgnoresCriticalResistance()] #자신에게 부여 효과
        self.enemy_status_effect = [status_effect.RegenerationInhibitionV()] #적에게 부여 효과

        