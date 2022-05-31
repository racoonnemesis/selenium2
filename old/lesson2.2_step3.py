import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:    
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    sum = int(num1) + int(num2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(sum))

    browser.find_element_by_class_name('btn').click()

finally:
    print(sum)
    time.sleep(15)
    browser.quit()
