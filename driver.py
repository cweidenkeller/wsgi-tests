#!/usr/bin/env python
if __name__ == '__main__':
    from gevent import pywsgi
    from paste.deploy import loadapp
    pywsgi.WSGIServer(('0.0.0.0', 80),loadapp('config:configured.ini', relative_to='.')).serve_forever(60)

