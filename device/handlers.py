import datetime
import tornado.web

from admin.handlers import BaseHandler
from bson.objectid import ObjectId


class DeviceHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render(
            'devices.html',
            devices = self.application.db.devices.find(),
            users = list(self.application.db.users.find()),
        )


class DeviceEditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id=None):
        device = dict()
        if id:
            coll = self.application.db.devices
            device = coll.find_one({"_id": ObjectId(id)})
        self.render(
            "edit-device.html",
            device=device
        )

    def post(self, id=None):
        id = self.get_argument('id', None)
        device_fields = ['name', 'description', 'status', 'employee']
        coll = self.application.db.devices
        device = dict()
        if id:
            device = coll.find_one({"_id": ObjectId(id)})
        for key in device_fields:
            device[key] = self.get_argument(key, None)
        if id:
            coll.update_one({"_id": ObjectId(id)}, {'$set': device})
        else:
            device['date_added'] = datetime.datetime.utcnow()
            coll.insert_one(device)
        self.redirect("/device")


class DeviceRemoveHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self, id=None):
        if id:
            self.application.db.devices.delete_one({"_id": ObjectId(id)})
        self.redirect("/device")