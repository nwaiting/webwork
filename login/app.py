#!/usr/bin/env python
# coding: utf-8

"""
@file: app.py.py
@time: 2016/12/20 10:00
"""
import os
from tornado import ioloop
from tornado import web
from tornado import httpserver
from userhandler import LoginHandler
from mainhandler import MainHandler

class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/login.html", LoginHandler),
            (r"/", MainHandler)
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        web.Application.__init__(self, handlers=handlers, **settings)


if __name__ == "__main__":
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(4096)
    print "tornado service start "
    ioloop.IOLoop.current().start()
