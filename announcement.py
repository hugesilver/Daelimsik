from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')


######################################### 학사공지 #########################################

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=900#page1')
sleep(3)
bachelor = driver.page_source
driver.quit() # 웹드라이버 종료

soup = BeautifulSoup(bachelor, 'html.parser')

m_900 = open("./data/l_bachelor.json", 'w')
m_900.write('{"version": "2.0","template": {"outputs": [{"listCard": {"header": {"title": "대림대학교 학사 공지사항"},"items": [')

for i in range(5):
    m_900.write('{')
    m_900.write('"title": ')
    if (soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .mark_num > span').get_text() == "공지"):
        m_900.write('"[공지] ')
    else:
        m_900.write('"')
    m_900.write('{}",'.format((soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a').get_text())).replace('"', '\"'))
    m_900.write('"description": "{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtInfo > .date').get_text()))
    m_900.write('"link": {')
    m_900.write('"web": "{}"'.format("https://www.daelim.ac.kr" + ((((str(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a')).split())[6])[6:])[:-1]).replace("amp;", "")))
    m_900.write('}')
    if(i != 4):
        m_900.write('},')
    else:
        m_900.write('}')

m_900.write('],')
m_900.write('"buttons": [{"label": "학사 공지사항 전체보기", "action": "webLink", "webLinkUrl": "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=900#page1"}]}}],"quickReplies":[{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_900.close()


######################################### 장학공지 #########################################

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=990#page1')
sleep(3)
scholarship = driver.page_source
driver.quit() # 웹드라이버 종료

soup = BeautifulSoup(scholarship, 'html.parser')

m_990 = open("./data/l_scholarship.json", 'w')

m_990.write('{"version": "2.0","template": {"outputs": [{"listCard": {"header": {"title": "대림대학교 장학 공지사항"},"items": [')

for i in range(5):
    m_990.write('{')
    m_990.write('"title": ')
    if(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .mark_num > span').get_text() == "공지"):
        m_990.write('"[공지] ')
    else:
        m_990.write('"')
    m_990.write('{}",'.format((soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a').get_text())).replace('"', '\"'))
    m_990.write('"description": "{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtInfo > .date').get_text()))
    m_990.write('"link": {')
    m_990.write('"web": "{}"'.format("https://www.daelim.ac.kr" + ((((str(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a')).split())[6])[6:])[:-1]).replace("amp;", "")))
    m_990.write('}')
    if(i != 4):
        m_990.write('},')
    else:
        m_990.write('}')

m_990.write('],')
m_990.write('"buttons": [{"label": "장학 공지사항 전체보기", "action": "webLink", "webLinkUrl": "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=990#page1"}]}}],"quickReplies":[{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_990.close()


######################################### 행정공지 #########################################

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=30#page1')
sleep(3)
administrative = driver.page_source
driver.quit() # 웹드라이버 종료

soup = BeautifulSoup(administrative, 'html.parser')

m_30 = open("./data/l_administrative.json", 'w')

m_30.write('{"version": "2.0","template": {"outputs": [{"listCard": {"header": {"title": "대림대학교 행정 공지사항"},"items": [')

for i in range(5):
    m_30.write('{')
    m_30.write('"title": ')
    if(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .mark_num > span').get_text() == "공지"):
        m_30.write('"[공지] ')
    else:
        m_30.write('"')
    m_30.write('{}",'.format(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a').get_text()))
    m_30.write('"description": "{}",'.format((soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtInfo > .date').get_text())).replace('"', '\"'))
    m_30.write('"link": {')
    m_30.write('"web": "{}"'.format("https://www.daelim.ac.kr" + ((((str(soup.select_one('#tbody > li:nth-child(' + str(i + 1) + ') > .txtL > a')).split())[6])[6:])[:-1]).replace("amp;", "")))
    m_30.write('}')
    if(i != 4):
        m_30.write('},')
    else:
        m_30.write('}')

m_30.write('],')
m_30.write('"buttons": [{"label": "행정 공지사항 전체보기", "action": "webLink", "webLinkUrl": "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=30#page1"}]}}],"quickReplies":[{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_30.close()

