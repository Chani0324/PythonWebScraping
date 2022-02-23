import requests
from bs4 import BeautifulSoup
import csv

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline : 데이터 row 간 공간 설정
writer = csv.writer(f) # writer를 통해 csv에 데이터 쓰기

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") # tab 구간을 ,로 구분하여 리스트로 저장
writer.writerow(title)

for page in range(1, 5):
    res = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)