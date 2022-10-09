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
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_number = today.weekday() # 월요일 0 일요일 6

######################################### 학생 식당 #########################################

m_1470 = open("./data/m_student.json", 'w')

m_1470.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_1470.write("[대림식 알림]\\n")
m_1470.write("\\n")
m_1470.write("{}년 {}월 {}일 {}\\n".format(today.year, today.month, today.day, days[weekday_number]))
m_1470.write("학생식당 메뉴입니다.\\n")
m_1470.write("\\n")

if(weekday_number >= 5):
    m_1470.write("메뉴가 없습니다.\\n")
    m_1470.write("\\n")
else:
    driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
    driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=1470')
    sleep(3)
    student = driver.page_source
    driver.quit() # 웹드라이버 종료

    soup = BeautifulSoup(student, 'html.parser')
    no_data = soup.find_all('tr', attrs={'class':'no_data','style':''})

    corner1 = 'tbody > tr:nth-child(1) > td:nth-child({})'.format(weekday_number + 2)
    corner2 = 'tbody > tr:nth-child(2) > td:nth-child({})'.format(weekday_number + 2)
    corner3 = 'tbody > tr:nth-child(3) > td:nth-child({})'.format(weekday_number + 2)
    corner4 = 'tbody > tr:nth-child(4) > td:nth-child({})'.format(weekday_number + 2)
    corner5 = 'tbody > tr:nth-child(5) > td:nth-child({})'.format(weekday_number + 2)
    corner6 = 'tbody > tr:nth-child(6) > td:nth-child({})'.format(weekday_number + 2)
    daelimcook = 'tbody > tr:nth-child(7) > td:nth-child({})'.format(weekday_number + 2)
    dellibus = 'tbody > tr:nth-child(8) > td:nth-child({})'.format(weekday_number + 2)
    plus = 'tbody > tr:nth-child(9) > td:nth-child({})'.format(weekday_number + 2)

    if(no_data != []):
        m_1470.write("메뉴가 없습니다.\\n")
        m_1470.write("\\n")
    else:
        # [Corner1]
        if (soup.select_one(corner1).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(1) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(corner1).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(corner1).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Corner2]
        if (soup.select_one(corner2).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(2) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(corner2).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(corner2).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Corner3]
        if (soup.select_one(corner3).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(3) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(corner3).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(corner3).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Corner4]
        if (soup.select_one(corner4).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(4) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(corner4).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(corner4).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Corner5]
        if (soup.select_one(corner5).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(5) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(corner5).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(corner5).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Corner6]
        if (soup.select_one(corner6).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(6) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(corner6).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(corner6).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Daelim Cook]
        if (soup.select_one(daelimcook).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(7) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(daelimcook).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(daelimcook).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [Dellibus]
        if (soup.select_one(dellibus).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(8) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(dellibus).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(dellibus).get_text())[-1] != "\n"):
                m_1470.write("\\n")

        # [PLUS+]
        if (soup.select_one(plus).get_text()) != "":
            m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(9) > th:nth-child(1)').get_text()))
            m_1470.write((((soup.select_one(plus).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(plus).get_text())[-1] != "\n"):
                m_1470.write("\\n")

m_1470.write("※ 식단 데이터는 매일 오전 9시 30분에 업데이트됩니다.\\n※ 식당 상황에 따라 메뉴가 변경될 수 있습니다.")
m_1470.write('"}}],"quickReplies":[{"action": "block", "messageText": "📃 전체 메뉴보기", "label": "📃 전체 메뉴보기", "blockId": "63098b155ce7b2313afc191b"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_1470.close()


######################################### 교직원 식당 #########################################

m_1480 = open("./data/m_profstaff.json", 'w')

m_1480.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_1480.write("[대림식 알림]\\n")
m_1480.write("\\n")
m_1480.write("{}년 {}월 {}일 {}\\n".format(today.year, today.month, today.day, days[weekday_number]))
m_1480.write("교직원식당 메뉴입니다.\\n")
m_1480.write("\\n")

if(weekday_number >= 5):
    m_1480.write("메뉴가 없습니다.\\n")
    m_1480.write("\\n")
else:
    driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
    driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=1480')
    sleep(3)
    profstaff = driver.page_source
    driver.quit() # 웹드라이버 종료

    soup = BeautifulSoup(profstaff, 'html.parser')
    no_data = soup.find_all('tr', attrs={'class':'no_data','style':''})

    lunch = 'tbody > tr:nth-child(1) > td:nth-child({})'.format(weekday_number + 2)
    dinner = 'tbody > tr:nth-child(2) > td:nth-child({})'.format(weekday_number + 2)
    notes = 'tbody > tr:nth-child(10) > td'

    if(no_data != []):
        m_1480.write("메뉴가 없습니다.\\n")
        m_1480.write("\\n")
    else:
        # [주간]
        if (soup.select_one(lunch).get_text()) != "":
            m_1480.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(1) > th:nth-child(1)').get_text()))
            m_1480.write((((soup.select_one(lunch).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if((soup.select_one(lunch).get_text())[-1] != "\n"):
                m_1480.write("\\n")

        # [석식]
        if (soup.select_one(dinner).get_text()) != "":
            m_1480.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(2) > th:nth-child(1)').get_text()))
            m_1480.write((((soup.select_one(dinner).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(dinner).get_text())[-1] != "\n"):
                m_1480.write("\\n")

        # [비고]
        if (soup.select_one(notes).get_text()) != "":
            m_1480.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(10) > th:nth-child(1)').get_text()))
            m_1480.write((((soup.select_one(notes).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ','') + "\\n")
            if ((soup.select_one(notes).get_text())[-1] != "\n"):
                m_1480.write("\\n")

m_1480.write("※ 식단 데이터는 매일 오전 9시 30분에 업데이트됩니다.\\n※ 식당 상황에 따라 메뉴가 변경될 수 있습니다.")
m_1480.write('"}}],"quickReplies":[{"action": "block", "messageText": "📃 전체 메뉴보기", "label": "📃 전체 메뉴보기", "blockId": "63098b155ce7b2313afc191b"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_1480.close()
