from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(1)
    browser.quit()

@pytest.mark.parametrize("link",['https://stepik.org/lesson/236895/step/1',
                                 # 'https://stepik.org/lesson/236896/step/1',
                                 # 'https://stepik.org/lesson/236897/step/1',
                                 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1',
                                 # 'https://stepik.org/lesson/236903/step/1',
                                 # 'https://stepik.org/lesson/236904/step/1',
                                 'https://stepik.org/lesson/236905/step/1'])
class TestPage():
    def test_page(self, browser, link):
        browser.get(link)
        time.sleep(3)
        browser.find_element_by_css_selector(".ember-text-area").send_keys(f"{math.log(int(time.time()))}")
        browser.find_element_by_css_selector(".submit-submission").click()
        icon = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "correct_icon")))
        message = browser.find_element_by_css_selector('.smart-hints__hint').text

        assert message == "Correct!", f'{message}'


