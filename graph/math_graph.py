import math
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

def parse_functions(exprs):
    funcs = []
    for expr in exprs.split(","):
        expr = expr.strip()
        funcs.append(lambda x, expr=expr: eval(expr, {"np": np, "x": x}))
    return funcs

# 여러 개의 식 입력 가능
expr_input = input("함수식을 입력하세요. 여러 개는 쉼표로 구분 (예: np.sin(x), x**2 + 3*x):\n")
functions = parse_functions(expr_input)

x = np.linspace(-10, 10, 1000)
plt.figure()

for f in functions:
    y = f(x)
    plt.plot(x, y, label=f.__defaults__[0])  # 식 이름 표시

plt.legend()
plt.title("Multiple Function Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
