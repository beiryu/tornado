import tornado.web

from chat.handlers import Messager
from .urls import urlpatterns
from pymongo import MongoClient
from ui import handlers as uimodules
from storefront.settings import DATABASE_NAME, HOST, TEMPLATE_PATH, STATIC_PATH, COOKIE_SECRET, LOGIN_URL

class Application(tornado.web.Application):
    def __init__(self):
        self.messager = Messager()

        handlers = urlpatterns

        conn = MongoClient(HOST, 27017)
        self.db = conn[DATABASE_NAME]

        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            ui_modules= uimodules,
            # debug=True,
            autoreload=True,
            cookie_secret=COOKIE_SECRET,
            xsrf_cookies=False,
            login_url=LOGIN_URL
        )
        
        tornado.web.Application.__init__(self, handlers, **settings)