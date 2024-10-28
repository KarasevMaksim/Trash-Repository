import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/file_input.html')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')         # добавляем к этому пути имя файла 
obj = browser.find_elements(By.CSS_SELECTOR, '[type=text]')
for i in obj:
    i.send_keys('message')
upload = browser.find_element(By.CSS_SELECTOR, '[type=file]')
upload.send_keys(file_path)
btn = browser.find_element(By.TAG_NAME, 'button')
btn.click()
time.sleep(10)