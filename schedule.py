import json
from datetime import date, datetime
import os.path

import requests

from private_variables import BLOCK_ID_SCHEDULE, PATH_SCHEDULE

today = date.today()

schedule_data_url = f"https://www.daelim.ac.kr/ajaxf/FrScheduleSvc/ScheduleData.do?SCH_YEAR={today.year - 1 if today.month < 3 else today.year}&SCH_DEPT_CD=2"
schedule_data = requests.get(schedule_data_url).json()["data"]

schedule_list_data_url = f"https://www.daelim.ac.kr/ajaxf/FrScheduleSvc/ScheduleListData.do?SCH_YEAR={today.year - 1 if today.month < 3 else today.year}&SCH_DEPT_CD=2"
schedule_list_data = requests.get(schedule_list_data_url).json()["data"]

unique_subject = []
uniquified_schedule_list_data = []

# SUBJECT 단일화

for sd in schedule_data:
    if sd.get("SUBJECT") is not None:
        unique_subject.append(sd["SUBJECT"])

for sld in schedule_list_data:
    if sld.get("SUBJECT") is not None:
        if sld["SUBJECT"] not in unique_subject:
            uniquified_schedule_list_data.append(sld)


def output(msg):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": msg.rstrip('\n')
                    }
                }
            ],
            "quickReplies": [
                {
                    "action": "block",
                    "messageText": "📃 전체 학사일정 보기",
                    "label": "📃 전체 학사일정 보기",
                    "blockId": BLOCK_ID_SCHEDULE
                }
            ]
        }
    }


def legend(bul):
    if bul == "R0201":
        return "학사"
    elif bul == "R0202":
        return "수업"
    elif bul == "R0203":
        return "행정"
    elif bul == "R0204":
        return "기타"
    elif bul == "R0205":
        return "휴일"
    else:
        return "기타"


def convert_from_ymd(ymd):
    return datetime.strptime(ymd, '%Y%m%d').strftime('%Y.%m.%d')


stack_subject = []
top_message = ""
message = []

top_message += "[대림식 알림]\n"
top_message += "\n"
top_message += f"{today.year}년 {today.month}월 학사일정입니다.\n"
top_message += "\n"

for i in range(len(schedule_data)):
    if schedule_data[i].get("SUBJECT") is not None:
        if i < len(schedule_data) - 1:
            if schedule_data[i + 1].get("SUBJECT") is not None and (
                    schedule_data[i]["SUBJECT"] == schedule_data[i + 1]["SUBJECT"]):
                stack_subject.append(schedule_data[i])
            else:
                if len(stack_subject) != 0:
                    if schedule_data[i]["SUBJECT"] == stack_subject[len(stack_subject) - 1]["SUBJECT"]:
                        stack_subject.append(schedule_data[i])
                        if (stack_subject[0]["M"] == today.month or stack_subject[len(stack_subject) - 1][
                            "M"] == today.month):
                            message.append(
                                f"[{convert_from_ymd(stack_subject[0]['FROM_YMD'])}~{convert_from_ymd(stack_subject[len(stack_subject) - 1]['FROM_YMD'])}]\n{legend(stack_subject[0]['SCH_TYPE'])} | {stack_subject[0]['SUBJECT']}\n\n")
                            stack_subject = []
                        else:
                            stack_subject = []
                else:
                    if schedule_data[i]["M"] == today.month:
                        message.append(
                            f"[{convert_from_ymd(schedule_data[i]['FROM_YMD'])}]\n{legend(schedule_data[i]['SCH_TYPE'])} | {schedule_data[i]['SUBJECT']}\n\n")
        else:
            if len(stack_subject) != 0:
                if schedule_data[i - 1].get("SUBJECT") is not None and (
                        schedule_data[i]["SUBJECT"] == schedule_data[i - 1]["SUBJECT"]):
                    stack_subject.append(schedule_data[i])
                    if (stack_subject[0]["M"] == today.month or stack_subject[len(stack_subject) - 1][
                        "M"] == today.month):
                        message.append(
                            f"[{convert_from_ymd(stack_subject[0]['FROM_YMD'])}~{convert_from_ymd(stack_subject[len(stack_subject) - 1]['FROM_YMD'])}]\n{legend(stack_subject[0]['SCH_TYPE'])} | {stack_subject[0]['SUBJECT']}\n\n")
                        stack_subject = []
                    else:
                        stack_subject = []
            else:
                if schedule_data[i]["M"] == today.month:
                    message.append(
                        f"[{convert_from_ymd(schedule_data[i]['FROM_YMD'])}]\n{legend(schedule_data[i]['SCH_TYPE'])} | {schedule_data[i]['SUBJECT']}\n\n")

for item in uniquified_schedule_list_data:
    if int(item["START_M"]) <= today.month <= int(item["END_M"]) and int(item["START_Y"]) <= today.year <= int(
            item["END_Y"]):
        if item["START_D"] == item["END_D"] and item["START_M"] == item["END_M"] and item["START_Y"] == item["END_Y"]:
            message.append(
                f"[{item['END_Y']}.{item['END_M']}.{item['END_D']}]\n{legend(item['SCH_TYPE'])} | {item['SUBJECT']}\n\n")
        else:
            message.append(
                f"[{item['START_Y']}.{item['START_M']}.{item['START_D']}~{item['END_Y']}.{item['END_M']}.{item['END_D']}]\n{legend(item['SCH_TYPE'])} | {item['SUBJECT']}\n\n")

if len(message) == 0:
    message.append("일정이 없습니다.\n\n")

if not os.path.isdir(PATH_SCHEDULE):
    os.makedirs(PATH_SCHEDULE)

with open(f"{PATH_SCHEDULE}/m_schedule.json", 'w') as outfile:
    json.dump(output(top_message + ''.join(sorted(message, key=lambda x: x[:12]))), outfile, ensure_ascii=False)
