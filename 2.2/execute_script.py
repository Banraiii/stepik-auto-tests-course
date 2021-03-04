from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	driver = webdriver.Chrome()
	link = 'http://SunInJuly.github.io/execute_script.html'
	driver.get(link)

	#Считаем X скролим
	numX = driver.find_element_by_css_selector('.form-group #input_value')
	numX = calc(numX.text)
	driver.execute_script("window.scrollBy(0, 100);")

	#Заполняем
	text_input = driver.find_element_by_css_selector('.form-group input')
	text_input.send_keys(numX)
	checkbox = driver.find_element_by_css_selector('.form-check #robotCheckbox')
	checkbox.click()
	radiobtn = driver.find_element_by_css_selector('.form-radio-custom .form-check-input')
	radiobtn.click()
	btn = driver.find_element_by_tag_name("button")
	btn.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	driver.quit()
