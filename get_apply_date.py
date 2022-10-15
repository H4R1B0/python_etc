"""
python, BeautifulSoup, selenium
"""

import os
import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

#popup close all
def popup_close():
    driver_count = len(driver.window_handles) #popup count
    while driver_count != 1:
        driver.switch_to.window(driver.window_handles[1]) 
        driver.close()
        driver_count -= 1

userId = 'your_id'
userPass = 'your_password'

city_list = ['고양시청', '남양주시청', '양주시청', '의정부시청', '파주시청', '포천시청', '김포시청']

driver = webdriver.Chrome()
driver.get('https://www.greenproduct.go.kr/boiler/main.do')
assert '가정용 보일러 인증시스템' in driver.title

popup_close()

#login
driver.switch_to.window(driver.window_handles[0])
elem = driver.find_element('id', 'userId')
elem.send_keys(userId)
elem = driver.find_element('id', 'userPass')
elem.send_keys(userPass)
elem.send_keys(Keys.RETURN)

#move site
driver.get('https://www.greenproduct.go.kr/boiler/elms/request/application_leftpage_new1.do')

select_area = Select(driver.find_element('id', 'AREA_SECD'))
select_area.select_by_visible_text('경기도')

for city in city_list:
    time.sleep(0.5)

    select_local = Select(driver.find_element('id', 'ITLPC_LOCGOV_CD'))
    select_local.select_by_visible_text(city)

    time.sleep(0.5)
    try:
        Alert(driver).accept()
    except:
        pass

    cur_html = driver.page_source
    soup = BeautifulSoup(cur_html, 'html.parser')
    date = soup.select('#rprsYmdDiv > span:nth-child(2)')[0].text
    print(city, date,'\n')

driver.quit()
os.system("pause")
