import tornado.web

from admin.handlers import BaseHandler
from bson.objectid import ObjectId
import datetime


class HistoryHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        coll = self.application.db.histories
        histories = coll.find()
        self.render(
            'history.html',
            histories = histories
        )

    def post(self, id=None):
        coll = self.application.db.histories
        history = dict()
        if id:
            history = coll.update_one({"_id": ObjectId(id)}, {'$set': {'withdraw_at': datetime.datetime.utcnow() }})
            self.redirect("/history")
            return
        try:
            history['user'] = self.application.db.users.find_one({"_id": ObjectId(self.get_argument('user_id', None))})
            history['device'] = self.application.db.devices.find_one({"_id": ObjectId(self.get_argument('device_id', None))})
            history['withdraw_at'] = None
            history['borrowed_at'] = datetime.datetime.utcnow()
            coll.insert_one(history)
        except Exception:
            self.render("error_pages/400.html")
        self.redirect("/device")