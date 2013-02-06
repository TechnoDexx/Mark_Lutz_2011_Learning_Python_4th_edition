#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Поиск наибольшего файла в единственном каталоге
import os, glob
if sys.platform[:3] == 'win':
	dirname = r'C:\Python30\Lib'
else:
	dirname = '/usr/lib/python'
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
	filesize = os.path.getsize(filename)
	allsizes.append((filesize, filename))
allsizes.sort()
print(allsizes[-1:])
