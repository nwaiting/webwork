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
from main_handler import MainHandler
from blog_handler import BlogHandler


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/blog", BlogHandler)
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

