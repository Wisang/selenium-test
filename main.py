from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome_driver_path = "D:\dev-tools\chromedriver.exe"
chrome_driver_path = "/Users/wisangeom/dev-util/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url = 'https://www.python.org/'
driver.get(url)
# event_div = driver.find_element(By.CLASS_NAME, 'event-widget')

menu_path = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul'
event_div = driver.find_element(By.XPATH, menu_path)

date_list = event_div.find_elements(By.CSS_SELECTOR, "time")
title_list = event_div.find_elements(By.CSS_SELECTOR, "a")

event_dict = {}

for i in range(len(date_list)):
    event_dict[f"{i}"] = {date_list[i].text: title_list[i].text}

print(event_dict)

# event_dict = {}
#
# for item in event_div:
#     event_dict[item.find_element(By.CSS_SELECTOR, "time").text] = item.find_element(By.CSS_SELECTOR, "a").text

# print(event_dict)
# date_list = event_div.find_elements(By.CSS_SELECTOR, "time")
# title_list = event_div.find_elements(By.CSS_SELECTOR, "a")

# for tittle in title_list:
#     print(tittle.text)

driver.quit()

