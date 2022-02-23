import requests
from bs4 import BeautifulSoup
import csv

for page in range(1, 5):
    res = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find_all("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        print(data)
    