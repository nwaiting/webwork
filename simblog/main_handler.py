#!/usr/bin/env python
# coding: utf-8

"""
@file: main_handler.py
@time: 2016/12/20 14:01
"""
from tornado import web
import json


class MainHandler(web.RequestHandler):
    def get(self):
        print "main index"
        res = {"welcome": "welcome to tornado", "errno": 0}
        # self.write(json.dumps(res))
        self.render("index.html")


if __name__ == "__main__":
    pass
