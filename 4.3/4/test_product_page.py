from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(driver, link):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
	product_page = ProductPage(driver, link)
	product_page.open()
	product_page.shold_be_add_button()
	product_page.add_to_card()
	product_page.shold_be_message_add()