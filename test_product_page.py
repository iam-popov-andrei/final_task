import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('promo', ['https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'])
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(browser, promo)
    page.open()
    
    page.add_product_to_basket()
