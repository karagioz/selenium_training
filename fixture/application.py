from selenium import webdriver
from fixture.session import SessionHelper
from fixture.general import GeneralHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "firefox_nightly":
            self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["start-maximized"]},
                                                             "loggingPrefs": {'performance': 'ALL'}})
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.general = GeneralHelper(self)
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
        self.wd.quit()
