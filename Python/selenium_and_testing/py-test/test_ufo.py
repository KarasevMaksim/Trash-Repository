import time
import math
import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')

answer = math.log(int(time.time()))

link = 'https://stepik.org/lesson/'
link_prefix = [
    '236895/step/1',
    '236896/step/1',
    '236897/step/1',
    '236898/step/1',
    '236899/step/1',
    '236903/step/1',
    '236904/step/1',
    '236905/step/1'
]

@pytest.fixture(scope='class')
def load_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://stepik.org/lesson/236895/step/1')
    btn1 = driver.find_element(By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')
    btn1.click()
    modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog"))
    )
    modal.click()
    input_email = driver.find_element(By.ID, 'id_login_email')
    input_email.clear()
    input_email.send_keys(LOGIN)
    input_password = driver.find_element(By.ID, 'id_login_password')
    input_password.clear()
    input_password.send_keys(PASSWORD)
    btn2 = driver.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
    btn2.click()
    yield driver
    time.sleep(30)
    driver.quit()


@pytest.mark.parametrize('prefix', link_prefix)
class TestUfo():
    def test_1(self, load_driver, prefix):
        url = link + prefix
        load_driver.get(url)
        input_answer = load_driver.find_element(By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea')
        input_answer.clear()
        input_answer.send_keys(math.log(int(time.time())))
        btn3 = WebDriverWait(load_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'submit-submission'))
        )
        btn3.click()
        value = WebDriverWait(load_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints.ember-view.lesson__hint p'))
        )
        assert 'Correct!' == value.text
        
