import re


def test_product_page(app):
    app.wd.get("http://localhost/litecart")
    info_main = {}
    info_product = {}
    product = app.wd.find_element_by_css_selector("#box-campaigns a.link")
    regular_price_m = product.find_element_by_css_selector(".regular-price")
    campaign_price_m = product.find_element_by_css_selector(".campaign-price")
    info_main['text'] = product.find_element_by_css_selector("div.name").text
    info_main['regular_price'] = regular_price_m.text
    info_main['campaign_price'] = campaign_price_m.text
    info_main['regular_price_style'] = regular_price_m.get_attribute("tagName")
    info_main['campaign_price_style'] = campaign_price_m.get_attribute("tagName")
    regular_price_color_main = regular_price_m.value_of_css_property("color")
    campaign_price_color_main = campaign_price_m.value_of_css_property("color")
    regular_price_size_main = regular_price_m.size
    campaign_price_size_main = campaign_price_m.size
    product.click()
    info_product['text'] = app.wd.find_element_by_css_selector("h1").text
    regular_price_p = app.wd.find_element_by_css_selector(".regular-price")
    campaign_price_p = app.wd.find_element_by_css_selector(".campaign-price")
    info_product['regular_price'] = regular_price_p.text
    info_product['campaign_price'] = campaign_price_p.text
    info_product['regular_price_style'] = regular_price_p.get_attribute("tagName")
    info_product['campaign_price_style'] = campaign_price_p.get_attribute("tagName")
    regular_price_color_product = regular_price_p.value_of_css_property("color")
    campaign_price_color_product = campaign_price_p.value_of_css_property("color")
    regular_price_size_product = regular_price_p.size
    campaign_price_size_product = campaign_price_p.size
    assert is_equal(info_main, info_product) \
           and info_main['regular_price_style'] == 'S' \
           and info_main['campaign_price_style'] == 'STRONG' \
           and is_grey(regular_price_color_main) \
           and is_grey(regular_price_color_product) \
           and is_red(campaign_price_color_main) \
           and is_red(campaign_price_color_product) \
           and is_larger(campaign_price_size_main, regular_price_size_main) \
           and is_larger(campaign_price_size_product, regular_price_size_product)


def is_grey(str):
    rgb_values = [int(s) for s in re.sub('[(),]', ' ', str).split() if s.isdigit()]
    if len(rgb_values) >= 3:
        return (rgb_values[0] == rgb_values[1]) and (rgb_values[1] == rgb_values[2])
    else:
        return False


def is_red(str):
    rgb_values = [int(s) for s in re.sub('[(),]', ' ', str).split() if s.isdigit()]
    if len(rgb_values) >= 3:
        return (rgb_values[1] == 0) and (rgb_values[2] == 0)
    else:
        return False


def is_larger(size2, size1):
    return (size2['height'] > size1['height']) and (size2['width'] > size1['width'])


def is_equal(dict1, dict2):
    return dict1['text'] == dict2['text'] and \
           dict1['regular_price'] == dict2['regular_price'] and \
           dict1['campaign_price'] == dict2['campaign_price'] and \
           dict1['regular_price_style'] == dict2['regular_price_style'] and \
           dict1['campaign_price_style'] == dict2['campaign_price_style']
