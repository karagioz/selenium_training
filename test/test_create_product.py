import os.path


def test_create_product(app):
    app.wd.find_element_by_xpath("//span[text()='Catalog']").click()
    app.wd.find_element_by_xpath("//a[text()=' Add New Product']").click()
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
    app.wd.find_element_by_xpath("//button[@name='save']").click()
