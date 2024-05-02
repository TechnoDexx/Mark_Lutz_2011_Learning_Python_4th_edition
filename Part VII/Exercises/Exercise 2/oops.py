#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, traceback

def safe(entry, *args):
	try:
		entry(*args)
	except:
		traceback.print_exc()
		print('Got', sys.exc_info()[0], sys.exc_info()[1])

def doomed():
	try:
		oops()
	except IndexError:
		print('caught an index error!')
	except MyError as data:
		print('caught error:', MyError, data)
	else:
		print('no error caught...')

if __name__ == '__main__':
	doomed()
