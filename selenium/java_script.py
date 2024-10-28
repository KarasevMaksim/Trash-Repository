from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
value = browser.find_element(By.ID, "input_value")
y = calc(value.text)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

btn = browser.find_element(By.TAG_NAME, 'button')
browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radio = browser.find_element(By.ID, 'robotsRule')
radio.click()
btn.click()

time.sleep(10)