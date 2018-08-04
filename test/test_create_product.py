import os.path
import time
from selenium.webdriver.support.ui import Select


def test_create_product(app):
    app.wd.find_element_by_xpath("//span[text()='Catalog']").click()
    app.wd.find_element_by_xpath("//a[text()=' Add New Product']").click()
    fill_general_tab(app)
    open_tab(app, tab_name="Information")
    fill_information_tab(app)
    open_tab(app, tab_name="Prices")
    fill_prices_tab(app)
    app.wd.find_element_by_xpath("//button[@name='save']").click()
    app.wd.find_element_by_xpath("//span[text()='Catalog']").click()
    app.wd.find_element_by_xpath("//a[text()='Rubber Ducks']").click()
    assert len(app.wd.find_elements_by_xpath("//tr[@class='row']/td/a[text()='Green Frog']")) == 1


def open_tab(app, tab_name):
    app.wd.find_element_by_link_text(tab_name).click()
    time.sleep(1)


def set_select_option(app, select_name, option_text):
    select_element = Select(app.wd.find_element_by_xpath("//select[@name='%s']" % select_name))
    select_element.select_by_visible_text('%s' % option_text)


def fill_information_tab(app):
    set_select_option(app, select_name='manufacturer_id', option_text='ACME Corp.')
    app.wd.find_element_by_xpath("//input[@name='keywords']").send_keys('Fascinating green frog')
    app.wd.find_element_by_xpath("//input[@name='short_description[en]']"). \
        send_keys('Fascinating green frog is the best present for everyone')
    app.wd.find_element_by_css_selector(".trumbowyg-editor"). \
        send_keys('Fascinating green frog is the best present for everyone')
    app.wd.find_element_by_xpath("//input[@name='head_title[en]']").send_keys('Frog')
    app.wd.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys('Frog')


def fill_general_tab(app):
    app.wd.find_element_by_xpath("//input[@name='status' and @value='1']").click()
    app.wd.find_element_by_xpath("//input[@name='name[en]']").send_keys('Green Frog')
    app.wd.find_element_by_xpath("//input[@name='code']").send_keys('green_frog')
    app.wd.find_element_by_xpath("//input[@data-name='Root']").click()
    app.wd.find_element_by_xpath("//input[@data-name='Rubber Ducks']").click()
    app.wd.find_element_by_xpath("//input[@name='product_groups[]' and @value='1-3']").click()
    app.wd.find_element_by_xpath("//input[@name='quantity']").clear()
    app.wd.find_element_by_xpath("//input[@name='quantity']").send_keys('10')
    current_dir = os.path.dirname(os.path.dirname(__file__))
    filename = os.path.join(current_dir, 'src/green_frog.jpg')
    app.wd.find_element_by_xpath("//input[@name='new_images[]']").send_keys(filename)
    app.wd.find_element_by_xpath("//input[@name='date_valid_from']").send_keys('01.08.2018')
    app.wd.find_element_by_xpath("//input[@name='date_valid_to']").send_keys('31.08.2018')


def fill_prices_tab(app):
    app.wd.find_element_by_xpath("//input[@name='purchase_price']").clear()
    app.wd.find_element_by_xpath("//input[@name='purchase_price']").send_keys('23')
    set_select_option(app, select_name='purchase_price_currency_code', option_text='US Dollars')
    app.wd.find_element_by_xpath("//input[@name='prices[USD]']").send_keys('23')
    app.wd.find_element_by_xpath("//input[@name='gross_prices[USD]']").send_keys('23')
    app.wd.find_element_by_xpath("//input[@name='prices[EUR]']").send_keys('22')
    app.wd.find_element_by_xpath("//input[@name='gross_prices[EUR]']").send_keys('22')
