from .locators import PageProductLocators
from .base_page import BasePage

class PageObject(BasePage):
    def go_to_basket_product(self):
        product_link = self.browser.find_element(*PageProductLocators.BASKET_FORM)
        product_link.click()

    #def should_be_basket_button(self):

        #assert self.is_element_present(*PageProductLocators.BASKET_FORM),\
        #"basket button is not present"
    def should_not_be_success_product_name(self):
        assert self.is_not_element_present(*PageProductLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_product_name(self):
        assert self.is_disappeared(*PageProductLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should disappear"

    def should_be_succes_product_price(self):
        assert self.is_element_present(*PageProductLocators.SUCCESS_PRODUCT_PRICE), \
            'No product price'

    def get_product_price(self):
        return self.browser.find_element(*PageProductLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*PageProductLocators.PRODUCT_NAME).text

    def get_success_product_price(self):
        return self.browser.find_element(*PageProductLocators.SUCCESS_PRODUCT_PRICE).text

    def get_success_product_name(self):
        return self.browser.find_element(*PageProductLocators.SUCCESS_PRODUCT_NAME).text

    def is_success_name_correct(self):
        assert self.get_product_name() == self.get_success_product_name(), \
            'Names of added product and product are unequal'

    def is_success_price_correct(self):
        assert self.get_product_price() == self.get_success_product_price(), \
        'Prices of added product and product are unequal'

    