from bs4 import BeautifulSoup

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
