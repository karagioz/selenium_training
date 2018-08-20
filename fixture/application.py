from selenium import webdriver
from fixture.session import SessionHelper
from fixture.general import GeneralHelper
from fixture.main_page import MainPageHelper
from fixture.product_page import ProductPageHelper
from fixture.cart_page import CartPageHelper
# from browsermobproxy import Server


class Application:

    def __init__(self, browser, base_url):
        # self.server = Server("C:\\Tools\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy")
        # self.server.start()
        # self.proxy = self.server.create_proxy()
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "firefox_nightly":
            self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            # chrome_options.add_argument("--proxy-server={0}".format(self.proxy.proxy))
            self.wd = webdriver.Chrome(chrome_options=chrome_options)
                                       # , desired_capabilities={"loggingPrefs": {'performance': 'ALL'}})
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.general = GeneralHelper(self)
        self.main = MainPageHelper(self)
        self.product = ProductPageHelper(self)
        self.cart = CartPageHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        # self.server.stop()
        self.wd.quit()
