from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	#Стартовая позиция страницы
	driver = webdriver.Chrome()
	link = 'http://suninjuly.github.io/math.html'
	driver.get(link)

	#Стандартный ввод и подсчёт формлуы
	input1 = driver.find_element_by_id('answer')
	number = driver.find_element_by_css_selector('.form-group #input_value')
	input1.send_keys(calc(number.text))

	#Поднимаем флажек за роботов 
	checbox1 = driver.find_element_by_css_selector('.form-check-custom .form-check-label')
	checbox1.click()

	#Выбор radiobtn
	radiobtn1 = driver.find_element_by_css_selector('.form-check.form-radio-custom .form-check-input')
	radiobtn1.click()
	btn = driver.find_element_by_tag_name("button")
	btn.click()
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	driver.quit()