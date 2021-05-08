import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# Я просто раньше занимался авто тестами, привычка использовать слово driver/ Это уже дело вкуса не судите
def test_check_page_have_add_btn(driver):
	driver.get(link)
	btn = driver.find_element_by_css_selector('.btn-lg.btn-primary')
	assert btn != None, "Нет элемента на стриничке"
	print(btn.text)