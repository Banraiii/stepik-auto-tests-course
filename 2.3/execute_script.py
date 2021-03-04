from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	driver = webdriver.Chrome()
	link = 'http://suninjuly.github.io/alert_accept.html'
	driver.get(link)

	#Первая страница редирект
	btn = driver.find_element_by_tag_name("button")
	btn.click()
	alert = browser.switch_to.alert
	alert.accept()
	numX = driver.find_element_by_css_selector('#input_value')
	numX = calc(numX.text)
	driver.execute_script("window.scrollBy(0, 100);")

	#Заполняем
	text_input = driver.find_element_by_css_selector('#answer')
	text_input.send_keys(numX)
	btn = driver.find_element_by_tag_name("button")
	btn.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	driver.quit()
