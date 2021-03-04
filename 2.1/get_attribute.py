from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	#Стартовая позиция страницы
	driver = webdriver.Chrome()
	link = 'http://suninjuly.github.io/get_attribute.html'
	driver.get(link)

	#Стандартный ввод и подсчёт формлуы
	input1 = driver.find_element_by_id('answer')
	picture = driver.find_element_by_tag_name('img')
	picture_checked = picture.get_attribute('valuex') 
	input1.send_keys(calc(picture_checked))
	print(picture_checked)
	#Поднимаем флажек за роботов 
	checbox1 = driver.find_element_by_css_selector('.check-input#robotCheckbox')
	checbox1.click()

	#Выбор radiobtn
	radiobtn1 = driver.find_element_by_css_selector('.check-input#robotsRule')
	radiobtn1.click()
	btn = driver.find_element_by_tag_name("button")
	btn.click()
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	driver.quit()
