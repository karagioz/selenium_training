def test_login(app):
    # app.proxy.new_har("test proxy")
    app.session.logout()
    username = "admin"
    password = "admin"
    app.session.login(username=username, password=password)
    assert ("You are now logged in as %s" % username in app.wd.page_source)
    # for l in app.proxy.har["log"]["entries"]:
    #     print(l["request"]["url"] + ' : ' + str(l["response"]["status"]))
