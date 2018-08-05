from selenium.webdriver.support.ui import Select


class GeneralHelper:

    def __init__(self, app):
        self.app = app

    def set_select_option(self, select_name, option_text):
        wd = self.app.wd
        select_element = Select(wd.find_element_by_xpath("//select[@name='%s']" % select_name))
        select_element.select_by_visible_text('%s' % option_text)
