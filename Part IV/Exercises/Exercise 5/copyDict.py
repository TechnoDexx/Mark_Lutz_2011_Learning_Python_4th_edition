#!/usr/bin/env python
# -*- coding: utf-8 -*-
def copyDict(dict):
	newDict = {}
	for key in dict.keys():
		newDict[key] = dict[key]
	return newDict
