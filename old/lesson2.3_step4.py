import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    
    browser.find_element_by_class_name('btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(f"{y}")
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(15)

