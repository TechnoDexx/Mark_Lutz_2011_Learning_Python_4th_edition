#!/usr/bin/env python
# -*- coding: utf-8 -*-
def addDict(dict1, dict2):
	newDict = {}
	for key in dict1.keys():
		newDict[key] = dict1[key]
	for key in dict2.keys():
		newDict[key] = dict2[key]
	return newDict
