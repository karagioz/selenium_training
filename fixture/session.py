class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Logout]").click()
