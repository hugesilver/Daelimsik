import os.path
from datetime import date, timedelta, datetime

import requests
import json

from private_variables import BLOCK_ID_CAFETERIA, PATH_CAFETERIA

today = date.today()
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_today = today.weekday()  # 월요일 0 일요일 6
file_weekday = ["mon", "tue", "wed", "thu", "fri"]

date_url = "https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroDateInfo.do"

current_week_monday = requests.get(date_url).json()["data"][0]["CURRENT_WEEK_MON_DAY"]
current_week_friday = requests.get(date_url).json()["data"][0]["CURRENT_WEEK_FRI_DAY"]


def output(msg):
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
            "quickReplies": [
                {
                    "action": "block",
                    "messageText": "📆 주간 메뉴보기",
                    "label": "📆 주간 메뉴보기",
                    "blockId": BLOCK_ID_CAFETERIA
                }
            ]
        }
    }


def cafeteria(cafeteria_name, menu, open_time, file_code):
    for i in range(1, 8):  # 1에서 7까지
        day = datetime.strptime(current_week_monday, '%Y.%m.%d') + timedelta(days=(i - 1))

        message = ''
        message += "[대림식 알림]\n"
        message += "\n"
        message += f"{day.year}년 {day.month}월 {day.day}일 {days[i - 1]}\n{cafeteria_name} 메뉴입니다.\n"
        message += "\n"

        if menu == "" or i > 5:
            message += "메뉴가 없습니다.\n\n"
        else:
            blank = 0
            for j in range(1, 10):  # 1에서 9까지
                if (menu[f"CCT{i}{j}"] != "") and (menu[f"CCT{i}{j}"] is not None):
                    message += "[{}]\n".format(menu[f"CNM1{j}"])
                    message += "{}".format(menu[f"CCT{i}{j}"]).replace("\r", "").rstrip("\n") + "\n\n"
                else:
                    blank = blank + 1

            if blank >= 9:
                message += "메뉴가 없습니다.\n\n"

        message += "※ 식당 상황에 따라 메뉴가 변경될 수 있습니다.\n"
        message += open_time

        if not os.path.isdir(f"{PATH_CAFETERIA}/{file_code}"):
            os.makedirs(f"{PATH_CAFETERIA}/{file_code}")

        if i < 6:
            with open(f"{PATH_CAFETERIA}/{file_code}/m_{file_code}_{file_weekday[i - 1]}.json", 'w') as outfile:
                json.dump(output(message), outfile, ensure_ascii=False)
        if (i - 1) == weekday_today:
            with open(f"{PATH_CAFETERIA}/{file_code}/m_{file_code}_today.json", 'w') as outfile:
                json.dump(output(message), outfile, ensure_ascii=False)


# 학생식당
student_url = f"https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do?pageNo=1&MENU_ID=1470&BISTRO_SEQ=1&START_DAY={current_week_monday}&END_DAY={current_week_friday}"
student_menu = requests.get(student_url).json()["data"]

cafeteria(
    "학생식당",
    student_menu,
    "※ 운영시간: 11:30 ~ 14:00 (석식, 방학 미운영)",
    "student")

# 교직원식당
profstaff_url = f"https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do?pageNo=1&MENU_ID=1480&BISTRO_SEQ=2&START_DAY={current_week_monday}&END_DAY={current_week_friday}"
profstaff_menu = requests.get(profstaff_url).json()["data"]

cafeteria(
    "교직원식당",
    profstaff_menu,
    "※ 학기 운영시간: 11:40 ~ 14:00 / 17:00 ~ 19:00\n※ 방학 운영시간: 11:40 ~ 13:30 / 석식 미운영",
    "profstaff")
