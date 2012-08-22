#!/usr/bin/env python
from pprint import pprint
from flask import Flask
import sys
app = Flask(__name__)
app.debug = True
@app.route('/')
def hello_world():
    raise Exception
    return 'woo'
class Caseless:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response, exc_info=None):
        pprint(environ)
        rr = 'apples'
        if exc_info[0] != None:
            rr = 'jjjjjj'
            raise ZeroDivisionError
        status = '200 OK'
        response_headers = [('X-I-am-in-the-middlware', 'text/plain')]
        resp = self.app(environ, start_response)
        a = ''
        for i in resp:
            a += i
        #start_response(status, response_headers)
        return[rr + a ]
def app_factory(global_config, name, greeting):
    return app
def filter_factory(app, global_config):
    return Caseless(app)  
