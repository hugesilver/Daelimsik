from bs4 import BeautifulSoup
from datetime import date

f1470 = open("./data/html_1470.txt", 'r')
html = f1470.read()
f1470.close()

soup = BeautifulSoup(html, 'html.parser')
no_data = soup.find_all('tr', attrs={'class':'no_data','style':''})
weekdate = soup.select_one('#current_date').get_text()
today = date.today()
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_number = today.weekday() # 월요일 0 일요일 6

corner1 = 'tbody > tr:nth-child(1) > td:nth-child({})'.format(weekday_number + 2)
corner2 = 'tbody > tr:nth-child(2) > td:nth-child({})'.format(weekday_number + 2)
corner3 = 'tbody > tr:nth-child(3) > td:nth-child({})'.format(weekday_number + 2)
corner4 = 'tbody > tr:nth-child(4) > td:nth-child({})'.format(weekday_number + 2)
corner5 = 'tbody > tr:nth-child(5) > td:nth-child({})'.format(weekday_number + 2)
corner6 = 'tbody > tr:nth-child(6) > td:nth-child({})'.format(weekday_number + 2)
daelimcook = 'tbody > tr:nth-child(7) > td:nth-child({})'.format(weekday_number + 2)
dellibus = 'tbody > tr:nth-child(8) > td:nth-child({})'.format(weekday_number + 2)
plus = 'tbody > tr:nth-child(9) > td:nth-child({})'.format(weekday_number + 2)

m_1470 = open("./data/m_student.json", 'w')

m_1470.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_1470.write("[대림식 알림]\\n")
m_1470.write("\\n")
m_1470.write("{} 주간 식단 중:\\n".format(weekdate))
m_1470.write("{}년 {}월 {}일 {} 학생식당 메뉴입니다.\\n".format(today.year, today.month, today.day, days[weekday_number]))
m_1470.write("\\n")

if(no_data != [] or weekday_number >= 5):
    m_1470.write("메뉴가 없습니다.\\n")
    m_1470.write("\\n")
else:
    # [Corner1]
    if (soup.select_one(corner1).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(1) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(corner1).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Corner2]
    if (soup.select_one(corner2).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(2) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(corner2).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Corner3]
    if (soup.select_one(corner3).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(3) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(corner3).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Corner4]
    if (soup.select_one(corner4).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(4) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(corner4).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Corner5]
    if (soup.select_one(corner5).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(5) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(corner5).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Corner6]
    if (soup.select_one(corner6).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(6) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(corner6).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Daelim Cook]
    if (soup.select_one(daelimcook).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(7) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(daelimcook).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [Dellibus]
    if (soup.select_one(dellibus).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(8) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(dellibus).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

    # [PLUS+]
    if (soup.select_one(plus).get_text()) != "":
        m_1470.write("[{}]\\n".format(soup.select_one('tbody > tr:nth-child(9) > th:nth-child(1)').get_text()))
        m_1470.write((soup.select_one(plus).get_text()).replace('\n', '\\n') + "\\n")
        m_1470.write("\\n")

m_1470.write("담당부서: 사무운영팀 | 031-467-4752")
m_1470.write('"}}]}}')
m_1470.close()