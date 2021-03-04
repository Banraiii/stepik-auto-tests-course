from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
	driver = webdriver.Chrome()
	link = 'http://suninjuly.github.io/selects1.html'
	driver.get(link)

	# find span by id
	num1 = driver.find_element_by_css_selector("h2 span#num1")
	num2 = driver.find_element_by_css_selector("h2 span#num2")
	result = int(num1.text) + int(num2.text)

	#drop down structure 
	select = Select(driver.find_element_by_tag_name("select"))
	select.select_by_value(f"{ result }") 

	#use btn
	btn = driver.find_element_by_tag_name("button")
	btn.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	driver.quit()
