import requests
import re
from bs4 import BeautifulSoup

for i in range(1, 6):
    print("페이지", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)


    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # print(res.text)

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # re.compile : 정규 표현식
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:
        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print(" 광고 상품 제외")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        # 애플 제품 제외
        if "Apple" in name:
            print(" Apple 상품 제외")
            continue

        price = item.find("strong", attrs={"class":"price-value"})
        if price:
            price = price.get_text()
        else:
            print(" 가격 정보 없음")
            continue

        # 평점 4.5 이상, 리뷰 100개 이상
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            print("평점 없음")
            continue

        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
        else:
            print("리뷰 없음")
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]


        if float(rate) >= 4.5 and int(rate_count) >= 200:
            # print(name, price, rate, rate_count)
            print("""제품명 : {0}
            가격 : {1}
            평점 : {2}
            리뷰 개수 : {3}
            바로가기 : {4}
            """.format(name, price, rate, rate_count, "https://www.coupang.com" + link))
            print("-" * 100)