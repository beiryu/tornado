import uuid
import pymongo
import tornado.web
import tornado.websocket
from datetime import datetime
from admin.handlers import BaseHandler


class Messager(object):
    threads = {}
    callbacks = []
    messager_db = None
    current_user = None

    def register(self, callback):
        self.callbacks.append(callback)

    def registerUser(self, session, user):
        self.current_user = user
        self.threads[session] = user

    def sendMessage(self, session, message):
        self.messager_db.insert_one({
            "username": self.current_user,
            "message": message,
            "date": datetime.utcnow() 
        })
        self.current_user = self.getUser(session)
        self.notifyCallbacks()

    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)

    def callbackHelper(self, callback):
        callback(self.getMessage(), self.current_user)

    def getMessage(self):
        return self.messager_db.find_one(sort=[( '_id', pymongo.DESCENDING )])['message']

    def getUser(self, session):
        return self.threads[uuid.UUID(session)].decode("utf-8") 

    def unregister(self, callback):    
        self.callbacks.remove(callback)

    def registerDatabase(self, database):
        self.messager_db = database


class MessagerHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        session = uuid.uuid4()
        self.application.messager.registerDatabase(self.application.db.messages)
        self.application.messager.registerUser(session, self.current_user)
        self.render("chat.html", session=session, user=self.current_user, messages=self.application.db.messages.find())


class ChatHandler(tornado.web.RequestHandler):
    def post(self):
        action = self.get_argument('action')
        session = self.get_argument('session')
        message = self.get_argument('message')
        if not session:
            self.set_status(400)
            return
        if action == 'send':
            self.application.messager.sendMessage(session, message)
        else:
            self.set_status(400)


class StatusHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.application.messager.register(self.callback)
    def on_close(self):
        self.application.messager.unregister(self.callback)
    def on_message(self, message):
        pass
    def callback(self, message, user):
        self.write_message('{"messageReturn":"%s", "user": "%s"}' % (message, user))