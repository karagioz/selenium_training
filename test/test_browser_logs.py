def test_browser_logs(app):
    app.wd.find_element_by_xpath("//span[text()='Catalog']").click()
    app.wd.find_element_by_xpath("//a[text()='Rubber Ducks']").click()
    products = app.wd.find_elements_by_xpath("//tr[td[input[contains(@name, 'products')]]]")
    # print(app.wd.log_types)
    if len(products) > 0:
        for i in range(len(products)):
            row = app.wd.find_element_by_xpath("(//tr[td[input[contains(@name, 'products')]]])[%s+1]" % i)
            row.find_element_by_xpath("./td[img]/a").click()
            logs = []
            for l in app.wd.get_log("browser"):
                logs.append(l)
            assert len(logs) == 0
            app.wd.find_element_by_xpath("//button[@name='cancel']").click()
