from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=900#page1')
sleep(5)
html_900 = driver.page_source
driver.quit() # 웹드라이버 종료
f900 = open("./data/html_900.txt", 'w')
f900.write(html_900)
f900.close()

driver = webdriver.Chrome("./webdriver/chromedriver",chrome_options=option)
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=990#page1')
sleep(5)
html_990 = driver.page_source
driver.quit() # 웹드라이버 종료
f990 = open("./data/html_990.txt", 'w')
f990.write(html_990)
f990.close()
