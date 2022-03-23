import time
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\dev-tools\chromedriver.exe"
# chrome_driver_path = "/Users/wisangeom/dev-util/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url = 'https://orteil.dashnet.org/experiments/cookie/'
driver.get(url)

cookie = driver.find_element(By.ID, "cookie")
# store = driver.find_elements(By.CSS_SELECTOR, "#store div")

inner_loop_end = time.time() + 5
outer_loop_end = time.time() + 60*2

while time.time() < outer_loop_end:
    while time.time() < inner_loop_end:
        cookie.click()

    inner_loop_end = inner_loop_end + 5

    store = driver.find_elements(By.CSS_SELECTOR, "#store div")

    for i in range(len(store)-1, -1, -1):
        try:
            if store[i].get_attribute("class") == "":
                print(f"{store[i].text} is clicked")
                store[i].click()
                break
        except selenium.common.exceptions.StaleElementReferenceException:
            pass

cps = driver.find_element(By.ID, "cps")

print("click/second is " + cps.text)

driver.quit()

# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# arts_link = driver.find_element(By.LINK_TEXT, "The arts")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

# driver.quit()