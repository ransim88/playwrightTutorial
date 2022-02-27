
class LoginPage:
    def __init__(self, page):
        self.page = page

    username_elem = "[aria-label='Username']"
    password_elem = "[aria-label='Password']"

    def login_form(self, username, password):
        username_elem = "[aria-label='Username']"
        password_elem = "[aria-label='Password']"
        self.page.fill(username_elem, username)
        self.page.fill(password_elem, password)




