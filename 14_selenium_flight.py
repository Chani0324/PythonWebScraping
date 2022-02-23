from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# browser.find_element_by_link_text("가는 날").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()


time.sleep(3)

# 이번 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # 리스트 없다고 나옴.. 검색해도 아직은 해결 못하겠음. 창 늦게 뜨는게 새로운 frame에 되는건지..
# browser.find_elements_by_link_text("28")[0].click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button/b").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b").click()

time.sleep(2)

# 도착지 제주도
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()

time.sleep(1)

# 항공권 검색 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

try:
    elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/div[1]")))
    # 결과 출력
    elem_1 = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/div[1]")
    elem_2 = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/div[2]")
    print(elem_1.text)
    print(elem_2.text)
finally:
    browser.quit()


while True:
    pass