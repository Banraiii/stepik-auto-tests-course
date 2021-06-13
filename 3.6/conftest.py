import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default=None,
		help='Выберите язык ="es" ')

    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
	user_language = request.config.getoption("language")
	driver = None
	print("\nstart chrome browser for test..")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	driver = webdriver.Chrome(options=options)
	yield driver
	print("\nquit browser..")
	driver.quit()

