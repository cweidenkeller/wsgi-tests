#!/usr/bin/env python
from pprint import pprint
from flask import Flask
from werkzeug.wrappers import Response
import sys
class Werk:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
    def __call__(self, environ, start_response, exc_info=None):
        try:
            raise Exception
        except Exception:
            exc_info = sys.exc_info()
        print "At the exc_info shit\n"
        print str(exc_info)
        print "end of it"
        start_response('500 OK', [('X-I-am-in-the-main-app', 'text/plain')], exc_info)
        return ['ello']
class Caseless:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response, exc_info):
        rr = 'apples'
        if exc_info != None:
            rr = 'jjjjjj'
            raise ZeroDivisionError
        status = '200 OK'
        response_headers = [('X-I-am-in-the-middlware', 'text/plain')]
        resp = self.app(environ, start_response)
        a = ''
        for i in resp:
            a += i
        #start_response(status, response_headers)
        return[a + rr]
def app_factory(global_config, name, greeting):
    return Werk(name, greeting)
def filter_factory(app, global_config):
    return Caseless(app)  
