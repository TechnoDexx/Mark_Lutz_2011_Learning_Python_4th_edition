#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, mytimer

reps = 10000
repslist = range(reps)

from math import sqrt


def mathMod():
	for i in repslist:
		res = sqrt(i)
	return res


def powCall():
	for i in repslist:
		res = pow(i, 0.5)
	return res


def powExpr():
	for i in repslist:
		res = i ** 0.5
	return res


print(sys.version)
for tester in (mytimer.timer, mytimer.best):
	print('<%s>' % tester.__name__)
	for test in (mathMod, powCall, powExpr):
		elapsed, result = tester(test)
		print('-' * 35)
		print('%s: %.5f => %s' % (test.__name__, elapsed, result))
