from bs4 import BeautifulSoup
import urllib.parse
from selenium import webdriver


def next_page(driver):
    try:
        # this is navigate to next page
        driver.find_element_by_xpath("//a[@class='nav next taLnk ui_button primary']")

        driver.implicitly_wait(2)

        return True
    except :
        return False


keyword='카페베네'
keyword_url = str(urllib.parse.quote(keyword))

trip_url='https://www.tripadvisor.co.kr'

url_list=[]
driver = webdriver.Chrome(
    'chromedriver/chromedriver_win.exe')


is_next = True

for i in range(34):             #페이지수를 확인해 넣어주세요
    if (i==0):
        url_naver = str("https://www.tripadvisor.co.kr/Search?geo=294196&pid=3826&q={}&ssrc=m&o={}&rf={}".format(keyword_url,(i*30),(i+1)))
        driver.get(url_naver)
        driver.implicitly_wait(10)
        driver.page_source
        response = driver.page_source

        soup = BeautifulSoup(response, 'html.parser',
                             from_encoding='utf-8')  # Beautifulsoup로 html의 구조를 정힌진 형태로 만들어냄
        print("++++++++++++++++++++++++++++++++++")

        tag_ul_infos = soup.findAll("div", {"class": "review-mention-block"})
    else :
        url_naver = str(
            "https://www.tripadvisor.co.kr/Search?geo=294196&pid=3826&q={}&ssrc=m&o={}&rf={}".format(keyword_url,
                                                                                                     (i * 30), (i + 1)))
        driver.get(url_naver)
        driver.implicitly_wait(10)
        driver.page_source
        response = driver.page_source

        soup = BeautifulSoup(response, 'html.parser',
                             from_encoding='utf-8')  # Beautifulsoup로 html의 구조를 정힌진 형태로 만들어냄
        print("++++++++++++++++++++++++++++++++++")

        tag_ul_infos = soup.findAll("div", {"class": "result-title"})

    for block in tag_ul_infos:

        mystr=block["onclick"]
        start_n=mystr.find('/')
        if (i==0):
            end_n=mystr.find('#')
            newstring = mystr[start_n:end_n]
        else:
            end_n = mystr.find("html")
            newstring = mystr[start_n:(end_n + 4)]

        full_url = str(trip_url+newstring)
        url_list.append(full_url)

        # print(i)
        # print(mystr)


with open(str(keyword + '_tripadviser_link.txt'), 'a+') as f:
    print(url_list)
    for i in range(len(url_list)):
        f.write(str(str(url_list[i])+"\n"))

