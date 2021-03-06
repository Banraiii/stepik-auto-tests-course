from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import time
import pytest


def test_guest_shold_see_login_link_on_product_page(driver):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(driver, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
	link = "http://selenium1py.pythonanywhere.com/en-gb/"
	page = ProductPage(driver, link)
	page.open()
	page.go_to_login_page()