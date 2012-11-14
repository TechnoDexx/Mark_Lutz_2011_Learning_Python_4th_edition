#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def countLines(file):
	file.seek(0)
	return len(file.readlines())

def countChars(file):
	file.seek(0)
	return len(file.read())

def test(name):
	file = open(name)
	print 'Lines: ' + str(countLines(file))
	print 'Chars: ' + str(countChars(file))

test(sys.argv[1])
