#!/usr/bin/env python
from pprint import pprint
from flask import Flask
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    raise Exception
    return 'woo'

class Configured:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s!\n' % (self.greeting, self.name)]
class Caseless:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        pprint(environ)
        rr = 'apples'
        if sys.exc_info()[0] != None:
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
def app_factory(global_config):
    return app
def filter_factory(app, global_config):
    return Caseless(app)  
