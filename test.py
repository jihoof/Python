year, month, day = input("년도 월 그리고 날짜를 입력하세여: ").split("/")
print(f"{year}/{month}/{day}")
year = int(year)
year += 10
print(f"{year}/{month}/{day}")