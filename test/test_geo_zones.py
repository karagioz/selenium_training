def test_geo_zones(app):
    app.wd.find_element_by_xpath("//a//span[text()='Geo Zones']").click()
    counties = app.wd.find_elements_by_xpath("//tr[@class='row']//a[not(@title)]")
    for i in range(len(counties)):
        app.wd.find_element_by_xpath("(//tr[@class='row']//a[not(@title)])[%s+1]" % i).click()
        zone_elements = app.wd.find_elements_by_xpath\
            ("//select[contains(@name, 'zone_code')]//option[@selected='selected']")
        zones = []
        for zone in zone_elements:
            zones.append(zone.text)
        assert zones == sorted(zones)
        app.wd.find_element_by_xpath("//a//span[text()='Geo Zones']").click()
