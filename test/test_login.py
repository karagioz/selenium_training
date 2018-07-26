def test_login(app):
    app.session.logout()
    username = "admin"
    password = "admin"
    app.session.login(username=username, password=password)
    assert ("You are now logged in as %s" % username in app.wd.page_source)
