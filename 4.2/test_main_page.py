from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

def test_guest_can_go_to_login_page(driver):
	link = "http://selenium1py.pythonanywhere.com"
	page = MainPage(driver, link)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()						# открываем страницу
	page.should_be_login_link()		# выполняем проверку нахождения логин линк
	page.go_to_login_page()			# выполняем метод страницы — переходим на страницу логина
	login_page = LoginPage(driver, driver.current_url)
	login_page.should_be_login_page()