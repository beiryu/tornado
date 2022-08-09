import tornado.web
import tornado.escape

class BaseHandler(tornado.web.RequestHandler):

    def get_login_url(self):
        return u"/login"

    def get_current_user(self):
        return self.get_secure_cookie("user")


class LoginHandler(BaseHandler):

    def get(self):
        self.render("sign-in.html", next=self.get_argument("next","/"))

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        auth = self.application.db.users.find_one({"username": username, "password": password})
        if auth:
            self.set_current_user(username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
            self.redirect(u"/login" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", user)
        else:
            self.clear_cookie("user")


class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("user")
        self.redirect(u"/login")


class DashboardHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render(
            'dashboard.html',
            user=self.current_user
        )
