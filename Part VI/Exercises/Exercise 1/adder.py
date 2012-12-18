#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Adder:
	def __init__(self, orig):
		self.data = orig

	def add(self, x, y):
		print("Not Implemented")

	def __add__(self, summand):
		return self.add(self.data, summand)

class ListAdder(Adder):
	def add(self, x, y):
		res = x.copy()
		res.extend(y)
		return res
	
class DictAdder(Adder):
	def add(self, x, y):
		res = x.copy()
		res.update(y)
		return res

if __name__ == '__main__':
	print('Testing ListAdder.')
	l1 = [1, 2, 3]
	l2 = [9, 8, 7]
	lRes = ['a', 'b', 'c']
	listAdder = ListAdder(lRes)
	print('Initially lRes = {0}'.format(lRes))
	print('ListAdder.add({0}, {1}): {2}'.format(l1, l2, listAdder.add(l1, l2)))
	print('lRes: {0}'.format(lRes))
	print('lRes + {0} = {1}'.format(l1, listAdder + l1))
	print('lRes: {0}'.format(lRes))
	
	print('\nTesting DictAdder.')
	d1 = {1: 'a', 2: 'b', 3: 'c'}
	d2 = {9: 'z', 8: 'y', 7: 'x'}
	dRes = {42:'spam'}
	dictAdder = DictAdder(dRes)
	print('Initially dRes = {0}'.format(dRes))
	print('DictAdder.add({0}, {1}): {2}'.format(d1, d2, dictAdder.add(d1, d2)))
	print('dRes: {0}'.format(dRes))
	print('dRes + {0} = {1}'.format(d1, dictAdder + d1))
	print('dRes: {0}'.format(dRes))
