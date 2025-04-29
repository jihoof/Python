from numba import njit  # 빠른 계산을 위해 사용하는 데코레이터 (지금은 아직 안 씀)
import numpy as np  # 수학 계산용 라이브러리
import glm  # 벡터, 행렬 계산용 (OpenGL용 수학)
import math  # 기본적인 수학 함수 제공

# 화면 해상도 설정
WIN_RES = glm.vec2(1500, 800)

# 카메라 설정
ASPECT_RATIO = WIN_RES.x / WIN_RES.y  # 가로세로 비율
FOV_DEG = 50  # 수직 시야각 (도 단위)
V_FOV = glm.radians(FOV_DEG)  # 수직 시야각 (라디안 단위로 변환)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # 가로 시야각 계산
NEAR = 0.1  # 카메라에서 가장 가까운 그릴 수 있는 거리
FAR = 2000.0  # 카메라에서 가장 먼 그릴 수 있는 거리
PITCH_MAX = glm.radians(89)  # 위아래로 올릴 수 있는 최대 각도

# 플레이어 설정
PLAYER_SPEED = 0.005  # 이동 속도
PLAYER_ROT_SPEED = 0.003  # 회전 속도
PLAYER_POS = glm.vec3(0, 0, 1)  # 초기 위치
MOUSE_SENSITIVITY = 0.002  # 마우스 민감도

# 배경 색상 설정
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)  # 어두운 파란색 느낌
