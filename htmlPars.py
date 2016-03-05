#!/usr/bin/env python
# -*- coding:utf-8 -*-
from HTMLParser import HTMLParser
import urllib
class MyHtmlParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.key ={'time':None,'event-title':None,'event-location':None}
	def handle_starttag(self,tag,attrs):
		if tag == 'time':
			self.key['time'] = True
		if tag == 
