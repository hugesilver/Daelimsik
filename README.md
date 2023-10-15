# 🟡 카카오톡 학식봇 대림식
<img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/Daelimsik_logo_Authority.jpg?raw=true" width="300px" height="300px"><br>

## 1️⃣ 소개
2022년 여름방학에 개인적으로 진행한 첫 Python 프로젝트입니다.<br>
방학 기간 동안 나태해지지 말고 전공 공부를 하자는 생각과 유용한 경험을 쌓기 위해,<br>
"카카오톡 대림대학교 학식봇 대림식"을 기획하게 되었습니다.<br>

\- 대림대학교 컴퓨터정보학부 19학번 학부생

## 2️⃣ 기술
* 1️⃣ 데이터 가공
    <br><br>
    <table>
    <tr>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_python.png?raw=true" width="100px" height="100px">
    </td>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_bs.jpeg?raw=true" width="100px" height="100px">
    </td>
    </tr>
    <tr>
    <td align="center">
    <b>Python</b>
    </td>
    <td align="center">
    <b>BeautifulSoup</b>
    </td>
    </tr>
    </table>
    <b>대림식</b>은 대림대학교 웹사이트 내 필요한 정보를<br>
    <u>교내 API</u> 요청 혹은 <u>BeautifulSoup</u>으로 통해<br>
    데이터를 추출하여 카카오톡 스킬 형식에 맞게 JSON 파일로 변환합니다.
    <br><br>
* 2️⃣ 서버
    <br><br>
    <table>
    <tr>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_ubuntu.png?raw=true" width="100px" height="100px">
    </td>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_fastapi.png?raw=true" width="100px" height="100px">
    </td>
    </tr>
    <tr>
    <td align="center">
    <b>Ubuntu</b>
    </td>
    <td align="center">
    <b>FastAPI</b>
    </td>
    </tr>
    </table>
    <b>대림식</b>은 <u>Ubuntu</u> 운영체제를 사용하여 작동되고 있습니다.<br>
    일정 시간마다 Python 파일을 실행 명령을 하여 생성된 JSON 파일을 가지고<br>
    <u>FastAPI</u>로 API 서버를 열어 카카오톡 서버와 통신합니다.<br>
    <br>

## 3️⃣ 카카오톡 챗봇
<img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/image_kakao_business.png?raw=true" width="700px"><br>
<br>
기존 비즈니스 채널의 챗봇 기능을 활성화하기 위해<br>
카카오비즈니스의 카카오 i 오픈빌더 서비스를 이용하여 챗봇 기능 사용 권한을 얻은 후,<br>
챗봇 기능을 사용하여 24시간 동안 필요한 정보를 제공할 수 있는 프로젝트를 만들었습니다.<br>
더욱 노력하는 <b>대림식</b>이 되겠습니다. 감사합니다.<br>
<br>
[[카카오 챗봇 가이드]](https://chatbot.kakao.com/docs/getting-started-overview)<br>