def test_cart(app):
    app.general.open_url("http://localhost/litecart")
    for i in range(3):
        add_product_to_cart(app)
    app.product.open_cart_page()
    products_in_cart = app.cart.get_products()
    for j in range(len(products_in_cart)):
        remove_product_from_cart(app)


def add_product_to_cart(app):
    app.main.open_product_page()
    items_in_cart = app.product.get_total_quantity()
    text_before = items_in_cart.text
    text_after = str(int(text_before) + 1)
    app.product.set_size('Small')
    app.product.add_to_cart()
    app.product.wait_for_updates(text_after)
    app.main.open_main_page()


def remove_product_from_cart(app):
    order_summary = app.cart.get_order_summary()
    app.cart.remove_product()
    app.cart.wait_for_updates(order_summary)
