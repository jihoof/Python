import tkinter as tk

root = tk.Tk()

# 원본 (큰 글씨)
label_big = tk.Label(root, text="◑ 이 폰트 사이즈", font=("Arial", 20))
label_big.pack()

# 줄인 버전 (같은 내용, 작은 글씨)
label_small = tk.Label(root, text="◑ 이 폰트 사이즈", font=("Arial", 10))
label_small.pack()

root.mainloop()
