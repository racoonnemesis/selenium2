import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_class_name('btn')
    button.click()
    
finally:
    print(x)
    time.sleep(15)
    browser.quit()
