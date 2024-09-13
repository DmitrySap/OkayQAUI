import pytest
from selenium import webdriver  # подключили библиотеку вебдрайвер


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)  # вызвал неявное ожидание
    yield browser
    browser.quit()