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


def station_to_school(loc):
    message = ""

    for tr in loc:
        if ((tr.select_one('td:nth-child(1)').get_text()) in ["휴게시간", "", " ", "&nbsp;", " "]):
            pass
        elif (((tr.select_one('td:nth-child(1)').get_text())[1].isdigit() == False) and (
                (tr.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]))):
            pass
        elif (tr.select_one('td:nth-child(1)').get_text())[1].isdigit() == True:
            if (tr.select_one('td:nth-child(1)').get_text() in ["", " ", "&nbsp;", " "]):
                pass
            else:
                message += "- "
                message += tr.select_one('td:nth-child(1)').get_text() + " "
                if (tr.select_one('td:nth-child(3)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                    message += "\n"
                else:
                    message += "(배차간격: {})\n".format(tr.select_one('td:nth-child(3)').get_text())
        elif (tr.select_one('td:nth-child(1)').get_text())[1].isdigit() == False:
            if (tr.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]):
                pass
            else:
                message += "- "
                message += tr.select_one('td:nth-child(2)').get_text() + " "
                if (tr.select_one('td:nth-child(4)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                    message += "\n"
                else:
                    message += "(배차간격: {})\n".format(tr.select_one('td:nth-child(4)').get_text())

    return message


def school_to_station(loc):
    message = ""

    for tr in loc:
        if ((tr.select_one('td:nth-child(1)').get_text()) == "휴게시간") or (
                tr.select_one('td:nth-child(1)[colspan]')):
            pass
        elif (tr.select_one('td:nth-child(1)').get_text() in ["", " ", "&nbsp;", " "]) or (
                (tr.select_one('td:nth-child(1)').get_text())[1].isdigit() == True):
            if (tr.select_one('td:nth-child(2)').get_text() in ["", " ", "&nbsp;", " "]):
                pass
            else:
                message += "- "
                message += tr.select_one('td:nth-child(2)').get_text() + " "
                if (tr.select_one('td:nth-child(3)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                    message += "\n"
                else:
                    message += "(배차간격: {})\n".format(tr.select_one('td:nth-child(3)').get_text())
        elif (tr.select_one('td:nth-child(1)').get_text())[1].isdigit() == False:
            if (tr.select_one('td:nth-child(3)').get_text() in ["", " ", "&nbsp;", " "]):
                pass
            else:
                message += "- "
                message += tr.select_one('td:nth-child(3)').get_text() + " "
                if (tr.select_one('td:nth-child(4)').get_text() in ["해당시간", "", " ", "&nbsp;", " "]):
                    message += "\n"
                else:
                    message += "(배차간격: {})\n".format(tr.select_one('td:nth-child(4)').get_text())

    return message


######################################### 안양역 #########################################

anyang_tr = soup.select_one('.lineTop_tbArea > table > tbody').select('tr')

### 안양역에서 학교 ###

anyang_to_school = ""

anyang_to_school += "[대림식 알림]\n"
anyang_to_school += "\n"
anyang_to_school += "안양역에서 학교로 이동하는 셔틀버스 안내입니다.\n"
anyang_to_school += "\n"

anyang_to_school += station_to_school(anyang_tr)

anyang_to_school += "\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다."

with open("./out/schoolbus/m_anyang_to_school.json", 'w') as outfile:
    json.dump(output(anyang_to_school, [quickreply("🚌 전체 셔틀버스 배차시간", block_id_schoolbus_all),
                                        quickreply("🚏 안양역 정류장", block_id_schoolbus_anyang)]), outfile,
              ensure_ascii=False)

### 학교에서 안양역 ###

school_to_anyang = ""

school_to_anyang += "[대림식 알림]\n"
school_to_anyang += "\n"
school_to_anyang += "학교에서 안양역으로 이동하는 셔틀버스 안내입니다.\n"
school_to_anyang += "\n"

school_to_anyang += school_to_station(anyang_tr)

school_to_anyang += "\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다."

with open("./out/schoolbus/m_school_to_anyang.json", 'w') as outfile:
    json.dump(output(school_to_anyang, [quickreply("🚌 전체 셔틀버스 배차시간", block_id_schoolbus_all),
                                        quickreply("🚏 안양역 정류장", block_id_schoolbus_anyang)]), outfile,
              ensure_ascii=False)

######################################### 범계역 #########################################

beomgye_tr = soup.select_one('.mT30 > table > tbody').select('tr')

### 범계역에서 학교 ###

beomgye_to_school = ""

beomgye_to_school += "[대림식 알림]\n"
beomgye_to_school += "\n"
beomgye_to_school += "범계역에서 학교로 이동하는 셔틀버스 안내입니다.\n"
beomgye_to_school += "\n"

beomgye_to_school += station_to_school(beomgye_tr)

beomgye_to_school += "\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다."

with open("./out/schoolbus/m_beomgye_to_school.json", 'w') as outfile:
    json.dump(output(beomgye_to_school, [quickreply("🚌 전체 셔틀버스 배차시간", block_id_schoolbus_all),
                                         quickreply("🚏 범계역 정류장", block_id_schoolbus_beomgye)]), outfile,
              ensure_ascii=False)

### 학교에서 범계역 ###

school_to_beomgye = ""

school_to_beomgye += "[대림식 알림]\n"
school_to_beomgye += "\n"
school_to_beomgye += "학교에서 범계역으로 이동하는 셔틀버스 안내입니다.\n"
school_to_beomgye += "\n"

school_to_beomgye += school_to_station(beomgye_tr)

school_to_beomgye += "\n※ 교통 혼잡 및 신호대기로 인해 운행시간이 변동될 수 있습니다."

with open("./out/schoolbus/m_school_to_beomgye.json", 'w') as outfile:
    json.dump(output(school_to_beomgye, [quickreply("🚌 전체 셔틀버스 배차시간", block_id_schoolbus_all),
                                         quickreply("🚏 범계역 정류장", block_id_schoolbus_beomgye)]), outfile,
              ensure_ascii=False)


######################################### 정류장 #########################################

def helpoutput(info, alttext):
    if info:
        text = ""
        if info.find('ul').find("li"):
            location = info.find('ul').find("li")
            if location.find("b"):
                location.find("b").decompose()
            if location.find(string=lambda text: isinstance(text, Comment)):
                location.find(string=lambda text: isinstance(text, Comment)).extract()
            text = location.get_text().replace("\n", "").rstrip()
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


anyang_info = soup.select_one('.comewayDiv')
beomgye_info = soup.select_one('.mT70')

with open("./out/schoolbus/m_help_anyang.json", 'w') as outfile:
    json.dump(helpoutput(anyang_info, "안양역 정류장"), outfile, ensure_ascii=False)
with open("./out/schoolbus/m_help_beomgye.json", 'w') as outfile:
    json.dump(helpoutput(beomgye_info, "범계역 정류장"), outfile, ensure_ascii=False)
