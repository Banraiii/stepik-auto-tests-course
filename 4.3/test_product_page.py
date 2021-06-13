from .pages.product_page import ProductPage


def test_guest_can_add_to_card(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.shold_be_add_button()
    product_page.add_to_card()
