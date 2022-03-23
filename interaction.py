from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/wisangeom/dev-util/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url = 'http://secure-retreat-92358.herokuapp.com/'
driver.get(url)

fname_box = driver.find_element(By.NAME, "fName")
fname_box.send_keys("wisang")

lname_box = driver.find_element(By.NAME, "lName")
lname_box.send_keys("eom")

email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("abc@abc.com")

send_button = driver.find_element(By.CSS_SELECTOR, "form button")
send_button.click()

# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# arts_link = driver.find_element(By.LINK_TEXT, "The arts")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

# driver.quit()