from .page.product_page import ProductPage
import pytest
from .page.base_page import BasePage
def test_guest_can_go_to_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solver_quiz_and_get_code()