from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPageHelper:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.wait = WebDriverWait(app.wd, 10)

    def get_order_summary(self):
        return self.wd.find_element_by_css_selector("div#order_confirmation-wrapper tr")

    def get_products(self):
        return self.wd.find_elements_by_css_selector("li.shortcut")

    def remove_product(self):
        self.wd.find_element_by_xpath("//button[@name='remove_cart_item']").click()

    def wait_for_updates(self, element):
        self.wait.until(EC.staleness_of(element))
