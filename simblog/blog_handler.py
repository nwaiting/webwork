#!/usr/bin/env python
# coding: utf-8

"""
@file: blog_handler.py
@time: 2016/12/20 14:29
"""
from tornado import web
import json
import datetime


class BlogHandler(web.RequestHandler):
    def get(self):
        res = 'welcome to blog service'
        blog = {'title': "my block", 'date': datetime.datetime.now(), 'content': ";asjdf;jasd;fj;asjdglasjd;jsa;dgjaslgja\njsadfj;asjdf\nlhsdlfhasldkf\ndslhflashdfl\nsdlfhasldfk\nsljdflsadfl\n"}
        self.render("blog.html", page_title="my block", blog=blog)

    def post(self):
        res = 'welcome to blog service'
        print res
        json_res = {"response": res, "errno": 0}
        self.write(json.dumps(json_res))


if __name__ == "__main__":
    pass
