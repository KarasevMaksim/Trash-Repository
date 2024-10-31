import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link1 = 'http://selenium1py.pythonanywhere.com/'
link2 = '/catalogue/coders-at-work_207/'

def test_botton_add_basket(browser):
    driver, lang = browser
    url = f'{link1}{lang}{link2}'
    driver.get(url)
    time.sleep(30)
    try:
        button = driver.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    except NoSuchElementException:
        button = None
    assert button, 'Button not found!'
