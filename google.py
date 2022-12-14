from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

person = "isaac newton"

PATH = "/Users/harishgundluru/Downloads/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get("https://google.com")
print(driver.title)

search = driver.find_element(By.NAME, "q")
search.click()
search.send_keys(person)
search.send_keys(Keys.RETURN)
try:
    about = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "kno-rdesc"))
    )
except:
    driver.quit()
about = driver.find_element(By.CLASS_NAME, "kno-rdesc")
time.sleep(2)
print(about.text)
driver.quit()
