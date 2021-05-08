from selenium import webdriver
import time
import os

try:
	driver = webdriver.Chrome()
	link = 'http://suninjuly.github.io/file_input.html'
	driver.get(link)

	#Данные
	name = driver.find_element_by_css_selector("[placeholder='Enter first name']")
	name.send_keys('Kostyans')
	lastN = driver.find_element_by_css_selector("[placeholder='Enter last name']")
	lastN.send_keys('Levi-Brawo')
	email = driver.find_element_by_css_selector("[placeholder='Enter email']")
	email.send_keys('KostyansLevi@Brawo.com')

	file = driver.find_element_by_css_selector('#file')
	current_dir = os.path.abspath(os.path.dirname(__file__))    
	print(current_dir)
	print(os.path.abspath(os.path.dirname(__file__)))
	file_path = os.path.join(current_dir, 'text.txt')   
	file.send_keys(file_path)

	btn = driver.find_element_by_tag_name("button")
	btn.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	driver.quit()
