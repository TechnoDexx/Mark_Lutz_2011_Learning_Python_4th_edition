#!/usr/bin/env python
# -*- coding: utf-8 -*-
def adder(a, *args):
	sum = a
	for next in args:
		sum += next
	return sum


print(adder(2, 3, 4))
print(adder('spam', 'eggs', 'toast'))
print(adder(['a', 'b'], ['c', 'd'], ['e', 'f']))
