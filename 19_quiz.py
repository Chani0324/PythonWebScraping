### 네이버 부동산 매물 scraping ###

from selenium import webdriver
import time
from bs4 import BeautifulSoup

# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.naver.com"
browser.get(url)

# 검색어 창 클릭 후 입력
elem_search_window = browser.find_element_by_class_name("input_text").send_keys("송파 헬리오시티")

# 검색
elem_search = browser.find_element_by_class_name("btn_submit").click()

time.sleep(2)

# 부동산 더보기란 클릭
elem_more = browser.find_element_by_class_name("more_icon_inner").click()



# 매물 정보 가져오기 + 새로운 창으로 전환
time.sleep(6)

last_tab = browser.window_handles[-1]
browser.switch_to.window(window_name=last_tab)

soup = BeautifulSoup(browser.page_source, "lxml")

sells = soup.find_all("a", attrs={"class":"item_link"}) # 되는 tag 잘 찾아서 해야되는건지? 아니면 특정 tag만 찾으면 되고 다른건 안되는건지...
print(len(sells))

for idx, sell in enumerate(sells):
    title = sell.find("span", attrs={"class":"text"}).get_text()
    price = sell.find("span", attrs={"class":"price"}).get_text()
    sell_type = sell.find("span", attrs={"class":"type"}).get_text()

    spec = sell.find("span", attrs={"class":"spec"}).get_text()
    area = spec[ : spec.index(",")]
    sell_floor = spec[spec.index(",") + 1 : spec.index(",", spec.index(",") + 1)]
    
    print(""" ====== 매물 {0} ======
    거래 : {1}
    면적 : {2}
    가격 : {3}
    동 : {4}
    층 : {5}
    """.format(idx + 1, sell_type, area, price, title, sell_floor))

while True:
    pass