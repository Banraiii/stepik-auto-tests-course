from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def shold_be_add_button(self):
		assert self.self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Нет кнопки добавить в коризину!'

	def add_to_card(self):
		btn = self.driver.find_element(*ProductPageLocators.ADD_BUTTON)
		btn.click()
		btn.solve_quiz_and_get_code()