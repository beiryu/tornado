
import tornado.web
from admin.handlers import BaseHandler
import tornado.httpclient
import tornado.httpserver
import tornado.gen

class CovidHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("https://api.covidtracking.com/v1/us/current.json", validate_cert=False)
        self.write(response.body)