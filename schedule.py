from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import date

option = Options()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

today = date.today()

m_930 = open("./data/m_schedule.json", 'w')

m_930.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_930.write("[대림식 알림]\\n")
m_930.write("\\n")
m_930.write("{}년 {}월 학사일정입니다.\\n".format(today.year, today.month))
m_930.write("\\n")

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=930')
sleep(3)
schedule = driver.page_source
driver.quit() # 웹드라이버 종료

soup = BeautifulSoup(schedule, 'html.parser')

ul = soup.select_one('#month{} > ul'.format(str(today.month)))
li = ul.select('li')

for i in li:
    if i is li[-1]:
        m_930.write("[{}]\\n{} | {}".format(i.select_one('strong').get_text(), i.select_one('p > .sort').get_text(), i.select_one('p').get_text()[2:]))
    else:
        m_930.write("[{}]\\n{} | {}".format(i.select_one('strong').get_text(), i.select_one('p > .sort').get_text(), i.select_one('p').get_text()[2:]))
        m_930.write("\\n")
        m_930.write("\\n")

m_930.write('"}}],"quickReplies":[{"action": "block", "messageText": "전체 학사일정 보기", "label": "전체 학사일정 보기", "blockId": "6315901ce40f1940e6d747ba"}]}}')
m_930.close()