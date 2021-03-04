from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	driver = webdriver.Chrome()
	link = 'http://suninjuly.github.io/redirect_accept.html'
	driver.get(link)

	#Первая страница редирект
	btn = driver.find_element_by_tag_name("button")
	btn.click()

	#Переход на 2 вкладку
	new_window = driver.window_handles[1]
	driver.switch_to.window(new_window)
	#Вычисляем
	numX = driver.find_element_by_css_selector('#input_value')
	numX = calc(numX.text)

	#Заполняем
	text_input = driver.find_element_by_css_selector('#answer')
	text_input.send_keys(numX)
	btn = driver.find_element_by_tag_name("button")
	btn.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(11)
	# закрываем браузер после всех манипуляций
	driver.quit()
