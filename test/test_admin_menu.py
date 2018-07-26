def test_admin_menu(app):
    menu_items = app.wd.find_elements_by_id("app-")
    for i in range(len(menu_items)):
        app.wd.find_element_by_xpath("(//li[@id='app-'])[%s+1]" % i).click()
        assert app.wd.find_element_by_css_selector("h1")
        menu_sub_items = app.wd.find_elements_by_css_selector("li#app- li")
        if len(menu_sub_items) > 0:
            for j in range(len(menu_sub_items)):
                app.wd.find_element_by_xpath("(//li[@id='app-']//li)[%s+1]" % j).click()
                assert app.wd.find_element_by_css_selector("h1")
