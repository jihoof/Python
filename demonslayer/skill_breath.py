import os
import sys
import math
import status_effect

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

import module

class PhantomSunCrimson(): #환일홍
    def __init__(self):
        self.name = "「환일홍」"
        self.damage_ratio = 1500
        self.breath_damage_ratio = 1500
        self.reflect_damage_ratio = 1000 #반격
        self.explantiton = (
            f"자신에게 환일홍(10턴 지속, 특수, 중복 불가) 상태를 부여한다."
            f"자신이 환일홍 상태일시: 모든 종류의 공격을 회피한다(99% 확률, 디버프 포함), 근접 공격을 반격한다.(90%확률, " \
            f"반격 데미지 비율: 자신의 체술의 {self.reflect_damage_ratio}%, 적에게 재생억제(V)를 부여한다(99턴 지속, 특수, 중첩 가능, 제거/약화 불가))"
            f"자신의 체력을 5% 회복한다."
            f'지정적에게 체술 {self.damage_ratio}%, 호흡 {self.breath_damage_ratio}%의 복합 공격을 가한다.'
            f'지정적에게 재생억제(V)를 부여한다(99턴 지속, 특수, 중첩 가능, 제거/약화 불가).'
            f'자신에게 필중효과를 부여한다.'
            f'자신에게 실명무시를 부여한다.' 
        )

        self.self_status_effect = [status_effect.RecoverHp(), status_effect.PhantomSunCrimsonStatEffect()]
        self.enemy_status_effect = [status_effect.RegenerationInhibitionV()]

class DragonSunHaloHeadDance(): #햇무리의 용·두무
    def __init__(self):
        self.name = "「햇무리의 용·두무」"
        self.damage_ratio = 2500
        self.breath_damage_ratio = 5000
        self.explantiton = (
            f'자신의 호흡이 200%증가한다(7턴 지속, 특수, 중복불가).'
            f'자신의 체술이 200%증가한다(7턴 지속, 특수, 중복불가).'
            f'자신에게 실명무시를 부여한다(1턴 지속).'
            f'자신에게 필중 효과를 부여한다(1턴 지속).'
            f"지정적에게 체술 {self.damage_ratio}%, 호흡 {self.breath_damage_ratio}%의 복합 근접 공격(총 6타)를 가한다."
            f'지정적에게 재생억제(V)를 부여한다(99턴 지속, 특수, 중첩 가능, 제거/약화 불가).'
            f'지정적에게 태양의 낙인(X)를 부여한다(99턴 지속, 특수, 최대 10중첩, 제거/약화 불가.)' #태양의 낙인이 걸려 있는 적에게 1중첩당 매턴 최대 체력의 1%의 백분율 대미지를 입힌다 최대 10% 최소 9% 풀중첩 기준
            # 백분율 대미지 저항을 90% 무시한다. 적에게 받는 대미지 증가(1중첩당 50%)를 부여한다. 모든 종류의 저항을 90% 무시한다. 최대 500% 최소 450% 풀중첩 기준.
        )

        self.self_status_effect = []
        self.enemy_status_effect = [status_effect.BrandOfTheSunX(), status_effect.RegenerationInhibitionV()]