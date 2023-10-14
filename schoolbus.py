import json

import requests
from bs4 import BeautifulSoup, Comment

from private_variables import block_id_schoolbus_anyang, block_id_schoolbus_beomgye, block_id_schoolbus_all

bus = requests.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=460')
soup = BeautifulSoup(bus.text, 'html.parser')


def output(msg, quickreplies):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": msg
                    }
                }
            ],
            "quickReplies": quickreplies
        }
    }


def quickreply(label, blockid):
    return {
        "action": "block",
        "messageText": label,
        "label": label,
        "blockId": blockid
    }


def get_table_data(loc, start_from):
    message = ""

    def bus_interval(text):
        if text and not text.isspace() and text != "해당시간":
            return f" (배차간격: {text})"
        else:
            return ''

    for tr in loc:
        td = tr.find_all('td')
        if len(td) == 4:
            if td[start_from + 1].text and not td[start_from + 1].text.isspace():
                message += f"- {td[start_from + 1].text}{bus_interval(td[-1].text)}\n"
        elif len(td) == 3:
            if td[start_from].text and not td[start_from].text.isspace():
                message += f"- {td[start_from].text}{bus_interval(td[-1].text)}\n"

    return message


start_from_station = 0
start_from_school = 1

# 버스 정보

anyang_tr = soup.select_one('.lineTop_tbArea > table > tbody').select('tr')
beomgye_tr = soup.select_one('.mT30 > table > tbody').select('tr')


def make_message(text, station, start_from, filename, busstop_label, busstop_block_id):
    message = ""

    message += "[대림식 알림]\n"
    message += "\n"
    message += f"{text} 이동하는 셔틀버스 안내입니다.\n"
    message += "\n"

    message += get_table_data(station, start_from)

    message += "\n※ 교통 혼잡 및 신호 대기로 인해 운행 시간이 변동될 수 있습니다."

    with open(f"./out/schoolbus/{filename}", 'w') as outfile:
        json.dump(
            output(message,
                   [quickreply("🚌 전체 셔틀버스 배차시간", block_id_schoolbus_all), quickreply(busstop_label, busstop_block_id)]),
            outfile,
            ensure_ascii=False)


# 안양역
make_message("안양역에서 학교로",
             anyang_tr,
             start_from_station,
             "m_anyang_to_school.json",
             "안양역 정류장",
             block_id_schoolbus_anyang)
make_message("학교에서 안양역으로",
             anyang_tr,
             start_from_school,
             "m_school_to_anyang.json",
             "안양역 정류장",
             block_id_schoolbus_anyang)

# 범계역
make_message("범계역에서 학교로",
             beomgye_tr,
             start_from_station,
             "m_beomgye_to_school.json",
             "범계역 정류장",
             block_id_schoolbus_beomgye)
make_message("학교에서 범계역으로",
             beomgye_tr,
             start_from_school,
             "m_school_to_beomgye.json",
             "범계역 정류장",
             block_id_schoolbus_beomgye)


# 정류장 정보

def helpoutput(info, alttext):
    if info:
        text = ""
        if info.find("ul").find("li"):
            location = info.find("ul").find("li")
            if location.find('b'):
                location.find('b').decompose()
            if location.find(string=lambda text: isinstance(text, Comment)):
                location.find(string=lambda text: isinstance(text, Comment)).extract()
            text = location.get_text().replace("\n", '').rstrip()
        return {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": f"https://www.daelim.ac.kr{info.find('img').get('src')}",
                            "altText": alttext
                        }
                    },
                    {
                        "simpleText": {
                            "text": text
                        }
                    }
                ],
            }
        }


anyang_info = soup.select_one(".comewayDiv")
beomgye_info = soup.select_one(".mT70")

with open("./out/schoolbus/m_help_anyang.json", 'w') as outfile:
    json.dump(helpoutput(anyang_info, "안양역 정류장"), outfile, ensure_ascii=False)
with open("./out/schoolbus/m_help_beomgye.json", 'w') as outfile:
    json.dump(helpoutput(beomgye_info, "범계역 정류장"), outfile, ensure_ascii=False)
