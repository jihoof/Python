import pygame
import math
import sys

pygame.init()

# 화면 크기 설정
W, H = 1200, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Infinite Zoom Graph")
clock = pygame.time.Clock()

# 중심 좌표, 카메라 위치, 스케일 설정
center = pygame.Vector2(W / 2, H / 2)
camera = pygame.Vector2(0.0, 0.0)
scale = 100.0

# 상태 변수
dragging = False
last_mouse = None

# 폰트와 색상
font = pygame.font.SysFont("Consolas", 14)
BG = (10, 10, 25)
GRID = (40, 40, 60)
AXIS = (200, 200, 230)
TEXT = (190, 220, 255)

# === 좌표 변환 ===
def screen_to_world(px, py):
    wx = camera.x + (px - center.x) / scale
    wy = camera.y + (center.y - py) / scale
    return pygame.Vector2(wx, wy)

def world_to_screen(wx, wy):
    sx = center.x + (wx - camera.x) * scale
    sy = center.y - (wy - camera.y) * scale
    return pygame.Vector2(sx, sy)

# === 눈금 간격 계산 ===
def nice_step_for_scale(scale):
    target_pixels = 120.0
    raw = target_pixels / max(scale, 1e-30)
    exp = math.floor(math.log10(raw))
    base = raw / (10 ** exp)
    if base <= 1.5:
        base = 1.0
    elif base <= 3.5:
        base = 2.0
    else:
        base = 5.0
    return base * (10 ** exp)

# === 숫자 포맷 ===
def fmt_number(x):
    ax = abs(x)
    if ax == 0:
        return "0"
    if ax < 1e-3 or ax >= 1e5:
        return f"{x:.3e}"
    return f"{x:.6g}"

# === 그래프 그리기 ===
def draw_grid():
    screen.fill(BG)
    step = nice_step_for_scale(scale)

    # 현재 화면의 월드 범위 계산
    top_left = screen_to_world(0, 0)
    bottom_right = screen_to_world(W, H)
    left = top_left.x
    right = bottom_right.x
    top = top_left.y
    bottom = bottom_right.y

    # 수직선 (x = const)
    start_x = math.floor(left / step) * step
    x = start_x
    while x <= right:
        p = world_to_screen(x, 0)
        color = AXIS if abs(x) < step * 0.5 else GRID
        pygame.draw.line(screen, color, (p.x, 0), (p.x, H))
        label = fmt_number(x)
        if abs(x) > step * 1e-3:
            surf = font.render(label, True, TEXT)
            screen.blit(surf, (p.x + 3, center.y + 3))
        x += step

    # 수평선 (y = const)
    start_y = math.floor(bottom / step) * step
    y = start_y
    while y <= top:
        p = world_to_screen(0, y)
        color = AXIS if abs(y) < step * 0.5 else GRID
        pygame.draw.line(screen, color, (0, p.y), (W, p.y))
        label = fmt_number(y)
        if abs(y) > step * 1e-3:
            surf = font.render(label, True, TEXT)
            screen.blit(surf, (center.x + 5, p.y + 3))
        y += step

# === 메인 루프 ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 줌 인/아웃
        elif event.type == pygame.MOUSEWHEEL:
            mouse_px = pygame.Vector2(pygame.mouse.get_pos())
            before = screen_to_world(mouse_px.x, mouse_px.y)
            factor = 1.2 if event.y > 0 else (1 / 1.2)
            scale *= factor
            scale = max(min(scale, 1e12), 1e-12)
            after = screen_to_world(mouse_px.x, mouse_px.y)
            camera += before - after  # 커서 기준 고정 줌

        # 마우스 드래그
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            last_mouse = pygame.Vector2(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            cur = pygame.Vector2(event.pos)
            delta_px = cur - last_mouse
            camera.x -= delta_px.x / scale
            camera.y += delta_px.y / scale
            last_mouse = cur

    draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
