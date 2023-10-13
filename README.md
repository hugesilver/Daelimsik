# 🟡 카카오톡 학식봇 대림식
<img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/Daelimsik_logo_Authority.jpg?raw=true" width="300px" height="300px"><br>

## 1️⃣ 소개
2022년 여름방학에 개인적으로 진행한 첫 파이썬 프로젝트입니다.<br>
방학기간 동안 나태해지지 말고 전공공부를 하자는 생각과 유용한 경험을 쌓기 위해,<br>
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
    <b>대림식</b>은 대림대학교 웹사이트 내 식단 페이지와 공지 페이지<br>
    HTML 문서를 <u>BeautifulSoup</u>으로 혹은 <u>교내 서버</u>를 통해 <br>
    데이터를 추출하여 카카오톡 스킬 형식에 맞게 JSON 파일로 변환합니다.
    <br><br>
* 2️⃣ 서버
    <br><br>
    <table>
    <tr>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_aws.png?raw=true" width="100px" height="100px">
    </td>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_ubuntu.png?raw=true" width="100px" height="100px">
    </td>
    <td align="center">
    <img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/logo_flask.png?raw=true" width="100px" height="100px">
    </td>
    </tr>
    <tr>
    <td align="center">
    <b>AWS</b>
    </td>
    <td align="center">
    <b>Ubuntu</b>
    </td>
    <td align="center">
    <b>Flask</b>
    </td>
    </tr>
    </table>
    <b>대림식</b> 서버는 <u>Amazon Web Service EC2</u>를 이용하여 <u>Ubuntu</u> 운영체제를 사용하여<br>
    작동되고 있습니다. 일정시간마다 Python 파일을 실행하게끔 명령하여 <u>Flask</u>로<br>
    생성된 JSON 파일을 가지고 API 서버를 열어 카카오톡 서버와 통신합니다.
    <br><br>

## 3️⃣ 카카오톡 챗봇
<img src="https://github.com/hugesilver/Daelimsik/blob/main/readme/image_kakao_business.png?raw=true" width="700px"><br><br>
카카오톡 채널을 운영하기 위해서는 카카오비즈니스의 카카오 i 오픈빌더 서비스를 이용해야합니다.<br>
단순 비즈니스 채널을 생성해 사용자와 1:1 채팅을 할 수 있는 서비스도 이용가능하지만,<br>
챗봇 기능을 사용하여 상담원이 근무하는 시간 외에도 소통할 수 있다는 좋은 기능입니다.<br>
이 기능을 이용하여 <b>대림식</b>에 24시간동안(서버가 문제 생기지 않는 이상 혹은 점검 중이 아닐 때)<br>
정보 제공할 수 있는 프로젝트를 만들었습니다.<br>
개인적으로 카카오톡 챗봇 구현에 시간을 많이 투자한 것 같습니다.<br>
[[카카오 챗봇 가이드]](https://chatbot.kakao.com/docs/getting-started-overview)<br>