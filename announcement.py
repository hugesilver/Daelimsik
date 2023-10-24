import json
import os

import requests

from private_variables import PATH_ANNOUNCEMENT


def output(title, items, buttonlabel, weblink):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": title
                        },
                        "items": items,
                        "buttons": [
                            {
                                "label": buttonlabel,
                                "action": "webLink",
                                "webLinkUrl": weblink
                            }
                        ]
                    }
                }
            ]
        }
    }


def listitem(title, desc, link):
    return {
        "title": title,
        "description": desc,
        "link": {
            "web": link
        }
    }


if not os.path.isdir(PATH_ANNOUNCEMENT):
    os.makedirs(PATH_ANNOUNCEMENT)

######################################### 행정공지 #########################################

url30 = "https://www.daelim.ac.kr/ajaxf/FrBoardSvc/BBSViewList.do?pageNo=1&MENU_ID=30&SITE_NO=2&BOARD_SEQ=1"
data30 = requests.get(url30).json()["data"]["list"]
listitem30 = []

for i in range(5):
    listitem30.append(listitem(
        f"{'[공지] ' if data30[i]['TOP_YN'] == 'Y' else ''}{data30[i]['SUBJECT']}",
        data30[i]["WRITE_DATE"],
        f"https://www.daelim.ac.kr/cms/FrBoardCon/BoardView.do?MENU_ID=30&SITE_NO=2&BOARD_SEQ=1&BBS_SEQ={data30[i]['BBS_SEQ']}"
    ))

with open(f"{PATH_ANNOUNCEMENT}/l_administrative.json", 'w') as outfile:
    json.dump(output("대림대학교 행정 공지사항", listitem30, "행정 공지사항 전체보기",
                     "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=30#page1"), outfile, ensure_ascii=False)

######################################### 학사공지 #########################################

url900 = "https://www.daelim.ac.kr/ajaxf/FrBoardSvc/BBSViewList.do?pageNo=1&MENU_ID=900&SITE_NO=2&BOARD_SEQ=8"
data900 = requests.get(url900).json()["data"]["list"]
listitem900 = []

for i in range(5):
    listitem900.append(listitem(
        f"{'[공지] ' if data900[i]['TOP_YN'] == 'Y' else ''}{data900[i]['SUBJECT']}",
        data900[i]["WRITE_DATE"],
        f"https://www.daelim.ac.kr/cms/FrBoardCon/BoardView.do?MENU_ID=900&SITE_NO=2&BOARD_SEQ=8&BBS_SEQ={data900[i]['BBS_SEQ']}"
    ))

with open(f"{PATH_ANNOUNCEMENT}/l_bachelor.json", 'w') as outfile:
    json.dump(output("대림대학교 학사 공지사항", listitem900, "학사 공지사항 전체보기",
                     "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=900#page1"), outfile, ensure_ascii=False)

######################################### 장학공지 #########################################

url990 = "https://www.daelim.ac.kr/ajaxf/FrBoardSvc/BBSViewList.do?pageNo=1&MENU_ID=990&SITE_NO=2&BOARD_SEQ=9"
data990 = requests.get(url990).json()["data"]["list"]
listitem990 = []

for i in range(5):
    listitem990.append(listitem(
        f"{'[공지] ' if data990[i]['TOP_YN'] == 'Y' else ''}{data990[i]['SUBJECT']}",
        data990[i]["WRITE_DATE"],
        f"https://www.daelim.ac.kr/cms/FrBoardCon/BoardView.do?MENU_ID=990&SITE_NO=2&BOARD_SEQ=9&BBS_SEQ={data990[i]['BBS_SEQ']}"
    ))

with open(f"{PATH_ANNOUNCEMENT}/l_scholarship.json", 'w') as outfile:
    json.dump(output("대림대학교 장학 공지사항", listitem990, "장학 공지사항 전체보기",
                     "https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=990#page1"), outfile, ensure_ascii=False)
