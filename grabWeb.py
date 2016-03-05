#!/usr/bin/env python

from urllib import urlretrieve

def firstNotBlank(lines):
	for eachLine in lines:
		if not eachLine.strip():
			continue
		else:
			return eachLine
def firstLast(webpage):
	f = open(webpage)
	lines = f.readlines()
	f.close()
	print firstNotBlank(lines) ,
	lines.reverse()
	print firstNotBlank(lines) ,
def download(url = 'http://www.baidu.com',proccess=firstLast)	:
	try:
		retval = urlretrieve(url)[0]
	except IOEror:
		retval = None
	if retval:
		proccess(retval)


if __name__ == '__main__':
	download()
