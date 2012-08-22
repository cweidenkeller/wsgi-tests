#!/usr/bin/env python
from wsgiref.simple_server import make_server
from webob import Request
def app(environ, start_response, exc_info=None):
    start_response('200 OK', [('Content-type', 'text/html')])
    req = Request(environ)
    a = ['<html><h3>Headers:</h3>']
    for (key, value) in req.headers.items():
        a.append(str(key) + ' ' + str(value) + '<br />')
    a.append('<h3>Method:</h3>')
    a.append(req.method + '<br />')
    a.append('<h3>Url:</h3></html>')
    a.append(req.url + '<br />')
    a.append('<h3>Environ:</h3>')
    for (key, value) in environ.items():
        a.append(str(key) + ' ' + str(value) + '<br /></html>')
    return a
if __name__ == '__main__':
    httpd = make_server('', 80, app).serve_forever()

