#coding=utf-8

from tornado import web

class LoginHandler(web.RequestHandler):
    def post(self):
        handlertype = self.get_argument("cmd")
        if handlertype == 'reg':
            print self.get_argument("usertel")
            print self.get_argument("usermail")
        print self.get_argument("username")
        print self.get_argument("pwd")

        self.write('ok')
