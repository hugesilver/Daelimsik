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
weekday_number = today.weekday()  #월요일 0 일요일 6

menu_today = "td:nth-child({})".format(weekday_number + 2)

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

    if(no_data != []):
        m_1470.write("메뉴가 없습니다.\\n")
        m_1470.write("\\n")
    else:
        student_none = 0
        student_table = soup.select_one('.lineTop_tbArea > table > tbody')
        student_table_tr = student_table.select('tr')
        for student_data in student_table_tr:
            try:
                if(student_data.select_one(menu_today).get_text() in ["", " ", "&nbsp;", " "]):
                    student_none = student_none + 1
                    pass
                else:
                    m_1470.write("[{}]\\n".format(student_data.select_one('th').get_text()))
                    if(student_data.select_one(menu_today).get_text()[-1] == "\n"):
                        m_1470.write((((student_data.select_one(menu_today).get_text()).replace('\n', '\\n')).replace(
                            '"', '')).replace(' ', ''))
                        m_1470.write("\\n")
                    else:
                        m_1470.write((((student_data.select_one(menu_today).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ',''))
                        m_1470.write("\\n")
                        m_1470.write("\\n")
            except AttributeError as e:
                pass

        if (student_none >= len(student_table_tr) - 2):
            m_1470.write("메뉴가 없습니다.\\n")
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

    if(no_data != []):
        m_1480.write("메뉴가 없습니다.\\n")
        m_1480.write("\\n")
    else:
        profstaff_none = 0
        profstaff_table = soup.select_one('.lineTop_tbArea > table > tbody')
        profstaff_table_tr = profstaff_table.select('tr')
        for profstaff_data in profstaff_table_tr:
            try:
                if (profstaff_data.select_one(menu_today).get_text() in ["", " ", "&nbsp;", " "]):
                    profstaff_none = profstaff_none + 1
                    pass
                else:
                    if(profstaff_data.select_one(menu_today).get_text()[-1] == "\n"):
                        m_1480.write("[{}]\\n".format(profstaff_data.select_one('th').get_text()))
                        m_1480.write((((profstaff_data.select_one(menu_today).get_text()).replace('\n', '\\n')).replace(
                            '"', '')).replace(' ', ''))
                        m_1480.write("\\n")
                    else:
                        m_1480.write("[{}]\\n".format(profstaff_data.select_one('th').get_text()))
                        m_1480.write((((profstaff_data.select_one(menu_today).get_text()).replace('\n', '\\n')).replace('"', '')).replace(' ', ''))
                        m_1480.write("\\n")
                        m_1480.write("\\n")
            except AttributeError as e:
                pass

        if(weekday_number == 0):
            if(len(profstaff_table_tr) - profstaff_none) == 1:
                m_1480.write("메뉴가 없습니다.\\n")
                m_1480.write("\\n")
        else:
            if(len(profstaff_table_tr) - profstaff_none) == 0:
                m_1480.write("메뉴가 없습니다.\\n")
                m_1480.write("\\n")


m_1480.write("※ 식단 데이터는 매일 오전 9시 30분에 업데이트됩니다.\\n※ 식당 상황에 따라 메뉴가 변경될 수 있습니다.")
m_1480.write('"}}],"quickReplies":[{"action": "block", "messageText": "📃 전체 메뉴보기", "label": "📃 전체 메뉴보기", "blockId": "63098b155ce7b2313afc191b"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_1480.close()
