from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.ID, 'num1')
    value2 = browser.find_element(By.ID, 'num2')
    value = int(value1.text) + int(value2.text)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(value))
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()
    


finally:
    time.sleep(10)
    browser.quit()
