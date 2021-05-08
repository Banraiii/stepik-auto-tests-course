import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope="function")
def driver():
	print('\n start браузер для селедующих тестов')
	driver = webdriver.Chrome()
	yield driver
	print('\nвыход из браузера')
	driver.quit()


class TestMainPage1():

	@pytest.mark.smoke
	def test_guest_should_see_login_link(self, driver):
		driver.get(link)
		driver.find_element_by_css_selector("#login_link")

	@pytest.mark.smoke
	@pytest.mark.win10
	def test_guest_should_see_basket_link_on_the_main_page(self, driver):
		driver.get(link)
		driver.find_element_by_css_selector(".basket-mini .btn-group > a")
