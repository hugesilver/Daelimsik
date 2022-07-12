from bs4 import BeautifulSoup
from datetime import date

f1480 = open("./data/html_1480.txt", 'r')
html = f1480.read()
f1480.close()

soup = BeautifulSoup(html, 'html.parser')
no_data = soup.find_all('tr', attrs={'class':'no_data','style':''})
today = date.today()
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_number = today.weekday() # 월요일 0 일요일 6
# weekdate = soup.select_one('#current_date').get_text()

lunch = 'tbody > tr:nth-child(1) > td:nth-child({})'.format(weekday_number + 2)
dinner = 'tbody > tr:nth-child(2) > td:nth-child({})'.format(weekday_number + 2)
notes = 'tbody > tr:nth-child(10) > td'

m_1480 = open("./data/m_profstaff.json", 'w')

m_1480.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_1480.write("[대림식 알림]\\n")
m_1480.write("\\n")
m_1480.write("{}년 {}월 {}일 {}\\n".format(today.year, today.month, today.day, days[weekday_number]))
m_1480.write("교직원식당 메뉴입니다.\\n")
m_1480.write("\\n")

if(no_data != [] or weekday_number >= 5):
    m_1480.write("메뉴가 없습니다.\\n")
    m_1480.write("\\n")
else:
    # [주간]
    if (soup.select_one(lunch).get_text()) != "":
        m_1480.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(1) > th:nth-child(1)').get_text()))
        m_1480.write((soup.select_one(lunch).get_text()).replace('\n', '\\n'))
        m_1480.write("\\n")

    # [석식]
    if (soup.select_one(dinner).get_text()) != "":
        m_1480.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(2) > th:nth-child(1)').get_text()))
        m_1480.write((soup.select_one(dinner).get_text()).replace('\n', '\\n'))
        m_1480.write("\\n")

    # [비고]
    if (soup.select_one(notes).get_text()) != "":
        m_1480.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(10) > th:nth-child(1)').get_text()))
        m_1480.write((soup.select_one(notes).get_text()).replace('\n', '\\n') + "\\n")
        m_1480.write("\\n")

m_1480.write("담당부서: 사무운영팀(031-467-4752)")
m_1480.write('"}}]}}')
m_1480.close()