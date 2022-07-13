from bs4 import BeautifulSoup

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
