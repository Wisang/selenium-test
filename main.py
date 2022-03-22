import webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\dev-tools\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.amazon.com/Fitbit-Advanced-Management-Tracking-Graphite/dp/B09BXQ4HMB/ref=sr_1_3?crid=2ZKPHWC7E8LIL&keywords=fitbit&qid=1647961526&sprefix=fitbit%2Caps%2C265&sr=8-3')
price = driver.find_element(By.XPATH, '//*[@id="olp_feature_div"]/div[2]/span/a/span[2]')

print(price.text)

