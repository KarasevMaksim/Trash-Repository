import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose lang: ru, en ...')


@pytest.fixture()
def browser(request):
    resp_lang = request.config.getoption('language')
    browser = webdriver.Chrome()
    if resp_lang:
        yield browser, resp_lang
    browser.quit()