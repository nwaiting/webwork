#coding=utf-8

from tornado import web

class MainHandler(web.RequestHandler):
    def get(self):
        print "enter MainHandler get"
        self.render('login.html')
