import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


result = ''

@pytest.fixture()
def driver():
	print('\nСтарт браузера...')
	driver = webdriver.Chrome()
	yield driver
	print('\nЗакрытие браузера...')
	#time.sleep(4) для тестов)
	driver.quit()

@pytest.mark.parametrize('link',  ["236895", "236896","236897",'236898','236899', '236903', '236904','236905'])
class TestAliens:
	def test_first_link(self, driver, link):
		global result
		link = f"https://stepik.org/lesson/{link}/step/1"
		driver.get(link)
		textarea = WebDriverWait(driver, 12).until(
				EC.element_to_be_clickable((By.CSS_SELECTOR , '.textarea.ember-text-area'))
			)
		answer = math.log(int(time.time()))
		textarea.send_keys(f'{answer}')

		btn = driver.find_element(By.CSS_SELECTOR , '.submit-submission')
		btn.click()

		checkTrue = 'Correct!'
		checkitem = WebDriverWait(driver, 12).until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, '.smart-hints__feedback'))
			)
		if checkTrue != checkitem.text:
			print(checkitem.text)
			result += str(checkitem.text)
		
		assert checkTrue == checkitem.text, 'Не верный ответ!'

print(result)