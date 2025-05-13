def coin(money):
    fh = money // 500
    oh = money % 500 // 100
    fih = money % 500 % 100 // 50
    th = money % 500 % 100 % 50 //10
    return fh, oh, fih, th

money = int(input())
print(coin(money))