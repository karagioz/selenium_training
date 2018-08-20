class MainPageHelper:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def open_main_page(self):
        self.wd.find_element_by_css_selector("#logotype-wrapper").click()

    def open_product_page(self):
        self.wd.find_element_by_css_selector(".product").click()
