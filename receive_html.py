from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("./webdriver/chromedriver")
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=1470')
sleep(5)
html_1470 = driver.page_source
driver.quit() # 웹드라이버 종료
f1470 = open("./data/html_1470.txt", 'w')
f1470.write(html_1470)
f1470.close()

driver = webdriver.Chrome("./webdriver/chromedriver")
driver.get('https://www.daelim.ac.kr/cms/FrCon/index.do?MENU_ID=1480')
sleep(5)
html_1480 = driver.page_source
driver.quit() # 웹드라이버 종료
f1480 = open("./data/html_1480.txt", 'w')
f1480.write(html_1480)
f1480.close()