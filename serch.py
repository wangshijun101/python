#!/usr/bin/env python
# -*- coding: utf-8 -*-
'testing for io_search'
__author__='Joseph'

import os
import sys

def search(dir_now,key):
	for f in os.listdir(dir_now):
		if os.path.isdir(f):
			search(os.path.join(dir_now,f),key)
		else:
			if f.find(key) != -1:
				print os.path.join(dir_now,f)
def main():
	if len(sys.argv) != 2:
		print u'参数个数有误！'
		return -1
	else:
		dir_now = '.'
		search(dir_now,sys.argv[1])
		return 1
if __name__ == '__main__':
	main()

