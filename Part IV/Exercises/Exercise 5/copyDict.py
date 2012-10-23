#!/usr/bin/env python
def copyDict(dict):
	newDict = {}
	for key in dict.keys():
		newDict[key] = dict[key]
	return newDict
