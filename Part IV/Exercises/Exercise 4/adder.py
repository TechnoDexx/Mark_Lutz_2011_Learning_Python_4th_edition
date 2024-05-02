#!/usr/bin/env python
# -*- coding: utf-8 -*-
def adder(**args):
	args = list(args.values())
	sum = args[0]
	for next in args[1:]:
		sum += next
	return sum


print(adder(good=2, bad=3, ugly=4))
print(adder(good='spam', bad='eggs', ugly='toast'))
print(adder(good=['a', 'b'], bad=['c', 'd'], ugly=['e', 'f']))
