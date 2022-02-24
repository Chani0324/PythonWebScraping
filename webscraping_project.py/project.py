import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

### 오늘의 날씨 ###
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%9F%AC%EC%8B%9C%EC%95%84+%EB%AF%B8%EC%82%AC%EC%9D%BC&tqi=hmN7Csp0Jy0ssiBx5OGsssssssK-080287"
    soup = create_soup(url)


    # attrs={'':['', '']} or 조건으로 찾는 방법과 attrs={'':'', '':''} and 조건으로 찾는 방법알아두기
    summary = soup.find("p", attrs={"class":"summary"}).get_text() 
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip() # strip() : 빈공간 없어지게 함.
    min_temp = soup.find("span", attrs={"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"highest"}).get_text()
    mor_rainfall = soup.find_all("span", attrs={"class":"rainfall"})[0].get_text()
    eve_rainfall = soup.find_all("span", attrs={"class":"rainfall"})[1].get_text()
    dust = soup.find_all("li", attrs={"class":"item_today level1"})[0].get_text().strip()
    small_dust = soup.find_all("li", attrs={"class":"item_today level1"})[1].get_text().strip()

    # 출력
    print(summary)
    print("{0} / {1} / {2}".format(curr_temp, min_temp, max_temp))
    print("오전 강수 확률 {0}, 오후 강수 확률 {1}".format(mor_rainfall, eve_rainfall))
    print()
    print("{0}, {1}".format(dust, small_dust))
    print()
    print()

### 헤드라인 뉴스 ###
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    
    for i in range(0, 6):
        url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{0}".format(i)
        soup = create_soup(url)

        clusters = soup.find_all("div", attrs={"class":"cluster_group _cluster_content"})
        # print(len(clusters))
        news = ["pol", "eco", "nav", "lif", "wor", "sci"]
        head_news = ["정치", "경제", "사회", "생활/문화", "세계", "IT/과학"]
        
        for idx, cluster in enumerate(clusters):
            cluster = clusters[idx].find("a", attrs={"class":"cluster_text_headline nclicks(cls_{0}.clsart)".format(news[i])}).get_text()
            link = clusters[idx].find("a", attrs={"class":"cluster_text_headline nclicks(cls_{0}.clsart)".format(news[i])})["href"]
        
            print("""      ====== {0} {1} 번째 헤드라인 뉴스 ======
            기사 : {2}
            링크 : {3}
            """.format(head_news[i], idx + 1, cluster, link))

            if idx == 2:
                print("=" * 150)
                break
    

def scrape_english():
    print("[오늘의 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("[영어 지문]")
    for sentence in sentences[len(sentences)//2:]: # 8문장 있다고 가정할 때, index 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())

    print()
    print("[한글 지문]")
    for sentence in sentences[:len(sentences)//2]: # 8문장 있다고 가정할 때, index 기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())

    print()

if __name__ == "__main__":
    scrape_weather() # 오늘 날씨 정보 가져오기
    scrape_headline_news() # 오늘 뉴스 정보 가져오기
    scrape_english()