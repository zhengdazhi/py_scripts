#!/usr/bin/env python
#coding:utf8

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	#return '<h1>Hello,web!</h1>'
	return '<h1>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')


