#!/usr/bin/python
#coding:utf8

import pycurl
import StringIO

def getURLContent_pycurl(url):
    c=pycurl.Curl()
    c.setopt(pycurl.URL,url)
    b=StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION,b.write)
    c.setopt(pycurl.FOLLOWLOCATION,1)
    c.setopt(pycurl.MAXREDIRS,5)

    c.perform()
    return b.getvalue()

url='http://www.baidu.com'

content = getURLContent_pycurl(url)

print content

