import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element_by_id('treasure')
    value = x.get_attribute("valuex")
    y = calc(value)
    answer = browser.find_element_by_id('answer').send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_class_name('btn')
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
