from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPageHelper:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.wait = WebDriverWait(app.wd, 10)

    def add_to_cart(self):
        self.wd.find_element_by_xpath("//button[@name='add_cart_product']").click()

    def get_total_quantity(self):
        return self.wd.find_element_by_css_selector("span.quantity")

    def open_cart_page(self):
        self.wd.find_element_by_xpath("//a[text()='Checkout »']").click()

    def set_size(self, value):
        size_select = self.wd.find_elements_by_xpath("//select[@name='options[Size]']")
        if len(size_select) > 0:
            self.app.general.set_select_option(select_name='options[Size]', option_text=value)

    def wait_for_updates(self, text):
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'quantity'), text))
