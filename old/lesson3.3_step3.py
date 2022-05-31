from selenium import webdriver
import time
import unittest


class Test_Page(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
        input_name.send_keys("Stepan")
        input_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
        input_name.send_keys("Shakirov")
        input_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
        input_name.send_keys("asd@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_page2(self):
        #второй тест
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
        input_name.send_keys("Stepan")
        input_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
        input_name.send_keys("Shakirov")
        input_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
        input_name.send_keys("asd@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

       # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()

