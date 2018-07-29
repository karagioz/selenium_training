def test_countries(app):
    app.wd.find_element_by_xpath("//a//span[text()='Countries']").click()
    rows = app.wd.find_elements_by_css_selector(".row")
    countries = []
    countries_with_zones = []
    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        country_name = cells[4].find_element_by_tag_name("a")
        countries.append(country_name.text)
        zones_column = cells[5]
        if int(zones_column.text) > 0:
            countries_with_zones.append(country_name.text)
    assert countries == sorted(countries)
    for cwz in countries_with_zones:
        zones = []
        app.wd.find_element_by_xpath("//a[text()='%s']" % cwz).click()
        zones_name = app.wd.find_elements_by_xpath("//td[input[contains(@name, '[name]') and not(@value='')]]")
        for zone in zones_name:
            zones.append(zone.text)
        assert zones == sorted(zones)
        app.wd.find_element_by_xpath("//a//span[text()='Countries']").click()
