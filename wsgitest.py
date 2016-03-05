#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return '<h1>Hello.%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

httpd = make_server('',8080,application)
print "serving HTTP on PORT 8080..."

httpd.serve_forever()

