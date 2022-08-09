import datetime
import tornado.web

from admin.handlers import BaseHandler
from bson.objectid import ObjectId


class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        coll = self.application.db.users
        users = coll.find()
        self.render(
            'users.html',
            users = users
        )


class UserEditHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "sign-up.html"
        )

    def post(self):
        import time
        user_fields = ['username', 'email', 'password']
        coll = self.application.db.users
        user = dict()
        for key in user_fields:
            user[key] = self.get_argument(key, None)
        user['date_added'] = datetime.datetime.utcnow()
        coll.insert_one(user)
        self.redirect("/")


class UserRemoveHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self, id=None):
        if id:
            self.application.db.users.delete_one({"_id": ObjectId(id)})
        self.redirect("/user")
