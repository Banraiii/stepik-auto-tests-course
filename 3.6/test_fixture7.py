import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
	print('\nЗапуск браузера для тестирован...')
	driver = webdriver.Chrome()
	yield driver
	print('\nВыход из браузера')
	driver.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(driver, language):
	link = f"http://selenium1py.pythonanywhere.com/{language}/"
	driver.get(link)
	driver
	.find_element_by_css_selector("#login_link")