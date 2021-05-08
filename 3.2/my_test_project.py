from selenium import webdriver
import unittest
import selenium
import time

class ThreeTest(unittest.TestCase):
	"""Тестовый класс для 3 тестов"""
	def test_for_first_page(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
		input1.send_keys('Kostyans')
		input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
		input2.send_keys('Kostyans')
		input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
		input3.send_keys('Kostyans@kostyansdog.ru')
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

		# с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'падение 1 теста')

		# закрываем браузер после всех манипуляций
		browser.quit()
	def test_for_two_page(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
		input1.send_keys('Kostyans')
		input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
		input2.send_keys('Kostyans')
		input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
		input3.send_keys('Kostyans@kostyansdog.ru')
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
		
		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'падение 2 теста')
		browser.quit()
		
if __name__ == "__main__":
    unittest.main()