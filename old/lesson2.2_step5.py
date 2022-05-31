from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

#поиск кнопки и использование JavaScript для прокрутки до видимости кнопки
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#прокуртка на 200 пикселей вниз
browser.execute_script("window.scrollBy(0, 200);")

time.sleep(5)
browser.quit()