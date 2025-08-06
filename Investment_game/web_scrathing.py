import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def get_naver_stock_price(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    price_tag = soup.select_one("p.no_today span.blind")
    if price_tag:
        price_text = price_tag.text.replace(",", "")
        return int(price_text)
    else:
        return None

def save_stock_price_csv(company_name, code, price):
    today = datetime.today().strftime("%Y-%m-%d")
    row = [today, company_name, code, price]

    with open("Investment_game\stock_data.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

if __name__ == "__main__":
    # 예시: 삼성전자
    company_name = "삼성전자"
    code = "005930"

    price = get_naver_stock_price(code)
    if price:
        print(f"{company_name} 주가: {price}원")
        save_stock_price_csv(company_name, code, price)
        print("✅ 주가 정보 저장 완료 (CSV)")
    else:
        print("❌ 주가 정보를 가져올 수 없습니다.")
