h, m = map(int, input().split())
add = int(input())

m += add
while True:
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h = 0
    else:
        break

print(h, m)