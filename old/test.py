from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link = "https://oro-inv-tst-01.luxoft.com/Invoicing/WebApi/sales-orders"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element_by_css_selector('[href="/Invoicing/WebApi/invoices"]')
    # button = browser.find_element_by_css_selector(".inv-logo.m-auto")
    # button = WebDriverWait(browser, 5).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/Invoicing/WebApi/invoices"]'))
    # )
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()