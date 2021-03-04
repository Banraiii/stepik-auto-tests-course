from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	driver = webdriver.Chrome()
	driver.get('http://suninjuly.github.io/explicit_wait2.html')
	button = driver.find_element(By.ID , 'book')
	price = WebDriverWait(driver, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	button = driver.find_element(By.ID , 'book')
	button.click()

	inpX = driver.find_element(By.CSS_SELECTOR, '#input_value')
	text_inp = driver.find_element(By.CSS_SELECTOR, '#answer')
	text_inp.send_keys(calc(inpX.text))
	btnOut = driver.find_element(By.CSS_SELECTOR, '#solve')
	btnOut.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	driver.quit()
