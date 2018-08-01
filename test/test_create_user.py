import random
import string
from selenium.webdriver.support.ui import Select


def test_create_user(app):
    app.wd.get("http://localhost/litecart")
    app.wd.find_element_by_link_text("New customers click here").click()
    email = random_string(10) + '@gmail.com'
    password = 'test_password'
    first_name = 'First Name'
    last_name = 'Last Name'
    fill_user_form(app, email, first_name=first_name, last_name=last_name, password=password,
                   confirmed_password=password)
    app.wd.find_element_by_name("create_account").click()
    app.wd.find_element_by_link_text("Logout").click()
    user_login(app, email, password)
    assert app.wd.find_element_by_class_name("notice").text == "You are now logged in as %s %s." % (first_name, last_name)
    app.wd.find_element_by_link_text("Logout").click()
    assert app.wd.find_element_by_class_name("notice").text == "You are now logged out."


def user_login(app, email, password):
    app.wd.find_element_by_name("email").send_keys(email)
    app.wd.find_element_by_name("password").send_keys(password)
    app.wd.find_element_by_name("login").click()


def fill_user_form(app, email, first_name="Test First Name", last_name="Test Last Name", address="Test Address",
                   postcode="12345", city="Los Angeles", country_name="United States", state_name="California",
                   phone="123456789", password="12345", confirmed_password="12345"):
    app.wd.find_element_by_name("firstname").send_keys(first_name)
    app.wd.find_element_by_name("lastname").send_keys(last_name)
    app.wd.find_element_by_name("address1").send_keys(address)
    app.wd.find_element_by_name("postcode").send_keys(postcode)
    app.wd.find_element_by_name("city").send_keys(city)
    country = Select(app.wd.find_element_by_name("country_code"))
    country.select_by_visible_text(country_name)
    state = Select(app.wd.find_element_by_css_selector("select[name=zone_code]"))
    state.select_by_visible_text(state_name)
    app.wd.find_element_by_name("email").send_keys(email)
    app.wd.find_element_by_name("phone").send_keys(phone)
    app.wd.find_element_by_name("password").send_keys(password)
    app.wd.find_element_by_name("confirmed_password").send_keys(confirmed_password)


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(maxlen)])
