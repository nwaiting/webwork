#coding=utf-8

from tornado import web

class LoginHandler(web.RequestHandler):
    def post(self):
        print self.get_argument("username")
        print self.get_argument("userpwd")
        self.write('ok')
