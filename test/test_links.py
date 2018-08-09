from selenium.webdriver.support.wait import WebDriverWait


def test_links(app):
    app.wd.find_element_by_xpath("//span[text()='Countries']").click()
    app.wd.find_element_by_css_selector("a.button").click()
    external_links = app.wd.find_elements_by_css_selector("a i.fa-external-link")
    main_window = app.wd.current_window_handle
    old_windows = app.wd.window_handles
    wait = WebDriverWait(app.wd, 10)
    for i in range(len(external_links)):
        app.wd.find_element_by_xpath("(//a/i[@class='fa fa-external-link'])[%s+1]" % i).click()
        new_window = wait.until(lambda d: new_window_is_opened(d, old_windows))
        app.wd.switch_to_window(new_window)
        app.wd.close()
        app.wd.switch_to_window(main_window)


def new_window_is_opened(driver, windows_before):
    current_windows = driver.window_handles
    windows_diff = list(set(current_windows) - set(windows_before))
    return windows_diff[0] if (len(windows_diff) > 0) else None
