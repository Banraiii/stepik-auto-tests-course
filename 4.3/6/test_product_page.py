from .pages.product_page import ProductPage
import time
import pytest


def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
	product_page = ProductPage(driver, link)
	product_page.open()
	product_page.add_to_card()
	product_page.shold_not_be_message_in_page()

def test_guest_cant_see_success_message(driver):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
	product_page = ProductPage(driver, link)
	product_page.open()
	product_page.shold_not_be_message_in_page()

def test_message_disappeared_after_adding_product_to_basket(driver):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
	product_page = ProductPage(driver, link)
	product_page.open()
	product_page.add_to_card()
	product_page.shold_be_disappeared_message()