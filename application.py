import json
import os.path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

from private_variables import PATH_CAFETERIA, PATH_ANNOUNCEMENT, PATH_SCHEDULE, \
    PATH_SCHOOLBUS

error_message = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "[대림식 알림]\n\n알 수 없는 오류가 발생하였습니다."
                }
            }
        ]
    }
}

app = FastAPI()


@app.get("/")
def main():
    return HTMLResponse(content="<h2>대림식 연결 성공</h2>", status_code=200)


def load_json_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    return error_message


@app.exception_handler(404)
async def error(request: Request, exc: HTTPException):
    return error_message


# 식당메뉴
@app.post("/cafeteria/{where}/{day}")
def student(where: str, day: str):
    path = f"{PATH_CAFETERIA}/{where}/m_{where}_{day}.json"
    return load_json_file(path)


# 공지사항
@app.post("/announcement/{category}")
def announcement(category: str):
    path = f"{PATH_ANNOUNCEMENT}/l_{category}.json"
    return load_json_file(path)


# 학사일정
@app.post("/schedule")
def schedule():
    path = f"{PATH_SCHEDULE}/m_schedule.json"
    return load_json_file(path)


# 셔틀버스
@app.post("/schoolbus/{route}")
def schoolbus(route: str):
    path = f"{PATH_SCHOOLBUS}/m_{route}.json"
    return load_json_file(path)
