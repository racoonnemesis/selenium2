import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 200);")
    answer = browser.find_element_by_id('answer').send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_class_name('btn')
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()
