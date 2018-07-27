def test_stickers(app):
    app.wd.get("http://localhost/litecart")
    goods = app.wd.find_elements_by_css_selector(".product")
    for g in goods:
        stickers = g.find_elements_by_xpath(".//div[contains(@class, 'sticker')]")
        assert len(stickers) == 1
