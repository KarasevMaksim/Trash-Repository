import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/redirect_accept.html')

try:
    btn_first = driver.find_element(By.CLASS_NAME, 'trollface')
    btn_first.click()
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    value = driver.find_element(By.ID, 'input_value')
    y = calc(value.text)
    
    input1 = driver.find_element(By.ID, 'answer')
    input1.send_keys(y)

    btn = driver.find_element(By.TAG_NAME, 'button')
    btn.click()
    time.sleep(20)
    
finally:
    driver.quit()