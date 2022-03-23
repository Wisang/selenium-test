from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome_driver_path = "D:\dev-tools\chromedriver.exe" for window
chrome_driver_path = "/Users/wisangeom/dev-util/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url = 'https://www.python.org/'
driver.get(url)

# menu_path = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul'
# event_div = driver.find_element(By.XPATH, menu_path)

date_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
title_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event_dict = {f"{i}": {f"date: {date_list[i].text}", f"name: {title_list[i].text}"} for i in range(len(date_list))}

print(event_dict)

driver.quit()

