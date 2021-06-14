from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math


class BasePage:
	def __init__(self, driver, url, timeout=10):
		self.driver = driver
		self.url = url

	def open(self):
		self.driver.get(self.url)

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(how, what)
		except NoSuchElementException:
			return False
		return True

	def solve_quiz_and_get_code(self):
		prompt = self.driver.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		prompt.send_keys(answer)
		prompt.accept()
		try:
			alert = self.driver.switch_to.alert
			alert_text = alert.text
			print(f"Ваш код: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print('Второго предупреждения не было')