from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_cart(app):
    wait = WebDriverWait(app.wd, 10)
    for i in range(3):
        add_product_to_cart(app,wait)
    app.wd.find_element_by_xpath("//a[text()='Checkout »']").click()
    products_in_cart = app.wd.find_elements_by_css_selector("li.shortcut")
    for j in range(len(products_in_cart)):
        remove_product_from_cart(app, wait)


def add_product_to_cart(app, wait):
    app.wd.get("http://localhost/litecart")
    app.wd.find_element_by_css_selector(".product").click()
    quantity = app.wd.find_element_by_css_selector("span.quantity")
    text_before = quantity.text
    text_after = str(int(text_before) + 1)
    size_select = app.wd.find_elements_by_xpath("//select[@name='options[Size]']")
    if len(size_select) > 0:
        app.general.set_select_option(select_name='options[Size]', option_text='Small')
    app.wd.find_element_by_xpath("//button[@name='add_cart_product']").click()
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'quantity'), text_after))


def remove_product_from_cart(app, wait):
    order_summary = app.wd.find_element_by_css_selector("div#order_confirmation-wrapper tr")
    app.wd.find_element_by_xpath("//button[@name='remove_cart_item']").click()
    wait.until(EC.staleness_of(order_summary))
