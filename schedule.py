import json
from datetime import date, datetime
import os.path

import requests

from private_variables import BLOCK_ID_SCHEDULE, PATH_SCHEDULE

today = date.today()

scheduleData_url = f"https://www.daelim.ac.kr/ajaxf/FrScheduleSvc/ScheduleData.do?SCH_YEAR={today.year - 1 if today.month < 3 else today.year}&SCH_DEPT_CD=2"
scheduleData = requests.get(scheduleData_url).json()["data"]

scheduleListData_url = f"https://www.daelim.ac.kr/ajaxf/FrScheduleSvc/ScheduleListData.do?SCH_YEAR={today.year - 1 if today.month < 3 else today.year}&SCH_DEPT_CD=2"
scheduleListData = requests.get(scheduleListData_url).json()["data"]

uniqueSubject = []
uniquifiedScheduleListData = []

# SUBJECT 단일화

for sd in scheduleData:
    if sd.get("SUBJECT") is not None:
        uniqueSubject.append(sd["SUBJECT"])

for sld in scheduleListData:
    if sld.get("SUBJECT") is not None:
        if sld["SUBJECT"] not in uniqueSubject:
            uniquifiedScheduleListData.append(sld)


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


stackSubject = []
topMessage = ""
message = []

topMessage += "[대림식 알림]\n"
topMessage += "\n"
topMessage += f"{today.year}년 {today.month}월 학사일정입니다.\n"
topMessage += "\n"

for i in range(len(scheduleData)):
    if scheduleData[i].get("SUBJECT") is not None:
        if i < len(scheduleData) - 1:
            if scheduleData[i + 1].get("SUBJECT") is not None and (
                    scheduleData[i]["SUBJECT"] == scheduleData[i + 1]["SUBJECT"]):
                stackSubject.append(scheduleData[i])
            else:
                if len(stackSubject) != 0:
                    if scheduleData[i]["SUBJECT"] == stackSubject[len(stackSubject) - 1]["SUBJECT"]:
                        stackSubject.append(scheduleData[i])
                        if (stackSubject[0]["M"] == today.month or stackSubject[len(stackSubject) - 1][
                            "M"] == today.month):
                            message.append(
                                f"[{convert_from_ymd(stackSubject[0]['FROM_YMD'])}~{convert_from_ymd(stackSubject[len(stackSubject) - 1]['FROM_YMD'])}]\n{legend(stackSubject[0]['SCH_TYPE'])} | {stackSubject[0]['SUBJECT']}\n\n")
                            stackSubject = []
                        else:
                            stackSubject = []
                else:
                    if scheduleData[i]["M"] == today.month:
                        message.append(
                            f"[{convert_from_ymd(scheduleData[i]['FROM_YMD'])}]\n{legend(scheduleData[i]['SCH_TYPE'])} | {scheduleData[i]['SUBJECT']}\n\n")
        else:
            if len(stackSubject) != 0:
                if scheduleData[i - 1].get("SUBJECT") is not None and (
                        scheduleData[i]["SUBJECT"] == scheduleData[i - 1]["SUBJECT"]):
                    stackSubject.append(scheduleData[i])
                    if (stackSubject[0]["M"] == today.month or stackSubject[len(stackSubject) - 1]["M"] == today.month):
                        message.append(
                            f"[{convert_from_ymd(stackSubject[0]['FROM_YMD'])}~{convert_from_ymd(stackSubject[len(stackSubject) - 1]['FROM_YMD'])}]\n{legend(stackSubject[0]['SCH_TYPE'])} | {stackSubject[0]['SUBJECT']}\n\n")
                        stackSubject = []
                    else:
                        stackSubject = []
            else:
                if scheduleData[i]["M"] == today.month:
                    message.append(
                        f"[{convert_from_ymd(scheduleData[i]['FROM_YMD'])}]\n{legend(scheduleData[i]['SCH_TYPE'])} | {scheduleData[i]['SUBJECT']}\n\n")

for item in uniquifiedScheduleListData:
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
    json.dump(output(topMessage + ''.join(sorted(message, key=lambda x: x[:12]))), outfile, ensure_ascii=False)
