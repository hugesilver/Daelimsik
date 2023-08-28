from datetime import date, timedelta, datetime

import requests
import json

today = date.today()
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_today = today.weekday()  # 월요일 0 일요일 6
file_weekday = ["mon", "tue", "wed", "thu", "fri"]

date_url = "https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroDateInfo.do"

current_week_monday = requests.get(date_url).json()["data"][0]["CURRENT_WEEK_MON_DAY"]
current_week_friday = requests.get(date_url).json()["data"][0]["CURRENT_WEEK_FRI_DAY"]

student_url = f"https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do?pageNo=1&MENU_ID=1470&BISTRO_SEQ=1&START_DAY={current_week_monday}&END_DAY={current_week_friday}"
student_menu = requests.get(student_url).json()["data"]

profstaff_url = f"https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do?pageNo=1&MENU_ID=1480&BISTRO_SEQ=2&START_DAY={current_week_monday}&END_DAY={current_week_friday}"
profstaff_menu = requests.get(profstaff_url).json()["data"]

def output(msg):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": ''.join(msg)
                    }
                }
            ],
            "quickReplies": [
                {
                    "action": "block",
                    "messageText": "📆 주간 메뉴보기",
                    "label": "📆 주간 메뉴보기",
                    "blockId": "63838ed48f7dc436c34546a9"
                }
            ]
        }
    }


######################################### 학생 식당 #########################################

for i in range(1, 8):  # 1에서 7까지
    day = datetime.strptime(current_week_monday, '%Y.%m.%d') + timedelta(days=(i - 1))

    student_message = []
    student_message.append("[대림식 알림]\n")
    student_message.append("\n")
    student_message.append(f"{day.year}년 {day.month}월 {day.day}일 {days[i - 1]}\n학생식당 메뉴입니다.\n")
    student_message.append("\n")

    if student_menu == "" or i > 5:
        student_message.append("메뉴가 없습니다.\n\n")
    else:
        blank = 0
        for j in range(1, 10):  # 1에서 9까지
            if (student_menu[f"CCT{i}{j}"] != "") and (student_menu[f"CCT{i}{j}"] is not None):
                student_message.append("[{}]\n".format(student_menu[f"CNM1{j}"]))
                student_message.append("{}".format(student_menu[f"CCT{i}{j}"]).replace("\r", "").rstrip("\n") + "\n\n")
            else:
                blank = blank + 1

        if blank >= 9:
            student_message.append("메뉴가 없습니다.\n\n")

    student_message.append("※ 식단 데이터는 매일 오전 6시에 업데이트됩니다.\n")
    student_message.append("※ 식당 상황에 따라 메뉴가 변경될 수 있습니다.\n")
    student_message.append("※ 운영시간: 11:30 ~ 14:00 (석식, 방학 미운영)")

    if i < 6:
        with open(f"./out/student/m_student_{file_weekday[i - 1]}.json", 'w') as outfile:
            json.dump(output(student_message), outfile, ensure_ascii=False)
    if (i - 1) == weekday_today:
        with open(f"./out/student/m_student_today.json", 'w') as outfile:
            json.dump(output(student_message), outfile, ensure_ascii=False)

######################################### 교직원 식당 #########################################

for i in range(1, 8):  # 1에서 7까지
    day = datetime.strptime(current_week_monday, '%Y.%m.%d') + timedelta(days=(i - 1))

    profstaff_message = []
    profstaff_message.append("[대림식 알림]\n")
    profstaff_message.append("\n")
    profstaff_message.append(f"{day.year}년 {day.month}월 {day.day}일 {days[i - 1]}\n교직원식당 메뉴입니다.\n")
    profstaff_message.append("\n")

    if profstaff_menu == "" or i > 5:
        profstaff_message.append("메뉴가 없습니다.\n\n")
    else:
        blank = 0
        for j in range(1, 10):  # 1에서 9까지
            if (profstaff_menu[f"CCT{i}{j}"] != "") and (profstaff_menu[f"CCT{i}{j}"] is not None):
                profstaff_message.append("[{}]\n".format(profstaff_menu[f"CNM1{j}"]))
                profstaff_message.append("{}".format(profstaff_menu[f"CCT{i}{j}"]).replace("\r", "").rstrip("\n") + "\n\n")
            else:
                blank = blank + 1

        if blank >= 9:
            profstaff_message.append("메뉴가 없습니다.\n\n")

    profstaff_message.append("※ 식단 데이터는 매일 오전 6시에 업데이트됩니다.\n")
    profstaff_message.append("※ 식당 상황에 따라 메뉴가 변경될 수 있습니다.\n")
    profstaff_message.append("※ 학기 운영시간: 11:40 ~ 14:00 / 17:00 ~ 19:00\n")
    profstaff_message.append("※ 방학 운영시간: 11:40 ~ 13:30 / 석식 미운영")

    if i < 6:
        with open(f"./out/profstaff/m_profstaff_{file_weekday[i - 1]}.json", 'w') as outfile:
            json.dump(output(profstaff_message), outfile, ensure_ascii=False)
    if (i - 1) == weekday_today:
        with open(f"./out/profstaff/m_profstaff_today.json", 'w') as outfile:
            json.dump(output(profstaff_message), outfile, ensure_ascii=False)
