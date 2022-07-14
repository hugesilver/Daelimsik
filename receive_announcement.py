from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

option = Options()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=900#page1')
sleep(5)
html_900 = driver.page_source
driver.quit() # 웹드라이버 종료
f900 = open("./data/html_900.txt", 'w')
f900.write(html_900)
f900.close()

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=990#page1')
sleep(5)
html_990 = driver.page_source
driver.quit() # 웹드라이버 종료
f990 = open("./data/html_990.txt", 'w')
f990.write(html_990)
f990.close()

f900 = open("./data/html_900.txt", 'r')
html = f900.read()
f900.close()

soup = BeautifulSoup(html, 'html.parser')

m_900 = open("./data/l_bachelor.json", 'w')

m_900.write('{"version": "2.0","template": {"outputs": [{"listCard": {"header": {"title": "대림대학교 학사공지"},"items": [')

for i in range(5):
    m_900.write('{')
    m_900.write('"title": "{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a').get_text()))
    m_900.write('"description": "{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtInfo > .date').get_text()))
    m_900.write('"link": {')
    m_900.write('"web": "{}"'.format("https://www.daelim.ac.kr" + ((((str(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a')).split())[6])[6:])[:-1]).replace("amp;", "")))
    m_900.write('}')
    if(i != 4):
        m_900.write('},')
    else:
        m_900.write('}')

m_900.write('],')
m_900.write('"buttons": [{"label": "학사공지 전체보기", "action": "webLink", "webLinkUrl": "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=900#page1"}]}}]}}')
m_900.close()

f990 = open("./data/html_990.txt", 'r')
html = f990.read()
f990.close()

soup = BeautifulSoup(html, 'html.parser')

m_990 = open("./data/l_scholar.json", 'w')

m_990.write('{"version": "2.0","template": {"outputs": [{"listCard": {"header": {"title": "대림대학교 장학 및 대출공지"},"items": [')

for i in range(5):
    m_990.write('{')
    m_990.write('"title": "{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a').get_text()))
    m_990.write('"description": "{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtInfo > .date').get_text()))
    m_990.write('"link": {')
    m_990.write('"web": "{}"'.format("https://www.daelim.ac.kr" + ((((str(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a')).split())[6])[6:])[:-1]).replace("amp;", "")))
    m_990.write('}')
    if(i != 4):
        m_990.write('},')
    else:
        m_990.write('}')

m_990.write('],')
m_990.write('"buttons": [{"label": "장학 및 대출공지 전체보기", "action": "webLink", "webLinkUrl": "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=990#page1"}]}}]}}')
m_990.close()