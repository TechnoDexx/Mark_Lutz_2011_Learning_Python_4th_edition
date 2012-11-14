#!/usr/bin/env python
# -*- coding: utf-8 -*-
L = []
for pow in range(7): L.append(2 ** pow)
X = 5
num = 2 ** X
if num in L:
	print(num, 'at index', L.index(num))
else:
	print(num, 'not found')
