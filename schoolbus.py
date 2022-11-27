from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=460')
sleep(3)
bus = driver.page_source
driver.quit() # 웹드라이버 종료

soup = BeautifulSoup(bus, 'html.parser')

# 안양역

anyang = soup.select_one('.lineTop_tbArea > table > tbody')
anyang_tr = anyang.select('tr')

# 안양역에서 학교

m_460_anyang_to_school = open("./out/schoolbus/m_anyang_to_school.json", 'w')
m_460_anyang_to_school.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_460_anyang_to_school.write("[대림식 알림]\\n")
m_460_anyang_to_school.write("\\n")
m_460_anyang_to_school.write("안양역에서 학교로 이동하는 셔틀버스 안내입니다.\\n")
m_460_anyang_to_school.write("\\n")

for anyang_to_school in anyang_tr:
    if ((anyang_to_school.select_one('td:nth-child(1)').get_text()) in ["휴게시간", "", " ", "&nbsp;", " "]):
        pass
    elif (((anyang_to_school.select_one('td:nth-child(1)').get_text())[1].isdigit() == False) and ((anyang_to_school.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]))):
        pass
    elif (anyang_to_school.select_one('td:nth-child(1)').get_text())[1].isdigit() == True:
        if (anyang_to_school.select_one('td:nth-child(1)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_anyang_to_school.write("- ")
            m_460_anyang_to_school.write(anyang_to_school.select_one('td:nth-child(1)').get_text() + " ")
            if (anyang_to_school.select_one('td:nth-child(3)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_anyang_to_school.write("\\n")
            else:
                m_460_anyang_to_school.write("(배차간격: {})\\n".format(anyang_to_school.select_one('td:nth-child(3)').get_text()))
    elif (anyang_to_school.select_one('td:nth-child(1)').get_text())[1].isdigit() == False:
        if (anyang_to_school.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_anyang_to_school.write("- ")
            m_460_anyang_to_school.write(anyang_to_school.select_one('td:nth-child(2)').get_text() + " ")
            if (anyang_to_school.select_one('td:nth-child(4)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_anyang_to_school.write("\\n")
            else:
                m_460_anyang_to_school.write("(배차간격: {})\\n".format(anyang_to_school.select_one('td:nth-child(4)').get_text()))

m_460_anyang_to_school.write("\\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다.")
m_460_anyang_to_school.write('"}}],"quickReplies":[{"action": "block", "messageText": "🚌 전체 셔틀버스 배차시간", "label": "🚌 전체 셔틀버스 배차시간", "blockId": "633e69ddca1fd2777db9a2a8"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_460_anyang_to_school.close()

# 학교에서 안양역

m_460_school_to_anyang = open("./out/schoolbus/m_school_to_anyang.json", 'w')
m_460_school_to_anyang.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_460_school_to_anyang.write("[대림식 알림]\\n")
m_460_school_to_anyang.write("\\n")
m_460_school_to_anyang.write("학교에서 안양역으로 이동하는 셔틀버스 안내입니다.\\n")
m_460_school_to_anyang.write("\\n")

for school_to_anyang in anyang_tr:
    if ((school_to_anyang.select_one('td:nth-child(1)').get_text()) == "휴게시간"):
        pass
    elif (school_to_anyang.select_one('td:nth-child(1)').get_text() in ["", " ", "&nbsp;", " "]) or ((school_to_anyang.select_one('td:nth-child(1)').get_text())[1].isdigit() == True):
        if(school_to_anyang.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_school_to_anyang.write("- ")
            m_460_school_to_anyang.write(school_to_anyang.select_one('td:nth-child(2)').get_text() + " ")
            if (school_to_anyang.select_one('td:nth-child(3)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_school_to_anyang.write("\\n")
            else:
                m_460_school_to_anyang.write("(배차간격: {})\\n".format(school_to_anyang.select_one('td:nth-child(3)').get_text()))
    elif (school_to_anyang.select_one('td:nth-child(1)').get_text())[1].isdigit() == False:
        if(school_to_anyang.select_one('td:nth-child(3)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_school_to_anyang.write("- ")
            m_460_school_to_anyang.write(school_to_anyang.select_one('td:nth-child(3)').get_text() + " ")
            if (school_to_anyang.select_one('td:nth-child(4)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_school_to_anyang.write("\\n")
            else:
                m_460_school_to_anyang.write("(배차간격: {})\\n".format(school_to_anyang.select_one('td:nth-child(4)').get_text()))

m_460_school_to_anyang.write("\\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다.")
m_460_school_to_anyang.write('"}}],"quickReplies":[{"action": "block", "messageText": "🚌 전체 셔틀버스 배차시간", "label": "🚌 전체 셔틀버스 배차시간", "blockId": "633e69ddca1fd2777db9a2a8"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_460_school_to_anyang.close()

# 범계역

beomgye = soup.select_one('.mT30 > table > tbody')
beomgye_tr = beomgye.select('tr')

# 범계역에서 학교

m_460_beomgye_to_school = open("./out/schoolbus/m_beomgye_to_school.json", 'w')
m_460_beomgye_to_school.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_460_beomgye_to_school.write("[대림식 알림]\\n")
m_460_beomgye_to_school.write("\\n")
m_460_beomgye_to_school.write("범계역에서 학교로 이동하는 셔틀버스 안내입니다.\\n")
m_460_beomgye_to_school.write("\\n")

for beomgye_to_school in beomgye_tr:
    if ((beomgye_to_school.select_one('td:nth-child(1)').get_text()) in ["휴게시간", "", " ", "&nbsp;", " "]):
        pass
    elif (((beomgye_to_school.select_one('td:nth-child(1)').get_text())[1].isdigit() == False) and (((beomgye_to_school.select_one('td:nth-child(2)').get_text()) in ["", " ", "&nbsp;", " "]))):
        pass
    elif (beomgye_to_school.select_one('td:nth-child(1)').get_text())[1].isdigit() == True:
        if(beomgye_to_school.select_one('td:nth-child(1)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_beomgye_to_school.write("- ")
            m_460_beomgye_to_school.write(beomgye_to_school.select_one('td:nth-child(1)').get_text() + " ")
            if (beomgye_to_school.select_one('td:nth-child(3)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_beomgye_to_school.write("\\n")
            else:
                m_460_beomgye_to_school.write("(배차간격: {})\\n".format(beomgye_to_school.select_one('td:nth-child(3)').get_text()))
    elif (beomgye_to_school.select_one('td:nth-child(1)').get_text())[1].isdigit() == False:
        if (beomgye_to_school.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_beomgye_to_school.write("- ")
            m_460_beomgye_to_school.write(beomgye_to_school.select_one('td:nth-child(2)').get_text() + " ")
            if (beomgye_to_school.select_one('td:nth-child(4)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_beomgye_to_school.write("\\n")
            else:
                m_460_beomgye_to_school.write("(배차간격: {})\\n".format(beomgye_to_school.select_one('td:nth-child(4)').get_text()))

m_460_beomgye_to_school.write("\\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다.")
m_460_beomgye_to_school.write('"}}],"quickReplies":[{"action": "block", "messageText": "🚌 전체 셔틀버스 배차시간", "label": "🚌 전체 셔틀버스 배차시간", "blockId": "633e69ddca1fd2777db9a2a8"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_460_beomgye_to_school.close()

# 학교에서 범계역

m_460_school_to_beomgye = open("./out/schoolbus/m_school_to_beomgye.json", 'w')
m_460_school_to_beomgye.write('{"version": "2.0","template": {"outputs": [{"simpleText": {"text": "')
m_460_school_to_beomgye.write("[대림식 알림]\\n")
m_460_school_to_beomgye.write("\\n")
m_460_school_to_beomgye.write("학교에서 범계역으로 이동하는 셔틀버스 안내입니다.\\n")
m_460_school_to_beomgye.write("\\n")

for school_to_beomgye in beomgye_tr:
    if ((school_to_beomgye.select_one('td:nth-child(1)').get_text()) == "휴게시간"):
        pass
    elif (school_to_beomgye.select_one('td:nth-child(1)').get_text() in ["", " ", "&nbsp;", " "]) or ((school_to_beomgye.select_one('td:nth-child(1)').get_text())[1].isdigit() == True):
        if(school_to_beomgye.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_school_to_beomgye.write("- ")
            m_460_school_to_beomgye.write(school_to_beomgye.select_one('td:nth-child(2)').get_text() + " ")
            if (school_to_beomgye.select_one('td:nth-child(3)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_school_to_beomgye.write("\\n")
            else:
                m_460_school_to_beomgye.write("(배차간격: {})\\n".format(school_to_beomgye.select_one('td:nth-child(3)').get_text()))
    elif (school_to_beomgye.select_one('td:nth-child(1)').get_text())[1].isdigit() == False:
        if (school_to_beomgye.select_one('td:nth-child(3)').get_text() in ["", " ", "&nbsp;", " "]):
            pass
        else:
            m_460_school_to_beomgye.write("- ")
            m_460_school_to_beomgye.write(school_to_beomgye.select_one('td:nth-child(3)').get_text() + " ")
            if (school_to_beomgye.select_one('td:nth-child(4)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                m_460_school_to_beomgye.write("\\n")
            else:
                m_460_school_to_beomgye.write("(배차간격: {})\\n".format(school_to_beomgye.select_one('td:nth-child(4)').get_text()))

m_460_school_to_beomgye.write("\\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다.")
m_460_school_to_beomgye.write('"}}],"quickReplies":[{"action": "block", "messageText": "🚌 전체 셔틀버스 배차시간", "label": "🚌 전체 셔틀버스 배차시간", "blockId": "633e69ddca1fd2777db9a2a8"},{"action": "block", "messageText": "☕️ 커피 후원하기", "label": "☕️ 커피 후원하기", "blockId": "633e658052a78f5479d6acea"}]}}')
m_460_school_to_beomgye.close()